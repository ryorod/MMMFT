# https://www.medi-08-data-06.work/entry/machine-learning-api

import time
import hashlib
from fastapi import FastAPI
from mangum import Mangum
from utils.req_res import *
from utils.exception import GenerationException, InitializationException

from MMM import MMM

app = FastAPI()

@app.get("/health")
async def get_health():
    return HealthRes()

@app.get('/init')
async def init():
    ut = str(time.time())
    hash = hashlib.sha256(ut.encode()).hexdigest()
    try:
        app.state.mmm = MMM(hash=hash)
        app.state.mmm.reset_midi()
        raise InitializationException('Could not initialize.')
    except InitializationException as e:
        print(e)
    return InitRes(hash=hash)

@app.post('/generate')
async def generate(req: GenerateReq):
    try:
        filename = app.state.mmm.generate(instruments=req.instruments)
        raise GenerationException('Could not generate music.')
    except GenerationException as e:
        print(e)
    return GenerateRes(hash=app.state.mmm.hash, filename=filename)

handler = Mangum(app)