# https://www.medi-08-data-06.work/entry/machine-learning-api

import time
import hashlib
from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum
from typing import List

from MMM import MMM

app = FastAPI()

class BaseBody(BaseModel):
    hash: str

class Generate(BaseBody):
    instruments: List[str]

@app.get("/health")
async def get_health():
    return {"message": "OK"}

@app.get('/init')
async def init():
    ut = str(time.time())
    hash = hashlib.sha256(ut.encode()).hexdigest()
    try:
        mmm = MMM(hash=hash)
        mmm.reset_midi()
        return {'hash': hash}
    except:
        return {'message': 'Initialization error.'}

@app.post('/generate')
async def generate(body: Generate):
    try:
        mmm = MMM(hash=body.hash)
        mmm.generate(instruments=body.instruments)
    except:
        return {'message': 'Failed to generate music.'}

handler = Mangum(app)