from fastapi import APIRouter, HTTPException
import os.path
import json

router = APIRouter()
data_path = "data/shapefiles/"

@router.get("/shapefiles/{file}/")
async def read_shapefiles(file: str):
    file += '.geojson'
    if os.path.isfile(data_path + file):
        with open(data_path + file, newline='') as shapefile:
            return json.load(shapefile)
    else:
        raise HTTPException(status_code=404, detail="Shapefile not found")