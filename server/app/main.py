import os
import ptvsd

from fastapi import FastAPI
from routers import gtfs

"""
Enable remote debugging
"""
if os.environ['ENVIRONMENT'] != 'PROD':
    ptvsd.enable_attach()

app = FastAPI()

app.include_router(gtfs.router)

@app.get("/")
def read_root():
    return {"Titi": "cocu"}
