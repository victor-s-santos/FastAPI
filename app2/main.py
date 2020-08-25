from typing import Optional

from fastapi import FastAPI

app2 = FastAPI()


@app2.get("/")
def dashboard():
    """returns the stock dashboard"""
    return {"Dashboard": "Welcome"}

@app2.post("/stock")
def create_stock():
    """post stocks and stores it in the database"""
    return{
        "status_code": 200,
        "message": "stock created successfully"
    }