// http://www.sfu.ca/~jeffe/MMM/DEMO/v2/demo.html

  var INST_MAP = {'acoustic_grand_piano': 0, 'bright_acoustic_piano': 1, 'electric_grand_piano': 2, 'honky_tonk_piano': 3, 'electric_piano_1': 4, 'electric_piano_2': 5, 'harpsichord': 6, 'clavi': 7, 'celesta': 8, 'glockenspiel': 9, 'music_box': 10, 'vibraphone': 11, 'marimba': 12, 'xylophone': 13, 'tubular_bells': 14, 'dulcimer': 15, 'drawbar_organ': 16, 'percussive_organ': 17, 'rock_organ': 18, 'church_organ': 19, 'reed_organ': 20, 'accordion': 21, 'harmonica': 22, 'tango_accordion': 23, 'acoustic_guitar_nylon': 24, 'acoustic_guitar_steel': 25, 'electric_guitar_jazz': 26, 'electric_guitar_clean': 27, 'electric_guitar_muted': 28, 'overdriven_guitar': 29, 'distortion_guitar': 30, 'guitar_harmonics': 31, 'acoustic_bass': 32, 'electric_bass_finger': 33, 'electric_bass_pick': 34, 'fretless_bass': 35, 'slap_bass_1': 36, 'slap_bass_2': 37, 'synth_bass_1': 38, 'synth_bass_2': 39, 'violin': 40, 'viola': 41, 'cello': 42, 'contrabass': 43, 'tremolo_strings': 44, 'pizzicato_strings': 45, 'orchestral_harp': 46, 'timpani': 47, 'string_ensemble_1': 48, 'string_ensemble_2': 49, 'synth_strings_1': 50, 'synth_strings_2': 51, 'choir_aahs': 52, 'voice_oohs': 53, 'synth_voice': 54, 'orchestra_hit': 55, 'trumpet': 56, 'trombone': 57, 'tuba': 58, 'muted_trumpet': 59, 'french_horn': 60, 'brass_section': 61, 'synth_brass_1': 62, 'synth_brass_2': 63, 'soprano_sax': 64, 'alto_sax': 65, 'tenor_sax': 66, 'baritone_sax': 67, 'oboe': 68, 'english_horn': 69, 'bassoon': 70, 'clarinet': 71, 'piccolo': 72, 'flute': 73, 'recorder': 74, 'pan_flute': 75, 'blown_bottle': 76, 'shakuhachi': 77, 'whistle': 78, 'ocarina': 79, 'lead_1_square': 80, 'lead_2_sawtooth': 81, 'lead_3_calliope': 82, 'lead_4_chiff': 83, 'lead_5_charang': 84, 'lead_6_voice': 85, 'lead_7_fifths': 86, 'lead_8_bass__lead': 87, 'pad_1_new_age': 88, 'pad_2_warm': 89, 'pad_3_polysynth': 90, 'pad_4_choir': 91, 'pad_5_bowed': 92, 'pad_6_metallic': 93, 'pad_7_halo': 94, 'pad_8_sweep': 95, 'fx_1_rain': 96, 'fx_2_soundtrack': 97, 'fx_3_crystal': 98, 'fx_4_atmosphere': 99, 'fx_5_brightness': 100, 'fx_6_goblins': 101, 'fx_7_echoes': 102, 'fx_8_sci_fi': 103, 'sitar': 104, 'banjo': 105, 'shamisen': 106, 'koto': 107, 'kalimba': 108, 'bag_pipe': 109, 'fiddle': 110, 'shanai': 111, 'tinkle_bell': 112, 'agogo': 113, 'steel_drums': 114, 'woodblock': 115, 'taiko_drum': 116, 'melodic_tom': 117, 'synth_drum': 118, 'reverse_cymbal': 119, 'guitar_fret_noise': 120, 'breath_noise': 121, 'seashore': 122, 'bird_tweet': 123, 'telephone_ring': 124, 'helicopter': 125, 'applause': 126, 'gunshot': 127, 'drum_0': 0, 'drum_1': 1, 'drum_2': 2, 'drum_3': 3, 'drum_4': 4, 'drum_5': 5, 'drum_6': 6, 'drum_7': 7, 'drum_8': 8, 'drum_9': 9, 'drum_10': 10, 'drum_11': 11, 'drum_12': 12, 'drum_13': 13, 'drum_14': 14, 'drum_15': 15, 'drum_16': 16, 'drum_17': 17, 'drum_18': 18, 'drum_19': 19, 'drum_20': 20, 'drum_21': 21, 'drum_22': 22, 'drum_23': 23, 'drum_24': 24, 'drum_25': 25, 'drum_26': 26, 'drum_27': 27, 'drum_28': 28, 'drum_29': 29, 'drum_30': 30, 'drum_31': 31, 'drum_32': 32, 'drum_33': 33, 'drum_34': 34, 'drum_35': 35, 'drum_36': 36, 'drum_37': 37, 'drum_38': 38, 'drum_39': 39, 'drum_40': 40, 'drum_41': 41, 'drum_42': 42, 'drum_43': 43, 'drum_44': 44, 'drum_45': 45, 'drum_46': 46, 'drum_47': 47, 'drum_48': 48, 'drum_49': 49, 'drum_50': 50, 'drum_51': 51, 'drum_52': 52, 'drum_53': 53, 'drum_54': 54, 'drum_55': 55, 'drum_56': 56, 'drum_57': 57, 'drum_58': 58, 'drum_59': 59, 'drum_60': 60, 'drum_61': 61, 'drum_62': 62, 'drum_63': 63, 'drum_64': 64, 'drum_65': 65, 'drum_66': 66, 'drum_67': 67, 'drum_68': 68, 'drum_69': 69, 'drum_70': 70, 'drum_71': 71, 'drum_72': 72, 'drum_73': 73, 'drum_74': 74, 'drum_75': 75, 'drum_76': 76, 'drum_77': 77, 'drum_78': 78, 'drum_79': 79, 'drum_80': 80, 'drum_81': 81, 'drum_82': 82, 'drum_83': 83, 'drum_84': 84, 'drum_85': 85, 'drum_86': 86, 'drum_87': 87, 'drum_88': 88, 'drum_89': 89, 'drum_90': 90, 'drum_91': 91, 'drum_92': 92, 'drum_93': 93, 'drum_94': 94, 'drum_95': 95, 'drum_96': 96, 'drum_97': 97, 'drum_98': 98, 'drum_99': 99, 'drum_100': 100, 'drum_101': 101, 'drum_102': 102, 'drum_103': 103, 'drum_104': 104, 'drum_105': 105, 'drum_106': 106, 'drum_107': 107, 'drum_108': 108, 'drum_109': 109, 'drum_110': 110, 'drum_111': 111, 'drum_112': 112, 'drum_113': 113, 'drum_114': 114, 'drum_115': 115, 'drum_116': 116, 'drum_117': 117, 'drum_118': 118, 'drum_119': 119, 'drum_120': 120, 'drum_121': 121, 'drum_122': 122, 'drum_123': 123, 'drum_124': 124, 'drum_125': 125, 'drum_126': 126, 'drum_127': 127};

  var REV_INST_MAP = {0: 'acoustic_grand_piano', 1: 'bright_acoustic_piano', 2: 'electric_grand_piano', 3: 'honky_tonk_piano', 4: 'electric_piano_1', 5: 'electric_piano_2', 6: 'harpsichord', 7: 'clavi', 8: 'celesta', 9: 'glockenspiel', 10: 'music_box', 11: 'vibraphone', 12: 'marimba', 13: 'xylophone', 14: 'tubular_bells', 15: 'dulcimer', 16: 'drawbar_organ', 17: 'percussive_organ', 18: 'rock_organ', 19: 'church_organ', 20: 'reed_organ', 21: 'accordion', 22: 'harmonica', 23: 'tango_accordion', 24: 'acoustic_guitar_nylon', 25: 'acoustic_guitar_steel', 26: 'electric_guitar_jazz', 27: 'electric_guitar_clean', 28: 'electric_guitar_muted', 29: 'overdriven_guitar', 30: 'distortion_guitar', 31: 'guitar_harmonics', 32: 'acoustic_bass', 33: 'electric_bass_finger', 34: 'electric_bass_pick', 35: 'fretless_bass', 36: 'slap_bass_1', 37: 'slap_bass_2', 38: 'synth_bass_1', 39: 'synth_bass_2', 40: 'violin', 41: 'viola', 42: 'cello', 43: 'contrabass', 44: 'tremolo_strings', 45: 'pizzicato_strings', 46: 'orchestral_harp', 47: 'timpani', 48: 'string_ensemble_1', 49: 'string_ensemble_2', 50: 'synth_strings_1', 51: 'synth_strings_2', 52: 'choir_aahs', 53: 'voice_oohs', 54: 'synth_voice', 55: 'orchestra_hit', 56: 'trumpet', 57: 'trombone', 58: 'tuba', 59: 'muted_trumpet', 60: 'french_horn', 61: 'brass_section', 62: 'synth_brass_1', 63: 'synth_brass_2', 64: 'soprano_sax', 65: 'alto_sax', 66: 'tenor_sax', 67: 'baritone_sax', 68: 'oboe', 69: 'english_horn', 70: 'bassoon', 71: 'clarinet', 72: 'piccolo', 73: 'flute', 74: 'recorder', 75: 'pan_flute', 76: 'blown_bottle', 77: 'shakuhachi', 78: 'whistle', 79: 'ocarina', 80: 'lead_1_square', 81: 'lead_2_sawtooth', 82: 'lead_3_calliope', 83: 'lead_4_chiff', 84: 'lead_5_charang', 85: 'lead_6_voice', 86: 'lead_7_fifths', 87: 'lead_8_bass__lead', 88: 'pad_1_new_age', 89: 'pad_2_warm', 90: 'pad_3_polysynth', 91: 'pad_4_choir', 92: 'pad_5_bowed', 93: 'pad_6_metallic', 94: 'pad_7_halo', 95: 'pad_8_sweep', 96: 'fx_1_rain', 97: 'fx_2_soundtrack', 98: 'fx_3_crystal', 99: 'fx_4_atmosphere', 100: 'fx_5_brightness', 101: 'fx_6_goblins', 102: 'fx_7_echoes', 103: 'fx_8_sci_fi', 104: 'sitar', 105: 'banjo', 106: 'shamisen', 107: 'koto', 108: 'kalimba', 109: 'bag_pipe', 110: 'fiddle', 111: 'shanai', 112: 'tinkle_bell', 113: 'agogo', 114: 'steel_drums', 115: 'woodblock', 116: 'taiko_drum', 117: 'melodic_tom', 118: 'synth_drum', 119: 'reverse_cymbal', 120: 'guitar_fret_noise', 121: 'breath_noise', 122: 'seashore', 123: 'bird_tweet', 124: 'telephone_ring', 125: 'helicopter', 126: 'applause', 127: 'gunshot', 128: 'drum_0', 129: 'drum_1', 130: 'drum_2', 131: 'drum_3', 132: 'drum_4', 133: 'drum_5', 134: 'drum_6', 135: 'drum_7', 136: 'drum_8', 137: 'drum_9', 138: 'drum_10', 139: 'drum_11', 140: 'drum_12', 141: 'drum_13', 142: 'drum_14', 143: 'drum_15', 144: 'drum_16', 145: 'drum_17', 146: 'drum_18', 147: 'drum_19', 148: 'drum_20', 149: 'drum_21', 150: 'drum_22', 151: 'drum_23', 152: 'drum_24', 153: 'drum_25', 154: 'drum_26', 155: 'drum_27', 156: 'drum_28', 157: 'drum_29', 158: 'drum_30', 159: 'drum_31', 160: 'drum_32', 161: 'drum_33', 162: 'drum_34', 163: 'drum_35', 164: 'drum_36', 165: 'drum_37', 166: 'drum_38', 167: 'drum_39', 168: 'drum_40', 169: 'drum_41', 170: 'drum_42', 171: 'drum_43', 172: 'drum_44', 173: 'drum_45', 174: 'drum_46', 175: 'drum_47', 176: 'drum_48', 177: 'drum_49', 178: 'drum_50', 179: 'drum_51', 180: 'drum_52', 181: 'drum_53', 182: 'drum_54', 183: 'drum_55', 184: 'drum_56', 185: 'drum_57', 186: 'drum_58', 187: 'drum_59', 188: 'drum_60', 189: 'drum_61', 190: 'drum_62', 191: 'drum_63', 192: 'drum_64', 193: 'drum_65', 194: 'drum_66', 195: 'drum_67', 196: 'drum_68', 197: 'drum_69', 198: 'drum_70', 199: 'drum_71', 200: 'drum_72', 201: 'drum_73', 202: 'drum_74', 203: 'drum_75', 204: 'drum_76', 205: 'drum_77', 206: 'drum_78', 207: 'drum_79', 208: 'drum_80', 209: 'drum_81', 210: 'drum_82', 211: 'drum_83', 212: 'drum_84', 213: 'drum_85', 214: 'drum_86', 215: 'drum_87', 216: 'drum_88', 217: 'drum_89', 218: 'drum_90', 219: 'drum_91', 220: 'drum_92', 221: 'drum_93', 222: 'drum_94', 223: 'drum_95', 224: 'drum_96', 225: 'drum_97', 226: 'drum_98', 227: 'drum_99', 228: 'drum_100', 229: 'drum_101', 230: 'drum_102', 231: 'drum_103', 232: 'drum_104', 233: 'drum_105', 234: 'drum_106', 235: 'drum_107', 236: 'drum_108', 237: 'drum_109', 238: 'drum_110', 239: 'drum_111', 240: 'drum_112', 241: 'drum_113', 242: 'drum_114', 243: 'drum_115', 244: 'drum_116', 245: 'drum_117', 246: 'drum_118', 247: 'drum_119', 248: 'drum_120', 249: 'drum_121', 250: 'drum_122', 251: 'drum_123', 252: 'drum_124', 253: 'drum_125', 254: 'drum_126', 255: 'drum_127'};

  const POLY_LEVELS = ["any", "one", "two", "three", "four", "five", "six"];
  const DUR_LEVELS = ["any", "thirty_second", "sixteenth", "eighth", "quarter", "half", "whole"];

  var HYPERPARAM_OPEN = false;
  var SNACKBAR = null;
  var HIGHLIGHT_OPACITY = .2;
  var CURRENT_NUM_BARS = 16;
  var TRACK_COUNT = 0;
  var GOOGLE_COLAB =  (typeof google !== "undefined") && (typeof google.colab !== "undefined");

  const BarLayerEnum = Object.freeze(
    {"SELECT":0, "IGNORE":1, "CONTEXT":2, "PROGRESS":3, "GENERATED":4});
  const BarLayerLabelEnum = Object.freeze(
    {0:"SELECT", 1:"IGNORE", 2:"CONTEXT", 3:"PROGRESS", 4:"GENERATED"});

  // function that takes state to color
  // and we have enum for different states
  const BarStateEnum = Object.freeze({"NONE":0, "HIGHLIGHT":1, "IGNORE":2, "GENERATED":3,"LOCKED":4});

  function any(iterable) {
    for (var index = 0; index < iterable.length; index++) {
      if (iterable[index]) return true;
    }
    return false;
  }
  function all(iterable) {
    for (var index = 0; index < iterable.length; index++) {
      if (!iterable[index]) return false;
    }
    return true;
  }

  function build_tooltip(tooltip_text, id, parent, right=false) {
    var tool = document.createElement("DIV");
    tool.setAttribute("data-mdl-for", id);
    if (right) {
      tool.className = "mdl-tooltip mdl-tooltip--right";
    }
    else {
      tool.className = "mdl-tooltip";
    }
    tool.textContent = tooltip_text;
    parent.appendChild(tool);
  }

  function build_snackbar(message) {
    SNACKBAR.labelText = message;
    SNACKBAR.open(); 
  }

  /////////////////////////////////////////////////////////////////////////
  /////////////////////////////////////////////////////////////////////////
  /// MIDI RENDERING

  function get_notes(midi_json, track_num) {
    // we can assume that the midi_json is well formed here
    var notes = [];
    var onsets = {};

    var track = midi_json["tracks"][track_num];
    if ("bars" in track) {
      var bar_start = 0;
      var bars = track["bars"];
      for (var i=0; i<bars.length; i++) {
        if ("events" in bars[i]) {
          var events = bars[i]["events"];
          for (var j=0; j<events.length; j++) {
            var event = midi_json["events"][events[j]];
            if (event["velocity"] > 0) {
              onsets[event["pitch"]] = {"time" : bar_start + event["time"]};
              //onsets[event["pitch"]]["time"] += bar_start;
            }
            else if(event["pitch"] in onsets) {
              notes.push({
                "start" : onsets[event["pitch"]]["time"],
                "end" : bar_start + event["time"],
                "pitch" : event["pitch"],
              });
              delete onsets[event["pitch"]];
            }
          }
        }
        bar_start += bars[i]["internalBeatLength"] * 12; // resolution
      }
    }
    // handle remaining notes
    for (var key in onsets) {
      notes.push({
        "start" : onsets[key]["time"],
        "end" : 192,
        "pitch" : onsets[key]["pitch"],
      });
    }
    return notes;
  }
  
  function build_svg_rect(x, y, width, height, fill="none", stroke="none", stroke_width=0) {
    var r = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    r.style.x = x.toString() + "%";
    r.style.y = y.toString() + "%";
    r.style.width = width.toString() + "%";
    r.style.height = height.toString() + "%";
    r.style.fill = fill;
    r.style.stroke = stroke;
    r.style.strokeWidth = stroke_width;
    return r;
  }
  
  function update_color(bar) {
    var state = bar.style.state;
    if (state == BarStateEnum.NONE) {
      bar.style.fill = "rgba(0,0,0,0)";
    }
    else if (state == BarStateEnum.HIGHLIGHT) {
      bar.style.fill = "rgba(0,0,255,.3)";
    }
    else if (state == BarStateEnum.LOCKED) {
      bar.style.fill = "rgba(0,0,255,.3)";
    }
    else if (state == BarStateEnum.IGNORE) {
      bar.style.fill = "rgba(255,0,0,.3)";
    }
    else if (state == BarStateEnum.GENERATED) {
      bar.style.fill = "rgba(0,255,0,.3)";
    }
    update_color_switches(bar);
  }

  function get_track_ids() {
    var track_ids = [];
    var tracks = $(".track");
    for (var i=0; i<tracks.length; i++) {
      track_ids.push( tracks[i].id.split("_")[1] );
    }
    return track_ids;
  }

  function clear_selection() {
    var track_ids = get_track_ids();
    track_ids.forEach(function (item, index) {
      for (var i=0; i<CURRENT_NUM_BARS; i++) {
        var b = get_bar(item,i)[0];
        b.style.state = 0;
        update_color(b);
      }
    });
  }

  function update_color_switches(bar) {
    var all_highlighted = true;
    var all_ignored = true;
    for (var i=0; i<CURRENT_NUM_BARS; i++) {
      var state = get_bar(bar.track_id,i)[0].style.state;
      all_highlighted &= (state == BarStateEnum.HIGHLIGHT);
      all_ignored &= (state == BarStateEnum.IGNORE);
    }
    // now using this button to control something else
    //set_switch(bar.track_id, "resample", all_highlighted);
    set_switch(bar.track_id, "ignore", all_ignored);
  }
  
  function flip_opacity(x) {
    if ((x.style.state != BarStateEnum.IGNORE) && (x.style.state != BarStateEnum.LOCKED)) {
      x.style.state = 1 - (x.style.state > 0);
      update_color(x);
    }
  }

  function get_bar(track, bar) {
    return $("#highlight_track_" + track.toString() + "_bar_" + bar.toString());
  }

  function set_bar(track, bar, state, override_ignore) {
    var b = get_bar(track, bar)[0];
    if (((b.style.state != BarStateEnum.IGNORE) && (b.style.state != BarStateEnum.LOCKED)) || (override_ignore)) {
      b.style.state = state;
      update_color(b);
    }
  }

  // resample LOCKS all bars
  // 

  function set_bars(tracks, bars, state) {
    for (var i=0; i<tracks.length; i++) {
      set_bar(tracks[i].toString(), bars[i].toString(), state, false);
    }
  }

  // might not need this anymore
  function get_highlighted_bars(track_id) {
    var highlighted_bars = [];
    for (var i=0; i<CURRENT_NUM_BARS; i++) {
      var bar = get_bar(track_id,i)[0];
      highlighted_bars.push( 
        (bar.style.state == BarStateEnum.HIGHLIGHT) || (bar.style.state == BarStateEnum.LOCKED) );
    }
    return highlighted_bars;
  }


  function get_bar_layer_id(track_num, bar_num, layer) {
    return BarLayerLabelEnum[layer] + "_" + track_num.toString() + "_bar_" + bar_num.toString();
  }

  function get_bar_layer(track_num, bar_num, layer) {
    var id = get_bar_layer_id(track_num, bar_num, layer);
    return $("#" + id)[0];
  }

  function set_bar_layer(track_num, bar_num, layer, state) {
    var b = get_bar_layer(track_num, bar_num, layer);
    b.style.state = state;
    if (state == 1) {
      if (layer == BarLayerEnum.SELECT) {
        b.style.fill = "rgba(0,0,255,.3)";
      }
      else if (layer == BarLayerEnum.CONTEXT) {
        b.style.fill = "rgba(255,0,255,.3)";
      }
      else if (layer == BarLayerEnum.IGNORE) {
        b.style.fill = "rgba(255,0,0,.3)";
      }
      else if (layer == BarLayerEnum.GENERATED) {
        b.style.fill = "rgba(0,255,0,.3)";
      }
      else if (layer == BarLayerEnum.PROGRESS) {
        b.style.fill = "rgba(255,255,0,.3)";
      }
    }
    else {
      b.style.fill = "rgba(0,0,0,0)";
    }
  }

  function set_all_layer_bars(x,clear) {
    if (clear) {
      clear_selection();
    }
    for (var i=0; i<x.length; i++) {
      set_bar_layer(x[i][0], x[i][1], x[i][2], x[i][3]);
    }
  }

  function build_bar(track, i, bar_width, layer) {
    var b = build_svg_rect(i*bar_width, 0, bar_width, 100, "rgba(0,0,0,0)");
    b.style.state = 0;
    b.id = get_bar_layer_id(track, i, layer);
    b.track_id = track;
    return b;
  }
  
  function build_pianoroll(midi_json, track_num) {
    // build piano roll should accept an actual track from the representation

    if (typeof midi_json === 'undefined') {
      notes = []
    }
    else {
      notes = get_notes(midi_json, track_num);
      CURRENT_NUM_BARS = midi_json["tracks"][track_num]["bars"].length;
    }

    nbars = CURRENT_NUM_BARS;
    var nbeats = 4;
    
    var resolution = 12;
    var max_notes = 128;
    var xticks = resolution * nbeats * nbars;
    var beat_width = 100. / (8 * nbars); // eighth note width
    var beat_color = "#9E9E9E";
    
    var bar_width = 100. / nbars; // bar width
    var bar_colors = ["#A9A9A9", "#B4B4B4"];
    var small = 1. / xticks / 4; // quarter of a tick width
  
    var x = document.createElement("DIV");
    var s = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  
    s.style.width = "100%";
    s.style.height = "190px";
    s.viewBox = "0 0 100 100";
    s.preserveAspectRatio = "none";
  
    // make the bars
    for (i=0; i<nbars; i++) {
      s.appendChild(build_svg_rect(i*bar_width, 0, bar_width, 100, bar_colors[i%2]));
    }
  
    // make the beats
    for (i=0; i<(8*nbars); i++) {
      s.appendChild(build_svg_rect(i*beat_width, 0, beat_width, 100, "none", beat_color, .15));
    }
  
    // draw the notes
    for (i=0; i<notes.length; i++) {
      note = notes[i];
      var y = 100 - (note["pitch"] / max_notes * 100);
      var x = note["start"] / xticks  * 100;
      var w = (((note["end"] - note["start"]) / xticks) - small) * 100;
      var h = 1. / max_notes * 100;
      s.appendChild(build_svg_rect(x,y,w,h,"red"));
    }
    
    // make the bar highlights
    // build a tooltip for the bars ?
    for (i=0; i<nbars; i++) {

      s.append( build_bar(track_num, i, bar_width, BarLayerEnum.CONTEXT) );
      s.append( build_bar(track_num, i, bar_width, BarLayerEnum.PROGRESS) );
      s.append( build_bar(track_num, i, bar_width, BarLayerEnum.GENERATED) );
      s.append( build_bar(track_num, i, bar_width, BarLayerEnum.IGNORE) );
      s.append( build_bar(track_num, i, bar_width, BarLayerEnum.SELECT) );

      var b = build_svg_rect(i*bar_width, 0, bar_width, 100, "rgba(0,0,0,0)");
      //b.style.opacity = 0;
      b.style.state = 0;
      b.onclick = function() { flip_opacity(this); };
      b.id = "highlight_track_" + track_num.toString() + "_bar_" + i.toString();
      b.track_id = track_num;
      s.appendChild(b);

      
    }
  
    return s;
  }  

  //////////////////////////////////////////////////////////////////////////

  function get_switch(track_id, name) {
    return $("#" + name + "_" + track_id + "-so")[0]
  }

  function switch_on(track_id, name) {
    return get_switch(track_id,name).MDCSwitch.checked;
  }

  function set_switch(track_id, name, state) {
    get_switch(track_id,name).MDCSwitch.checked = state;
  }

  var createMuteHandler = function(track_id) {
    return function() {
      if (get_switch(track_id,"mute").MDCSwitch.checked) {
        set_switch(track_id, "solo", false);
      }
    };
  }

  var createSoloHandler = function(track_id) {
    return function() {
      if (get_switch(track_id,"solo").MDCSwitch.checked) {
        set_switch(track_id, "mute", false);
      }
    };
  }

  var createRemoveHandler = function(track_id) {
    return function() {
      $("#track_" + track_id).remove();
    }
  }

  var createMoveUpHandler = function(track_id) {
    return function() {
      var a = $("#track_" + track_id);
      var b = a.prev();
      if (b) {
        a.after(b);
      }
    }
  }

  var createMoveDownHandler = function(track_id) {
    return function() {
      var a = $("#track_" + track_id);
      var b = a.next();
      if (b) {
        a.before(b);
      }
    }
  }

  var createResampleHandler = function(track_id) {
    return function() {
      var state = BarStateEnum.NONE;
      if (switch_on(track_id, "resample")) {
        state = BarStateEnum.LOCKED;
        set_switch(track_id, "ignore", false);
      }
      for (var i=0; i<CURRENT_NUM_BARS; i++) {
        set_bar(track_id, i, state, true);
      }
    }
  }

  var createIgnoreHandler = function(track_id) {
    return function() {
      var state = BarStateEnum.NONE;
      if (switch_on(track_id, "ignore")) {
        state = BarStateEnum.IGNORE;
        set_switch(track_id, "resample", false);
      }
      for (var i=0; i<CURRENT_NUM_BARS; i++) {
        set_bar(track_id, i, state, true);
      }
    }
  }

  var createDensitySwitchHandler = function(track_id) {
    return function() {
      $("#density-slider_" + track_id + "-slo")[0].MDCSlider.disabled = !$("#density_" + track_id + "-so")[0].MDCSwitch.checked;
    }
  }
  
  function load_template(n, parent, id, elem_selector) {
    var tmp = document.getElementsByTagName("template")[n];
    var node = tmp.content.cloneNode(true);
    parent.append(node);
    var elem = parent.find(elem_selector);
    elem.attr("id", id);
    return elem;
  }

  function build_switch(parent, id) {
    id = id + "-so"
    load_template(0, parent, id, "div:first");     
  }

  function build_sym_button(parent, id, button_text) {
    id = id + "-button"
    var elem = load_template(1, parent, id, "button:first");
    elem.text(button_text);
  }

  function build_slider(parent, id, num_steps) {
    id = id + "-slo"
    elem = load_template(5, parent, id, "div:first");
    elem.attr("aria-valuemax", num_steps-1);
  }

  function build_menu(parent, name, menu_items, small_menu=false) {
    id = name + "-mo"
    el = load_template(3, parent, id, "div:first");
    if (small_menu) {
      el.removeClass("inst-select");
      el.addClass("poly-select");
    }
    el.find('.mdc-floating-label').text(name);
    for (var i=0; i<menu_items.length; i++) {
      // this could probably be cleaned up
      var tmp = document.getElementsByTagName("template")[2];
      var node = tmp.content.cloneNode(true);
      $(".mdc-list", parent).append(node);
      var $el = $('.mdc-list li:last', parent);
      $el.find('.mdc-list-item__text').text(menu_items[i]);
      $el.attr("data-value", menu_items[i]);
    }
  }

  function update_mdc() {
    componentHandler.upgradeDom();
    // enable all switches
    [].map.call(document.querySelectorAll(".mdc-switch"), function(el) {
      el.MDCSwitch = new mdc.switchControl.MDCSwitch(el);
    });

    // enable all menus
    [].map.call(document.querySelectorAll(".mdc-select"), function(el) {
      el.MDCSelect = new mdc.select.MDCSelect(el);
    });

    // enable all sliders
    [].map.call(document.querySelectorAll(".mdc-slider"), function(el) {
      el.MDCSlider = new mdc.slider.MDCSlider(el);
    });
  }


  function build_track_controls(track_id) {

    //console.log($("#track_" + track_id).find("#solo-switch"));
    var track = $("#track_" + track_id);
    build_switch(track.find("#solo-switch"), "solo_" + track_id);
    build_switch(track.find("#mute-switch"), "mute_" + track_id);
    build_switch(track.find("#resample-switch"), "resample_" + track_id);
    build_switch(track.find("#ignore-switch"), "ignore_" + track_id);
    build_switch(track.find("#density-switch"), "density_" + track_id);

    build_slider(track.find("#density-slider"), "density-slider_" + track_id, 10);

    
    build_sym_button(
      track.find("#delete-button"), "delete_" + track_id, "remove_circle");
    build_sym_button(
      track.find("#down-button"), "down_" + track_id, "keyboard_arrow_down");
    build_sym_button(
      track.find("#up-button"), "up_" + track_id, "keyboard_arrow_up");

    menu_items = Object.values(REV_INST_MAP);
    build_menu(track.find("#inst-menu"), "inst_" + track_id, menu_items);

    // make menus for polyphony and note duration
    build_menu(track.find("#poly-min"),"poly_min_"+track_id, POLY_LEVELS, true);
    build_menu(track.find("#poly-max"),"poly_max_"+track_id, POLY_LEVELS, true);
    build_menu(track.find("#dur-min"), "dur_min_" + track_id, DUR_LEVELS, true);
    build_menu(track.find("#dur-max"), "dur_max_" + track_id, DUR_LEVELS, true);

    $("#delete_" + track_id + "-button").click(createRemoveHandler(track_id));
    $("#up_" + track_id + "-button").click(createMoveUpHandler(track_id));
    $("#down_" + track_id + "-button").click(createMoveDownHandler(track_id));
    $("#resample_" + track_id + "-so").click(createResampleHandler(track_id));
    $("#density_" + track_id + "-so").click(createDensitySwitchHandler(track_id));

    $("#ignore_" + track_id + "-so").click(createIgnoreHandler(track_id));
    $("#mute_" + track_id + "-so").click(createMuteHandler(track_id));
    $("#solo_" + track_id + "-so").click(createSoloHandler(track_id));

    var panel = track.find(".track-controls")[0];
    build_tooltip("Remove this track.", "delete_" + track_id + "-button", panel);
    build_tooltip("Move this track up.", "up_" + track_id + "-button", panel);
    build_tooltip("Move this track down.", "down_" + track_id + "-button", panel);
    build_tooltip("Mute this track.", "mute_" + track_id + "-so", panel);
    build_tooltip("Solo this track.", "solo_" + track_id + "-so", panel);
    build_tooltip("Select an instrument for generation.", "inst_" + track_id + "-mo", panel, true);
    build_tooltip("Control the note density for generation.", "density-slider" + track_id + "-slo", panel);
    build_tooltip("Autoregressively resample the entire track. Note that this will ignore all content on this track when generating.", "resample_" + track_id + "-so", panel);
    build_tooltip("Do not allow the model to condition generation on this track.", "ignore_" + track_id + "-so", panel);

  }

  function build_hyperparam_controls() {
    load_template(7, $("#hyper-container"), "hyperparam", "div.hyperparam-controls:first");
    var parent = $("#hyperparam");
    
    build_sym_button(parent.find("#close"), "close", "remove_circle");
    $("#close").click( close_hyperparam );
    
    //build_menu(parent.find("#param1-select"), "track_stride", [1,2,3,4,5,6]);
    //build_menu(parent.find("#param2-select"), "bar_stride", [1,2,3,4,5,6]);
    build_menu(parent.find("#param3-select"), "tracks_per_step", [1,2,3,4,5,6,7,8]);
    build_menu(parent.find("#param4-select"), "bars_per_step", [1,2,3,4,5,6,7,8]);
    build_switch(parent.find("#param6-select"), "shuffle");
    build_slider(parent.find("#param7-select"), "percentage", 101);
    build_menu(parent.find("#param8-select"), "temperature", [0.9, 0.95, 0.975, 0.99, 1., 1.01, 1.025, 1.05, 1.1]);
    build_menu(parent.find("#param9-select"), "model_size", [4, 8]);

    build_tooltip("The maximum number of tracks to generate each step. Selecting a larger value will increase variability of the generated output.", "tracks_per_step-mo", parent[0], true);
    build_tooltip("The maximum number of bars to generate each step. Selecting a larger value with increase variability of the generated output.", "bars_per_step-mo", parent[0], true);
    build_tooltip("When shuffle is enabled the order of generation steps is randomly shuffled. Note that this only applies to non-autoregressive tracks", "shuffle-so", parent[0], true);
    build_tooltip("The percentage of selected bars that are resampled. Note that this only applies to non-autoregressive tracks.", "percentage-slo", parent[0], true);
    build_tooltip("Set temperature for samping. Values higher than 1 increase entropy and values lower than 1 decrease entropy.", "temperature-mo", parent[0], true);
    build_tooltip("The number of bars the model can handle. A higher value will take more time, as each generation step takes more context into consideration, but will likely provide a better result.", "model_size-mo", parent[0], true);

    update_mdc();

    //$("#track_stride-mo")[0].MDCSelect.value = "2";
    //$("#bar_stride-mo")[0].MDCSelect.value = "2";
    $("#tracks_per_step-mo")[0].MDCSelect.value = "1";
    $("#bars_per_step-mo")[0].MDCSelect.value = "2";
    $("#shuffle-so")[0].MDCSwitch.checked = true;
    $("#percentage-slo")[0].MDCSlider.value = 100;
    $("#temperature-mo")[0].MDCSelect.value = "1";
    $("#model_size-mo")[0].MDCSelect.value = "4";

  }

  function build_track(midi_json) {
    //console.log(density);
    //console.log(TRACK_COUNT);
    var track_id = TRACK_COUNT.toString();
    load_template(6, $("#track-container"), "track_" + track_id, "div.track:last");
    build_track_controls(track_id);

    var s = build_pianoroll(midi_json, TRACK_COUNT);
    $("#track_" + track_id).find(".roll")[0].append(s);

    update_mdc();

    // set to default value
    var inst = "acoustic_grand_piano";
    var density = 5;
    var min_poly = "any";
    var max_poly = "any";
    var min_dur = "any";
    var max_dur = "any";

    if (typeof midi_json !== 'undefined') {
      var isDrum = (midi_json["tracks"][TRACK_COUNT]["trackType"]==11)||(midi_json["tracks"][TRACK_COUNT]["trackType"]=="STANDARD_DRUM_TRACK");
      var inst_number = midi_json["tracks"][TRACK_COUNT]["instrument"];
      inst = REV_INST_MAP[inst_number + 128*isDrum];

      var features = midi_json["tracks"][TRACK_COUNT]["internalFeatures"][0];
      console.log(features);
      density = features["noteDensityV2"];
      min_poly = POLY_LEVELS[ features["minPolyphonyQ"] + 1];
      max_poly = POLY_LEVELS[ features["maxPolyphonyQ"] + 1];
      min_dur = DUR_LEVELS[ features["minNoteDurationQ"] + 1];
      max_dur = DUR_LEVELS[ features["maxNoteDurationQ"] + 1];
    }
    console.log(min_poly, max_poly);
    $("#inst_" + track_id + "-mo")[0].MDCSelect.value = inst;
    $("#poly_min_" + track_id + "-mo")[0].MDCSelect.value = min_poly;
    $("#poly_max_" + track_id + "-mo")[0].MDCSelect.value = max_poly;
    $("#dur_min_" + track_id + "-mo")[0].MDCSelect.value = min_dur;
    $("#dur_max_" + track_id + "-mo")[0].MDCSelect.value = max_dur;
    $("#density-slider_" + track_id + "-slo")[0].MDCSlider.value = density;
    $("#density_" + track_id + "-so").trigger("click");

    if (typeof midi_json === 'undefined') {
      resample_button = $("#resample_" + track_id + "-so");
      resample_button[0].MDCSwitch.checked = true;
      resample_button.trigger("click");
    }

    TRACK_COUNT++;
  }

  function build_from_midi(midi_json) {
    clear_tracks(false);
    for (var i=0; i<midi_json["tracks"].length; i++) {
      build_track(midi_json);
    }
  }

  function check_overlap(l1x, l1y, l2x, l2y, r1x, r1y, r2x, r2y) {
    //console.log(l1x, l1y, l2x, l2y, r1x, r1y, r2x, r2y, (l1x >= r2x), (l2x >= r1x), (l1y <= r2y), (l2y <= r1y));
    if ((l1x >= r2x) || (l2x >= r1x)) {
      return false;
    }
    if ((l1y >= r2y) || (l2y >= r1y)) {
      return false;
    }
    return true;
  }

  MOUSEDOWN = false;
  DRAGX = 0;
  DRAGY = 0;
  SHIFTKEYON = false;
  LAST_MOVE = 0;

  function build_drag_select() {
    $("#track-container")
    .mousedown(function(e) {
      DRAGX = e.pageX;
      DRAGY = e.pageY;
      // only set mousedown if we are to the right of
      // track controls
      if (DRAGX > 350) {
        MOUSEDOWN = true;
        SHIFTKEYON = e.shiftKey;
      }
    })
    .mousemove(function(e) {
      if ((MOUSEDOWN) && (!HYPERPARAM_OPEN) && (Date.now() - LAST_MOVE > 40)) {
        // how can we make this called less frequently
        var sl = Math.min(DRAGX,e.pageX);
        var st = Math.min(DRAGY,e.pageY);
        var sr = Math.max(DRAGX,e.pageX);
        var sb = Math.max(DRAGY,e.pageY);

        var track_ids = get_track_ids();
        for (var i=0; i<track_ids.length; i++) {
          for (var j=0; j<CURRENT_NUM_BARS; j++) {
            var track_id = track_ids[i];
            var bar = get_bar(track_id,j);
            var offset = bar.offset();
            var overlaps = check_overlap(
              offset["left"], offset["top"], 
              sl, st, 
              offset["left"] + bar.width(), offset["top"] + bar.height(), 
              sr, sb);
            if (overlaps) {
              set_bar(track_id, j, BarStateEnum.HIGHLIGHT, false);
            }
            else if (!SHIFTKEYON) {
              set_bar(track_id, j, BarStateEnum.NONE, false);
            }
          }
        }
        LAST_MOVE = Date.now();
      }
    })
    .mouseup(function() {
      MOUSEDOWN = false;
    });
  }


  function start_up() {
    build_hyperparam_controls();
    build_track();
    build_drag_select();

    // initialize the snackbar
    var MDCSnackbar = mdc.snackbar.MDCSnackbar;
    var el = document.getElementById("snackbar");
    SNACKBAR = new MDCSnackbar(el);
  }

  document.addEventListener("DOMContentLoaded", function(event) {
    start_up();
  });

  ////////////////////////////////////////////////////////////////////////////
  ////////////////////////////////////////////////////////////////////////////
  // functions for the header

  function add_track() {
    build_track();
  }

  function clear_tracks(reset_midi) {
    $("#track-container").empty();
    TRACK_COUNT = 0;
    if (GOOGLE_COLAB && reset_midi) {   
      google.colab.kernel.invokeFunction("reset_midi", [], {});
    }
  }

  function open_hyperparam() {
    HYPERPARAM_OPEN = true;
    $(".hyperparam-wrapper").css("display", "grid");
    $(".overlay").css("display","block");
    [].map.call($("#hyperparam").find(".mdc-slider"), function(el) {
      el.MDCSlider = new mdc.slider.MDCSlider(el);
    });
  }
  function close_hyperparam() {
    HYPERPARAM_OPEN = false;
    $(".hyperparam-wrapper").css("display", "none");
    $(".overlay").css("display","none");
  }

  function get_status() {
    var can_generate = false;
    var can_listen = false;
    var status = {"tracks" : []};
    var tracks = $(".track");
    for (var i=0; i<tracks.length; i++) {
      var track_id = tracks[i].id.split("_")[1];
      var inst = $("#inst_" + track_id + "-mo")[0].MDCSelect.value;
      var density = $("#density-slider_" + track_id + "-slo")[0].MDCSlider.value;
      var density_disabled = $("#density-slider_" + track_id + "-slo")[0].MDCSlider.disabled;
      var min_poly = $("#poly_min_" + track_id + "-mo")[0].MDCSelect.value;
      var max_poly = $("#poly_max_" + track_id + "-mo")[0].MDCSelect.value;
      var min_dur = $("#dur_min_" + track_id + "-mo")[0].MDCSelect.value;
      var max_dur = $("#dur_max_" + track_id + "-mo")[0].MDCSelect.value;
      var resample = $("#resample_" + track_id + "-so")[0].MDCSwitch.checked;
      var mute = $("#mute_" + track_id + "-so")[0].MDCSwitch.checked;
      var solo = $("#solo_" + track_id + "-so")[0].MDCSwitch.checked;
      var highlighted_bars = get_highlighted_bars(track_id);
      if (any(highlighted_bars)) {
        can_generate = true;
      }
      if (solo || !mute) {
        can_listen = true;
      }

      density = parseInt(density) + 1;
      if (density_disabled) {
        density = 0;
      }

      var ignore = $("#ignore_" + track_id + "-so")[0].MDCSwitch.checked;
      var track_type = 10;
      if (inst.includes("drum_")) {
        track_type = 11;
      }

      status["tracks"].push({
        "track_id" : parseInt(track_id),
        "instrument" : inst,
        "instrument_num" : INST_MAP[inst],
        "density" : density,
        "track_type" : track_type,
        "mute" : mute,
        "solo" : solo,
        "ignore" : ignore,
        "resample" : resample,
        "selected_bars" : highlighted_bars,
        "min_polyphony_q" : "POLYPHONY_" + min_poly.toUpperCase(),
        "max_polyphony_q" : "POLYPHONY_" + max_poly.toUpperCase(),
        "min_note_duration_q" : "DURATION_" + min_dur.toUpperCase(),
        "max_note_duration_q" : "DURATION_" + max_dur.toUpperCase()
      });
    }

    var tempo = "120"; //document.getElementById("tempo").MDCSelect.value;
    status["temperature"] = parseFloat($("#temperature-mo")[0].MDCSelect.value);
    status["canGenerate"] = can_generate;
    status["canListen"] = can_listen;
    status["tempo"] = parseInt(tempo);
    status["nbars"] = CURRENT_NUM_BARS;

    //status["track_stride"] = parseInt($("#track_stride-mo")[0].MDCSelect.value);
    //status["bar_stride"] = parseInt($("#bar_stride-mo")[0].MDCSelect.value);
    status["tracks_per_step"] = parseInt($("#tracks_per_step-mo")[0].MDCSelect.value);
    status["bars_per_step"] = parseInt($("#bars_per_step-mo")[0].MDCSelect.value);
    status["shuffle"] = $("#shuffle-so")[0].MDCSwitch.checked;
    status["percentage"] = $("#percentage-slo")[0].MDCSlider.value;
    status["model_dim"] = parseInt($("#model_size-mo")[0].MDCSelect.value);

    //console.log(status);

    return status;
  }

  function add_midi() {
    //document.getElementById("stems").MDCSelect.value = "NONE";
    //clear_tracks(false);
    var floader = document.querySelector("#file_loader");
    floader.value = "";
    floader.click();
    floader.onchange = function() {
      var file = floader.files[0];
      var reader = new FileReader();
      if (GOOGLE_COLAB) {
        reader.onloadend = function (e) {
          var status = get_status();
          google.colab.kernel.invokeFunction("add_midi_callback", [status, this.result], {});
        }
        reader.readAsDataURL(file);
      }
      else {
        reader.onloadend = function (e) {
          build_from_midi(JSON.parse(this.result)["test_16"]["piece"]);
        }
        reader.readAsText(file);
      }
    }
  }

  function download_midi() {
    if (GOOGLE_COLAB) {
      google.colab.kernel.invokeFunction("download_midi_callback", [], {});
    }
  }

  function run_download(encoded_data) {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:audio/midi;base64,' + encoded_data);
    element.setAttribute('download', "download.mid");
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
  }

  function run_download_zip(encoded_data) {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:application/zip;base64,' + encoded_data);
    element.setAttribute('download', "download.zip");
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
  }

  function generate() {
    var status = get_status();
    if (status["tracks"].length == 0) {
      build_snackbar("Must add tracks before you can generate.");
      return;
    }
    if (!status["canGenerate"]) {
      build_snackbar("Must highlight one or more bars (by clicking on them) before you can generate.");
      return;
    }
    if (GOOGLE_COLAB) {
      google.colab.kernel.invokeFunction("generate_callback", [status], {});
    }
  }
  
  function play() {
    var status = get_status();
    if (status["tracks"].length == 0) {
      build_snackbar("There are no tracks to play!");
      return;
    }
    if (!status["canListen"]) {
      build_snackbar("Must unmute or solo atleast one track!")
      return;
    }
    if (GOOGLE_COLAB) {
      google.colab.kernel.invokeFunction("play_callback", [status], {});
    }
  }