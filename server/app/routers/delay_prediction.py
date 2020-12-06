from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from machine_learning.model_prediction import predict

router = APIRouter()

class Info(BaseModel):
    stop: str
    line: str
    direction: str

class Prediction(BaseModel):
    result: float

@router.post("/delay")
async def delay_prediction(info: Info):
    prediction = predict(info.stop, info.line, info.direction)
    return prediction[0]

    