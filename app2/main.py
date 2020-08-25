#from typing import Optional
import models
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
from sqlalchemy.orm import Session

app2 = FastAPI()

#create tables
models.Base.metadata.create_all(bind=engine)

#to use html templates
templates = Jinja2Templates(directory="templates")

@app2.get("/")
def dashboard(request: Request):
    """returns the stock dashboard"""
    context = {"request": request}
    return templates.TemplateResponse("dashboard.html", context)

@app2.post("/stock")
def create_stock():
    """post stocks and stores it in the database"""
    return{
        "status_code": 200,
        "message": "stock created successfully"
    }