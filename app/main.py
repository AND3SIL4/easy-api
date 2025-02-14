from datetime import datetime

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    cur_date = datetime.now()
    return {"status": "working", "time": cur_date}
