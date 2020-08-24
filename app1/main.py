from fastapi import FastAPI
from pydantic import BaseModel

app1 = FastAPI()
#root route
@app1.get('/')
def root():
    return {"Message": "Hello Python"}