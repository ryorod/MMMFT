# https://www.medi-08-data-06.work/entry/machine-learning-api

import time
import hashlib
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from mangum import Mangum
from starlette.middleware.cors import CORSMiddleware
from utils.req_res import *
from utils.exception import GenerationException, InitializationException

from MMM import MMM

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# GET
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
    except InitializationException as e:
        print(e)
    return InitRes(hash=hash)


# POST
@app.post('/generate')
async def generate(req: GenerateReq):
    try:
        filename = app.state.mmm.generate(instruments=req.instruments)
    except GenerationException as e:
        print(e)
    return GenerateRes(hash=app.state.mmm.hash, filename=filename)


# Exception
@app.exception_handler(Exception)
async def unknown_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={'message': 'Internal error.'})

@app.exception_handler(InitializationException)
async def initialization_exception_handler(request: Request, exc: InitializationException):
    return JSONResponse(status_code=400, content={'message': 'Initialization error.'})

@app.exception_handler(GenerationException)
async def generation_exception_handler(request: Request, exc: GenerationException):
    return JSONResponse(status_code=400, content={'message': 'Failed to generate music.'})


# Mangum
handler = Mangum(app)