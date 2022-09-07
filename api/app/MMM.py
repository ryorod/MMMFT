# https://colab.research.google.com/drive/10ZAdEwHDbL1lVcUGeCdj9FxXnQSNFSH4?usp=sharing

import re
import base64
import json
import mmm_api as mmm
from midi2audio import FluidSynth
from IPython.display import display, Javascript
from js2py import eval_js

class MMM:
    def __init__(self):
        self.reset_midi()
        with open('./js/demo.js', 'r') as f:
            self.js = Javascript(f.read())
        display(self.js)
        eval_js("start_up()")

    def get_current_midi(self):
        with open("current_midi.json", "r") as f:
            return json.load(f)

    def save_current_midi(self, midi_json):
        with open("current_midi.json", "w") as f:
            json.dump(midi_json, f)

    def update_gui_midi(self, midi_json):
        assert isinstance(midi_json, dict)
        # output.eval_js('''build_from_midi(JSON.parse('{}'))'''.format(json.dumps(midi_json)))

    def generate_callback(self, status):
        midi_json = self.get_current_midi()
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
        self.mix_tracks_in_json(midi_json)

        # update the midi
        self.update_gui_midi(midi_json)

        # save the midi
        self.save_current_midi(midi_json)

    # this should work now basically
    def mix_tracks_in_json(self, midi_json, levels=None):
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

    def play_callback(self, status):
        midi_json = self.get_current_midi()
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
        # display(HTML(script))

    def add_midi_callback(self, status, raw):  
        data = re.search(r'base64,(.*)', raw).group(1)
        with open("input.mid", "wb") as f:
            f.write(base64.b64decode(data))
  
        enc = mmm.TrackDensityEncoder()
        midi_json = json.loads(enc.midi_to_json("input.mid"))
        bars_to_keep = list(range(len(midi_json["tracks"][0]["bars"])))  
        midi_json = json.loads(mmm.prune_empty_tracks(json.dumps(midi_json), bars_to_keep))

        # add new midi to what we already have
        # first filter tracks via status
        cur_midi_json = self.get_current_midi()
        if len(cur_midi_json) and len(status.get("tracks",[])):
            valid_tracks = []
            for track in status.get("tracks",[]):
                valid_tracks.append( cur_midi_json["tracks"][track["track_id"]] )
            cur_midi_json["tracks"] = valid_tracks
            bars_to_keep = list(range(len(cur_midi_json["tracks"][0]["bars"])))  
            cur_midi_json = json.loads(mmm.prune_empty_tracks(json.dumps(cur_midi_json), bars_to_keep))

            midi_json = json.loads(mmm.append_piece(json.dumps(cur_midi_json), json.dumps(midi_json)))

        if len(midi_json.get("tracks",[])) == 0:
            # output.eval_js('''build_snackbar("Invalid MIDI file. Make sure each track has atleast 8 bars.")''')
            return

        if not "tempo" in midi_json:
            midi_json["tempo"] = 120
  
        # get density for tracks
        midi_str = json.dumps(midi_json)
        midi_str = mmm.update_note_density(midi_str)
        midi_str = mmm.update_av_polyphony_and_note_duration(midi_str)
        midi_json = json.loads(midi_str)

        # normalize volume (works in place)
        self.mix_tracks_in_json(midi_json)

        # update the midi
        self.update_gui_midi(midi_json)

        # save the midi
        self.save_current_midi(midi_json)

    def download_midi_callback(self):
        from zipfile import ZipFile
        midi_json = self.get_current_midi()
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
        # output.eval_js('''run_download_zip("{}")'''.format(encoded_data))

    def reset_midi(self):
        self.save_current_midi({})
