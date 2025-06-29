from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse


name="sameer shrinath"
app=FastAPI()

@app.get('/')
async def page_html():
    return FileResponse("index.html")



@app.get('/hello')
def hello():
    return {"Message":"Hello I am sameer"}

@app.get('/name')
def return_name():
    return {"name":name}

class UserInput(BaseModel):
    name: str
    age: int

user_inputs = []

@app.post('/submit')
def submit_user_input(user: UserInput):
    user_inputs.append(user)
    return {"message": "User input received"}

@app.get('/users')
def get_users():
    return {"users": [user.dict() for user in user_inputs]}