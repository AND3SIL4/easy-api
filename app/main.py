from fastapi import FastAPI
from datetime import datetime
from app.database.db import create_db_and_models

create_db_and_models()


app = FastAPI()


@app.get("/")
def root():
    cur_date = datetime.now()
    return {"status": "working", "time": cur_date}
