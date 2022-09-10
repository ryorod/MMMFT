# https://colab.research.google.com/drive/10ZAdEwHDbL1lVcUGeCdj9FxXnQSNFSH4?usp=sharing

import re
import base64
import json
from typing import List
from boto3 import Session
import mmm_api as mmm
from midi2audio import FluidSynth
# from IPython.display import display, Javascript
# from js2py import eval_js

INST_MAP = {'acoustic_grand_piano': 0, 'bright_acoustic_piano': 1, 'electric_grand_piano': 2, 'honky_tonk_piano': 3, 'electric_piano_1': 4, 'electric_piano_2': 5, 'harpsichord': 6, 'clavi': 7, 'celesta': 8, 'glockenspiel': 9, 'music_box': 10, 'vibraphone': 11, 'marimba': 12, 'xylophone': 13, 'tubular_bells': 14, 'dulcimer': 15, 'drawbar_organ': 16, 'percussive_organ': 17, 'rock_organ': 18, 'church_organ': 19, 'reed_organ': 20, 'accordion': 21, 'harmonica': 22, 'tango_accordion': 23, 'acoustic_guitar_nylon': 24, 'acoustic_guitar_steel': 25, 'electric_guitar_jazz': 26, 'electric_guitar_clean': 27, 'electric_guitar_muted': 28, 'overdriven_guitar': 29, 'distortion_guitar': 30, 'guitar_harmonics': 31, 'acoustic_bass': 32, 'electric_bass_finger': 33, 'electric_bass_pick': 34, 'fretless_bass': 35, 'slap_bass_1': 36, 'slap_bass_2': 37, 'synth_bass_1': 38, 'synth_bass_2': 39, 'violin': 40, 'viola': 41, 'cello': 42, 'contrabass': 43, 'tremolo_strings': 44, 'pizzicato_strings': 45, 'orchestral_harp': 46, 'timpani': 47, 'string_ensemble_1': 48, 'string_ensemble_2': 49, 'synth_strings_1': 50, 'synth_strings_2': 51, 'choir_aahs': 52, 'voice_oohs': 53, 'synth_voice': 54, 'orchestra_hit': 55, 'trumpet': 56, 'trombone': 57, 'tuba': 58, 'muted_trumpet': 59, 'french_horn': 60, 'brass_section': 61, 'synth_brass_1': 62, 'synth_brass_2': 63, 'soprano_sax': 64, 'alto_sax': 65, 'tenor_sax': 66, 'baritone_sax': 67, 'oboe': 68, 'english_horn': 69, 'bassoon': 70, 'clarinet': 71, 'piccolo': 72, 'flute': 73, 'recorder': 74, 'pan_flute': 75, 'blown_bottle': 76, 'shakuhachi': 77, 'whistle': 78, 'ocarina': 79, 'lead_1_square': 80, 'lead_2_sawtooth': 81, 'lead_3_calliope': 82, 'lead_4_chiff': 83, 'lead_5_charang': 84, 'lead_6_voice': 85, 'lead_7_fifths': 86, 'lead_8_bass__lead': 87, 'pad_1_new_age': 88, 'pad_2_warm': 89, 'pad_3_polysynth': 90, 'pad_4_choir': 91, 'pad_5_bowed': 92, 'pad_6_metallic': 93, 'pad_7_halo': 94, 'pad_8_sweep': 95, 'fx_1_rain': 96, 'fx_2_soundtrack': 97, 'fx_3_crystal': 98, 'fx_4_atmosphere': 99, 'fx_5_brightness': 100, 'fx_6_goblins': 101, 'fx_7_echoes': 102, 'fx_8_sci_fi': 103, 'sitar': 104, 'banjo': 105, 'shamisen': 106, 'koto': 107, 'kalimba': 108, 'bag_pipe': 109, 'fiddle': 110, 'shanai': 111, 'tinkle_bell': 112, 'agogo': 113, 'steel_drums': 114, 'woodblock': 115, 'taiko_drum': 116, 'melodic_tom': 117, 'synth_drum': 118, 'reverse_cymbal': 119, 'guitar_fret_noise': 120, 'breath_noise': 121, 'seashore': 122, 'bird_tweet': 123, 'telephone_ring': 124, 'helicopter': 125, 'applause': 126, 'gunshot': 127, 'drum_0': 0, 'drum_1': 1, 'drum_2': 2, 'drum_3': 3, 'drum_4': 4, 'drum_5': 5, 'drum_6': 6, 'drum_7': 7, 'drum_8': 8, 'drum_9': 9, 'drum_10': 10, 'drum_11': 11, 'drum_12': 12, 'drum_13': 13, 'drum_14': 14, 'drum_15': 15, 'drum_16': 16, 'drum_17': 17, 'drum_18': 18, 'drum_19': 19, 'drum_20': 20, 'drum_21': 21, 'drum_22': 22, 'drum_23': 23, 'drum_24': 24, 'drum_25': 25, 'drum_26': 26, 'drum_27': 27, 'drum_28': 28, 'drum_29': 29, 'drum_30': 30, 'drum_31': 31, 'drum_32': 32, 'drum_33': 33, 'drum_34': 34, 'drum_35': 35, 'drum_36': 36, 'drum_37': 37, 'drum_38': 38, 'drum_39': 39, 'drum_40': 40, 'drum_41': 41, 'drum_42': 42, 'drum_43': 43, 'drum_44': 44, 'drum_45': 45, 'drum_46': 46, 'drum_47': 47, 'drum_48': 48, 'drum_49': 49, 'drum_50': 50, 'drum_51': 51, 'drum_52': 52, 'drum_53': 53, 'drum_54': 54, 'drum_55': 55, 'drum_56': 56, 'drum_57': 57, 'drum_58': 58, 'drum_59': 59, 'drum_60': 60, 'drum_61': 61, 'drum_62': 62, 'drum_63': 63, 'drum_64': 64, 'drum_65': 65, 'drum_66': 66, 'drum_67': 67, 'drum_68': 68, 'drum_69': 69, 'drum_70': 70, 'drum_71': 71, 'drum_72': 72, 'drum_73': 73, 'drum_74': 74, 'drum_75': 75, 'drum_76': 76, 'drum_77': 77, 'drum_78': 78, 'drum_79': 79, 'drum_80': 80, 'drum_81': 81, 'drum_82': 82, 'drum_83': 83, 'drum_84': 84, 'drum_85': 85, 'drum_86': 86, 'drum_87': 87, 'drum_88': 88, 'drum_89': 89, 'drum_90': 90, 'drum_91': 91, 'drum_92': 92, 'drum_93': 93, 'drum_94': 94, 'drum_95': 95, 'drum_96': 96, 'drum_97': 97, 'drum_98': 98, 'drum_99': 99, 'drum_100': 100, 'drum_101': 101, 'drum_102': 102, 'drum_103': 103, 'drum_104': 104, 'drum_105': 105, 'drum_106': 106, 'drum_107': 107, 'drum_108': 108, 'drum_109': 109, 'drum_110': 110, 'drum_111': 111, 'drum_112': 112, 'drum_113': 113, 'drum_114': 114, 'drum_115': 115, 'drum_116': 116, 'drum_117': 117, 'drum_118': 118, 'drum_119': 119, 'drum_120': 120, 'drum_121': 121, 'drum_122': 122, 'drum_123': 123, 'drum_124': 124, 'drum_125': 125, 'drum_126': 126, 'drum_127': 127}
REV_INST_MAP = {0: 'acoustic_grand_piano', 1: 'bright_acoustic_piano', 2: 'electric_grand_piano', 3: 'honky_tonk_piano', 4: 'electric_piano_1', 5: 'electric_piano_2', 6: 'harpsichord', 7: 'clavi', 8: 'celesta', 9: 'glockenspiel', 10: 'music_box', 11: 'vibraphone', 12: 'marimba', 13: 'xylophone', 14: 'tubular_bells', 15: 'dulcimer', 16: 'drawbar_organ', 17: 'percussive_organ', 18: 'rock_organ', 19: 'church_organ', 20: 'reed_organ', 21: 'accordion', 22: 'harmonica', 23: 'tango_accordion', 24: 'acoustic_guitar_nylon', 25: 'acoustic_guitar_steel', 26: 'electric_guitar_jazz', 27: 'electric_guitar_clean', 28: 'electric_guitar_muted', 29: 'overdriven_guitar', 30: 'distortion_guitar', 31: 'guitar_harmonics', 32: 'acoustic_bass', 33: 'electric_bass_finger', 34: 'electric_bass_pick', 35: 'fretless_bass', 36: 'slap_bass_1', 37: 'slap_bass_2', 38: 'synth_bass_1', 39: 'synth_bass_2', 40: 'violin', 41: 'viola', 42: 'cello', 43: 'contrabass', 44: 'tremolo_strings', 45: 'pizzicato_strings', 46: 'orchestral_harp', 47: 'timpani', 48: 'string_ensemble_1', 49: 'string_ensemble_2', 50: 'synth_strings_1', 51: 'synth_strings_2', 52: 'choir_aahs', 53: 'voice_oohs', 54: 'synth_voice', 55: 'orchestra_hit', 56: 'trumpet', 57: 'trombone', 58: 'tuba', 59: 'muted_trumpet', 60: 'french_horn', 61: 'brass_section', 62: 'synth_brass_1', 63: 'synth_brass_2', 64: 'soprano_sax', 65: 'alto_sax', 66: 'tenor_sax', 67: 'baritone_sax', 68: 'oboe', 69: 'english_horn', 70: 'bassoon', 71: 'clarinet', 72: 'piccolo', 73: 'flute', 74: 'recorder', 75: 'pan_flute', 76: 'blown_bottle', 77: 'shakuhachi', 78: 'whistle', 79: 'ocarina', 80: 'lead_1_square', 81: 'lead_2_sawtooth', 82: 'lead_3_calliope', 83: 'lead_4_chiff', 84: 'lead_5_charang', 85: 'lead_6_voice', 86: 'lead_7_fifths', 87: 'lead_8_bass__lead', 88: 'pad_1_new_age', 89: 'pad_2_warm', 90: 'pad_3_polysynth', 91: 'pad_4_choir', 92: 'pad_5_bowed', 93: 'pad_6_metallic', 94: 'pad_7_halo', 95: 'pad_8_sweep', 96: 'fx_1_rain', 97: 'fx_2_soundtrack', 98: 'fx_3_crystal', 99: 'fx_4_atmosphere', 100: 'fx_5_brightness', 101: 'fx_6_goblins', 102: 'fx_7_echoes', 103: 'fx_8_sci_fi', 104: 'sitar', 105: 'banjo', 106: 'shamisen', 107: 'koto', 108: 'kalimba', 109: 'bag_pipe', 110: 'fiddle', 111: 'shanai', 112: 'tinkle_bell', 113: 'agogo', 114: 'steel_drums', 115: 'woodblock', 116: 'taiko_drum', 117: 'melodic_tom', 118: 'synth_drum', 119: 'reverse_cymbal', 120: 'guitar_fret_noise', 121: 'breath_noise', 122: 'seashore', 123: 'bird_tweet', 124: 'telephone_ring', 125: 'helicopter', 126: 'applause', 127: 'gunshot', 128: 'drum_0', 129: 'drum_1', 130: 'drum_2', 131: 'drum_3', 132: 'drum_4', 133: 'drum_5', 134: 'drum_6', 135: 'drum_7', 136: 'drum_8', 137: 'drum_9', 138: 'drum_10', 139: 'drum_11', 140: 'drum_12', 141: 'drum_13', 142: 'drum_14', 143: 'drum_15', 144: 'drum_16', 145: 'drum_17', 146: 'drum_18', 147: 'drum_19', 148: 'drum_20', 149: 'drum_21', 150: 'drum_22', 151: 'drum_23', 152: 'drum_24', 153: 'drum_25', 154: 'drum_26', 155: 'drum_27', 156: 'drum_28', 157: 'drum_29', 158: 'drum_30', 159: 'drum_31', 160: 'drum_32', 161: 'drum_33', 162: 'drum_34', 163: 'drum_35', 164: 'drum_36', 165: 'drum_37', 166: 'drum_38', 167: 'drum_39', 168: 'drum_40', 169: 'drum_41', 170: 'drum_42', 171: 'drum_43', 172: 'drum_44', 173: 'drum_45', 174: 'drum_46', 175: 'drum_47', 176: 'drum_48', 177: 'drum_49', 178: 'drum_50', 179: 'drum_51', 180: 'drum_52', 181: 'drum_53', 182: 'drum_54', 183: 'drum_55', 184: 'drum_56', 185: 'drum_57', 186: 'drum_58', 187: 'drum_59', 188: 'drum_60', 189: 'drum_61', 190: 'drum_62', 191: 'drum_63', 192: 'drum_64', 193: 'drum_65', 194: 'drum_66', 195: 'drum_67', 196: 'drum_68', 197: 'drum_69', 198: 'drum_70', 199: 'drum_71', 200: 'drum_72', 201: 'drum_73', 202: 'drum_74', 203: 'drum_75', 204: 'drum_76', 205: 'drum_77', 206: 'drum_78', 207: 'drum_79', 208: 'drum_80', 209: 'drum_81', 210: 'drum_82', 211: 'drum_83', 212: 'drum_84', 213: 'drum_85', 214: 'drum_86', 215: 'drum_87', 216: 'drum_88', 217: 'drum_89', 218: 'drum_90', 219: 'drum_91', 220: 'drum_92', 221: 'drum_93', 222: 'drum_94', 223: 'drum_95', 224: 'drum_96', 225: 'drum_97', 226: 'drum_98', 227: 'drum_99', 228: 'drum_100', 229: 'drum_101', 230: 'drum_102', 231: 'drum_103', 232: 'drum_104', 233: 'drum_105', 234: 'drum_106', 235: 'drum_107', 236: 'drum_108', 237: 'drum_109', 238: 'drum_110', 239: 'drum_111', 240: 'drum_112', 241: 'drum_113', 242: 'drum_114', 243: 'drum_115', 244: 'drum_116', 245: 'drum_117', 246: 'drum_118', 247: 'drum_119', 248: 'drum_120', 249: 'drum_121', 250: 'drum_122', 251: 'drum_123', 252: 'drum_124', 253: 'drum_125', 254: 'drum_126', 255: 'drum_127'}
POLY_LEVELS = ["any", "one", "two", "three", "four", "five", "six"]
DUR_LEVELS = ["any", "thirty_second", "sixteenth", "eighth", "quarter", "half", "whole"]
CURRENT_NUM_BARS = 16

BUCKET_NAME = 'mmmft'
MIDI_JSON_FILENAME = 'current_midi.json'

class MMM:
    def __init__(self, hash: str):
        self.hash = hash
        # with open('./js/demo.js', 'r') as f:
        #     self.js = Javascript(f.read())
        # display(self.js)

        # if isInit:
        #     self.reset_midi()
            # eval_js("start_up()")

    def get_current_midi(self):
        # TODO: Get current_midi.json from S3
        with open(MIDI_JSON_FILENAME, "r") as f:
            return json.load(f)

    def save_current_midi(self, midi_json, is_generate: bool = False):
        # TODO: Save .mid and .wav to S3
        with open(MIDI_JSON_FILENAME, "w") as f:
            json.dump(midi_json, f)
        sess = Session()
        s3 = sess.client('s3')
        s3.upload_file(f'/{self.hash}/{MIDI_JSON_FILENAME}', BUCKET_NAME, MIDI_JSON_FILENAME)

        if is_generate:
            pass

    def generate_callback(self, instruments: List[str]):
        status = self.get_status(instruments=instruments)
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


    # def add_new_track(self):
    #     eval_js("add_track()")

    def get_status(self, instruments: List[str]):
        status = {"tracks" : []}
        for i, inst in enumerate(instruments):
            status["tracks"].append({
                "track_id" : i,
                "instrument" : inst,
                "instrument_num" : INST_MAP[inst],
                "density" : 0,
                "track_type" : 11 if 'drum_' in inst else 10,
                "mute" : False,
                "solo" : False,
                "ignore" : False,
                "resample" : True,
                "selected_bars" : self.get_highlighted_bars(),
                "min_polyphony_q" : "POLYPHONY_" + POLY_LEVELS[0].upper(),
                "max_polyphony_q" : "POLYPHONY_" + POLY_LEVELS[0].upper(),
                "min_note_duration_q" : "DURATION_" + DUR_LEVELS[0].upper(),
                "max_note_duration_q" : "DURATION_" + DUR_LEVELS[0].upper()
            })

        status["temperature"] = 1
        status["canGenerate"] = True
        status["canListen"] = True
        status["tempo"] = 120
        status["nbars"] = CURRENT_NUM_BARS

        status["tracks_per_step"] = 1
        status["bars_per_step"] = 2
        status["shuffle"] = True
        status["percentage"] = 100
        status["model_dim"] = 4

        return status

    def get_highlighted_bars(self):
        highlighted_bars = []
        for i in range(CURRENT_NUM_BARS):
            highlighted_bars.append(True)
        return highlighted_bars
