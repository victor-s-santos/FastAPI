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
    User(id=4, first_name='Victor', last_name='Silva', email='victor@net.com'),
    User(id=3, first_name='João', last_name='Pedro', email='joao@net.com'),
    User(id=2, first_name='José', last_name='Carlos', email='jose@net.com'),
    User(id=1, first_name='Suelen', last_name='Simoes', email='suelen@net.com'),
]

#user list route
@app1.get('/users')
def get_user_list():
    """returns the list of registered users"""
    return(user_list)

#user:id route
@app1.get('/users/{id_user}')
def get_user_by_id(id_user: int):
    """returns the request user by id"""
    for user in user_list:
        if(user.id == id_user):
            return user
    return("The requested user couldn't be found!")

@app1.post('/users/')
def post_user(user:User):
    """insert user in user_list"""
    user_list.append(user)
    return(f'The inserted user,{user.first_name}, has been created successfully!')