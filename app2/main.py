#from typing import Optional
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
app2 = FastAPI()

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