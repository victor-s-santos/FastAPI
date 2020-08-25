#from typing import Optional
import models
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models import Stock
app2 = FastAPI()
models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")
class StockRequest(BaseModel):
    symbol: str

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app2.get("/")
def dashboard(request: Request):
    """returns the stock dashboard"""
    context = {"request": request}
    return templates.TemplateResponse("dashboard.html", context)

@app2.post("/stock")
def create_stock(stock_request: StockRequest, db: Session = Depends(get_db)):
    """post stocks and stores it in the database"""
    stock = Stock()
    stock.symbol = stock_request.symbol
    #populating the database
    db.add(stock)
    db.commit()
    return{
        "status_code": 200,
        "message": "stock created successfully"
    }