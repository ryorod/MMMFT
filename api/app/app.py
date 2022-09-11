# https://www.medi-08-data-06.work/entry/machine-learning-api

import time
import hashlib
from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum
from typing import List

from MMM import MMM

app = FastAPI()

class BaseReq(BaseModel):
    hash: str

class Generate(BaseReq):
    instruments: List[str]

@app.get("/health")
async def get_health():
    return {"message": "OK"}

@app.get('/init')
async def init():
    ut = str(time.time())
    hash = hashlib.sha256(ut.encode()).hexdigest()
    try:
        app.state.mmm = MMM(hash=hash)
        app.state.mmm.reset_midi()
        return {'hash': hash}
    except:
        return {'message': 'Initialization error.'}

@app.post('/generate')
async def generate(req: Generate):
    try:
        filename = app.state.mmm.generate(instruments=req.instruments)
        return {'hash': app.state.mmm.hash, 'filename': filename}
    except:
        return {'message': 'Failed to generate music.'}

handler = Mangum(app)