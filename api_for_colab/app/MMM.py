# https://colab.research.google.com/drive/10ZAdEwHDbL1lVcUGeCdj9FxXnQSNFSH4?usp=sharing

from datetime import datetime
import json
from typing import List
from boto3 import Session
import mmm_api as mmm
from midi2audio import FluidSynth
from utils.lib import get_status
from utils.const import MIDI_JSON_FILENAME, BUCKET_NAME

class MMM:
    def __init__(self, hash: str):
        self.hash = hash

    def get_current_midi(self):
        sess = Session()
        s3 = sess.client('s3')
        try:
            res = s3.get_object(Bucket=BUCKET_NAME, Key=f'{self.hash}/{MIDI_JSON_FILENAME}')
            body = res['Body'].read()
            return json.loads(body.decode('utf-8'))
        except:
            return json.loads(r'{}')

    def save_current_midi(self, midi_json):
        with open(MIDI_JSON_FILENAME, "w") as f:
            json.dump(midi_json, f)
        sess = Session()
        s3 = sess.client('s3')
        s3.upload_file(MIDI_JSON_FILENAME, BUCKET_NAME, f'{self.hash}/{MIDI_JSON_FILENAME}')
        return s3

    def generate(self, instruments: List[str]):
        self.instruments = instruments
        status = get_status(instruments=self.instruments)
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

        # save the midi
        s3 = self.save_current_midi(midi_json)

        # save .mid and .wav
        return self.save_midi_and_wav(s3)

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

    def save_midi_and_wav(self, s3_client):
        status = get_status(instruments=self.instruments)
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

        # filename
        all_inst = '-'.join(self.instruments)
        date_time = datetime.now()
        datetime_num = str(date_time.year) + str(date_time.month) + str(date_time.day) + str(date_time.hour) + str(date_time.minute) + str(date_time.second)
        filename = all_inst + '__' + datetime_num

        # upload .mid
        s3_client.upload_file('current.mid', BUCKET_NAME, f'{self.hash}/{filename}.mid')

        # upload .wav
        FluidSynth("font.sf2").midi_to_audio('current.mid', 'current.wav')
        s3_client.upload_file('current.wav', BUCKET_NAME, f'{self.hash}/{filename}.wav')

        return filename

    def reset_midi(self):
        self.save_current_midi({})
