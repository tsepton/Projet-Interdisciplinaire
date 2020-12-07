from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import HTTPException
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
    try:
        prediction = predict(
            info.stop.upper(), info.line.upper(), info.direction.lower())[0]
    except:
        raise HTTPException(
            status_code=418,
            detail="Sorry, l'API de la STIB puait la merde, on a pas eu le time"
        )
    return prediction
