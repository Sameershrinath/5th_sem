from fastapi import FastAPI
from pydentic import BaseModel
import pickle
import json


app=FastAPI()

class Model_input(BaseModel):
    Pregnancies:int
    Glucose:int
    BloodPressure:int
    SkinThickness:int
    Insulin:int
    BMI:float
    DiabetesPedigreeFunction:float
    Age:int