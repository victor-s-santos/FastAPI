from fastapi import FastAPI
from pydantic import BaseModel

app1 = FastAPI()
#root route
@app1.get('/')
def root():
    return {"Message": "Hello Python"}

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str

user_list = [
    User(id=1, first_name='Victor', last_name='Silva', email='victor@net.com'),
    User(id=2, first_name='Suelen', last_name='Simões', email='suelen@net.com')
]

#user list route
@app1.get('/users')
def get_user_list():
    """returns the list of registered users"""
    return(user_list)