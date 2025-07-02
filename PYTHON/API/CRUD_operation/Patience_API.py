from fastapi import FastAPI
import json


app=FastAPI()


def load_data():
    with open('Patient_details.json',"r") as f:
        data=json.load(f)
    return data



@app.get("/")
def hello():
    return {"Message":"Welcome to the patience management system."}

@app.get("/about")
def about():
    return {"message":"A fully functional API to manage patience."}

@app.get("/view")
def view():
    data=load_data()
    return data