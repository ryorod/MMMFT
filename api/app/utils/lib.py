from typing import List
from const import INST_MAP, POLY_LEVELS, DUR_LEVELS, CURRENT_NUM_BARS

def get_status(instruments: List[str]):
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
            "selected_bars" : get_highlighted_bars(),
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

def get_highlighted_bars():
    highlighted_bars = []
    for i in range(CURRENT_NUM_BARS):
        highlighted_bars.append(True)
    return highlighted_bars