from fastapi import FastAPI

app1 = FastAPI()

@app1.get('/')
async def root():
    return {"Message": "Hello Python"}