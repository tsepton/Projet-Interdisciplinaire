from fastapi import APIRouter, HTTPException
import csv
import os.path
import re

router = APIRouter()
data_path = "data/gtfs/"


@router.get("/gtfs/{file}/")
async def read_gtfs(file: str):
    file += '.txt'
    if os.path.isfile(data_path + file):
        return file_to_json(file)
    else:
        raise HTTPException(status_code=404, detail="Gtfs file not found")


def file_to_json(file: str):
    stops = []
    with open(data_path + file, newline='') as csvstops:
        reader = csv.DictReader(csvstops)
        for dic in reader:
            stops.append({key: re.sub(' +', ' ', dic[key]) for key in dic})
    return stops
