# https://www.medi-08-data-06.work/entry/machine-learning-api

import time
import hashlib
import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum
from boto3 import Session
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


# @app.post('/add_track')
# async def add_track(body: BaseBody):
#     try:
#         mmm = MMM(hash=body.hash)
#         mmm.add_new_track()
#         return {'message': 'SUCCESS'}
#     except:
#         return {'message': 'Failed to add a track.'}

@app.post('/generate')
async def generate(body: Generate):
    try:
        mmm = MMM(hash=body.hash)
        mmm.generate_callback(instruments=body.instruments)
    except:
        return {'message': 'Failed to generate music.'}

# @app.post("/predict")
# async def post_predict(features:List[Features]):
#     # S3からモデル読み込み
#     session = Session()
#     s3client = session.client("s3")
#     model_obj = s3client.get_object(Bucket="my-boston-model", Key="boston.model")
#     model = pickle.loads(model_obj["Body"].read())
#     # PUTされたjsonをpndasに整形
#     rm_list = [feature.RM for feature in features]
#     age_list = [feature.AGE for feature in features]
#     df_feature = pd.DataFrame({
#         "RM" :rm_list,
#         "AGE":age_list
#     })
#     # 予測結果をjsonに変換
#     pred = model.predict(df_feature)
#     responce = [{"predict":p} for p in pred]
#     return responce

handler = Mangum(app)