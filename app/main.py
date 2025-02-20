from fastapi import FastAPI
from datetime import datetime


app = FastAPI()


@app.get("/")
def root():
    cur_date = datetime.now()
    return {"status": "working", "time": cur_date}
