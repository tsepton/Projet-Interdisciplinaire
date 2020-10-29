import os
import ptvsd

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import gtfs, shapefiles

"""
Enable remote debugging
"""
if os.environ['ENVIRONMENT'] != 'PROD':
    ptvsd.enable_attach()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "http://localhost:5000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(gtfs.router)
app.include_router(shapefiles.router)


@app.get("/")
def read_root():
    return {"Titi": "cocu"}
