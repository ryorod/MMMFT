import os
import re
import base64
import copy
import time
import glob
import json
import random
import itertools
import numpy as np
from subprocess import call
import mmm_api as mmm
from copy import deepcopy

from midi2audio import FluidSynth

import logging
logging.disable(logging.CRITICAL)

# read the demo.html from the web
import urllib.request
url = 'http://www.sfu.ca/~jeffe/MMM/DEMO/v2/demo.html'
response = urllib.request.urlopen(url)
html = response.read().decode("utf-8")

# read demo.html from local
#with open("../demo.html", "r") as f:
#  html = f.read()

def read_track_map():
  with open("track_map.json", "r") as f:
    return json.load(f)

def write_track_map(x):
  with open("track_map.json", "w") as f:
    json.dump(x,f)

def get_current_midi():
  with open("current_midi.json", "r") as f:
    return json.load(f)

def save_current_midi(midi_json):
  with open("current_midi.json", "w") as f:
    json.dump(midi_json, f)

def save_status(status):
  with open("current_status.json", "w") as f:
    json.dump(status, f)

def update_gui_midi(midi_json):
  assert isinstance(midi_json, dict)
  output.eval_js('''build_from_midi(JSON.parse('{}'))'''.format(json.dumps(midi_json)))

def show_track(piece, i):
  print("="*30)
  for bar in piece["tracks"][i]["bars"]:
    for event in bar.get("events",[]):
      print(piece["events"][event])
  print("="*30)

def generate_callback(status):
  midi_json = get_current_midi()
  midi_json["resolution"] = midi_json.get("resolution",12)
  midi_json["tempo"] = 120

  # before we start make the midi_json
  # and the status have the same track order
  # i.e. re-order midi_json to match status
  # what if we do the reverse? does this simplify things?
  # but then it will have to be re-ordered at the end to preserve gui
  ordered_midi_json_tracks = []
  track_gui_map = {}
  num_bars = len(status["tracks"][0]["selected_bars"])
  num_tracks = len(midi_json.get("tracks",[]))
  for i,track in enumerate(status["tracks"]):
    if track["track_id"] < num_tracks:
      midi_track = midi_json["tracks"][track["track_id"]]
    else:
      midi_track = {}
      midi_track["trackType"] = track["track_type"]
      midi_track["bars"] = [{"events":[],"internalBeatLength":4,"tsNumerator":4,"tsDenominator":4} for _ in range(num_bars)]
    
    # override instrument via status
    midi_track["instrument"] = track["instrument_num"]
    midi_track["trackType"] = track["track_type"]

    ordered_midi_json_tracks.append( midi_track )

    track_gui_map[i] = track["track_id"]
    track["track_id"] = i
  midi_json["tracks"] = ordered_midi_json_tracks


  # format param
  param = {
    "tracks_per_step": status.pop("tracks_per_step"),
    "bars_per_step": status.pop("bars_per_step"),
    "model_dim": status.pop("model_dim"),
    "percentage": status.pop("percentage"),
    "batch_size": 1,
    "temperature": status.pop("temperature"),
    "max_steps": 0,
    "polyphony_hard_limit": 6,
    "shuffle": status.pop("shuffle"),
    "verbose": False,
    "ckpt": "/content/model.pt"
  }

  # format status
  valid_status = {"tracks" : []}
  for track in status.get("tracks",[]):
    track.pop("mute")
    track.pop("solo")
    track.pop("instrument_num")
    track["autoregressive"] = track.pop("resample")
    valid_status["tracks"].append( track )
  
  # run generate
  #show_track(midi_json, 0)
  piece = json.dumps(midi_json)
  status = json.dumps(valid_status)
  param = json.dumps(param)
  midi_str = mmm.sample_multi_step(piece, status, param)
  #show_track(json.loads(midi_str), 0)

  # get density for tracks
  midi_str = mmm.update_note_density(midi_str)
  midi_str = mmm.update_av_polyphony_and_note_duration(midi_str)
  midi_json = json.loads(midi_str)

  # make sure each bar has events
  for track in midi_json["tracks"]:
    for bar in track["bars"]:
      bar["events"] = bar.get("events",[])
  midi_json["events"] = midi_json.get("events",[])

  # normalize volume (works in place)
  mix_tracks_in_json(midi_json)

  # update the midi
  update_gui_midi(midi_json)

  # save the midi
  save_current_midi(midi_json)

# this should work now basically
def mix_tracks_in_json(midi_json, levels=None):
  AUDIO_LEVELS = [12,24,36,48,60,72,84,96,108,120]
  for track_num, track in enumerate(midi_json.get("tracks",[])):
    for bar in track.get("bars",[]):
      for event_index in bar.get("events",[]):
        event = midi_json["events"][event_index]
        if event["velocity"] > 0:
          audio_level = AUDIO_LEVELS[8]
          if levels is not None:
            audio_level = AUDIO_LEVELS[levels[track_num]]
          event["velocity"] = audio_level

def play_callback(status):
  midi_json = get_current_midi()
  tracks = []
  for track in status["tracks"]:
    tid = int(track["track_id"])
    if track["solo"]:
      tracks = [ tid ]
      break
    elif not track["mute"]:
      tracks.append( tid )

  encoder = mmm.TrackDensityEncoder()
  
  midi_json["tempo"] = status["tempo"]
  #mix_tracks_in_json(midi_json)
  raw = json.dumps(midi_json)
  bars_to_keep = list(range(status["nbars"]))
  raw = mmm.prune_tracks(raw, tracks, bars_to_keep)
  encoder.json_to_midi(raw, "current.mid")
  FluidSynth("font.sf2").midi_to_audio('current.mid', 'current.wav')
  
  # set the src and play
  sound = open("current.wav", "rb").read()
  sound_encoded = base64.b64encode(sound).decode('ascii')
  script = '''<script type="text/javascript">
  var audio = document.querySelector("#beep");
  audio.src = "data:audio/wav;base64,{raw_audio}";
  audio.play();
  </script>'''.format(raw_audio=sound_encoded)
  display(HTML(script))

def add_midi_callback(status, raw):  
  data = re.search(r'base64,(.*)', raw).group(1)
  with open("input.mid", "wb") as f:
    f.write(base64.b64decode(data))
  
  enc = mmm.TrackDensityEncoder()
  midi_json = json.loads(enc.midi_to_json("input.mid"))
  bars_to_keep = list(range(len(midi_json["tracks"][0]["bars"])))  
  midi_json = json.loads(mmm.prune_empty_tracks(json.dumps(midi_json), bars_to_keep))

  # add new midi to what we already have
  # first filter tracks via status
  cur_midi_json = get_current_midi()
  if len(cur_midi_json) and len(status.get("tracks",[])):
    valid_tracks = []
    for track in status.get("tracks",[]):
      valid_tracks.append( cur_midi_json["tracks"][track["track_id"]] )
    cur_midi_json["tracks"] = valid_tracks
    bars_to_keep = list(range(len(cur_midi_json["tracks"][0]["bars"])))  
    cur_midi_json = json.loads(mmm.prune_empty_tracks(json.dumps(cur_midi_json), bars_to_keep))

    midi_json = json.loads(mmm.append_piece(json.dumps(cur_midi_json), json.dumps(midi_json)))

  if len(midi_json.get("tracks",[])) == 0:
    output.eval_js('''build_snackbar("Invalid MIDI file. Make sure each track has atleast 8 bars.")''')
    return

  if not "tempo" in midi_json:
    midi_json["tempo"] = 120
  
  # get density for tracks
  midi_str = json.dumps(midi_json)
  midi_str = mmm.update_note_density(midi_str)
  midi_str = mmm.update_av_polyphony_and_note_duration(midi_str)
  midi_json = json.loads(midi_str)

  # normalize volume (works in place)
  mix_tracks_in_json(midi_json)

  # update the midi
  update_gui_midi(midi_json)

  # save the midi
  save_current_midi(midi_json)

def download_midi_callback():
  midi_json = get_current_midi()
  enc = mmm.TrackDensityEncoder()
  enc.json_to_midi(json.dumps(midi_json),"download.mid")
  with open("download.mid", "rb") as f:
    encoded_data = base64.b64encode(f.read()).decode('utf-8')
  output.eval_js('''run_download("{}")'''.format(encoded_data))

def download_midi_callback():
  from zipfile import ZipFile
  midi_json = get_current_midi()
  enc = mmm.TrackDensityEncoder()
  with ZipFile('download.zip', 'w') as z:
    for i in range(len(midi_json.get("tracks",[]))):
      save_path = "track_{}.mid".format(i)
      enc.json_track_to_midi(json.dumps(midi_json),save_path,i)
      z.write(save_path)
    try:
      enc.json_to_midi(json.dumps(midi_json), "full.mid")
      z.write("full.mid")
    except:
      pass
  with open("download.zip", "rb") as f:
    encoded_data = base64.b64encode(f.read()).decode('utf-8')
  output.eval_js('''run_download_zip("{}")'''.format(encoded_data))

def reset_midi():
  save_current_midi({})

# =============================================
# setup

# start out with blank midi
save_current_midi({})

GOOGLE_COLAB = True

# register python callbacks
if GOOGLE_COLAB:
  output.register_callback('reset_midi', reset_midi)
  output.register_callback('generate_callback', generate_callback)
  output.register_callback('play_callback', play_callback)
  output.register_callback('add_midi_callback', add_midi_callback)
  output.register_callback('save_current_midi', save_current_midi)
  output.register_callback('download_midi_callback', download_midi_callback)

  display(HTML(html))
  output.eval_js("start_up()");
  display(Javascript("google.colab.output.setIframeHeight('1400px');"))