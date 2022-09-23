from pydantic import BaseModel
from typing import List, Optional

class BaseBody(BaseModel):
    hash: str

class HealthRes(BaseModel):
    message: Optional[str] = 'OK'

class InitRes(BaseBody):
    pass

class GenerateReq(BaseBody):
    instruments: List[str]

class GenerateRes(BaseBody):
    filename: str