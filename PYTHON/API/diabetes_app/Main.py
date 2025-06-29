from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import pickle
import json


app=FastAPI()

# Add CORS middleware to allow requests from HTML page
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (for CSS, JS, images if needed)
app.mount("/static", StaticFiles(directory="."), name="static")

# Serve the HTML page at root
@app.get("/")
async def read_index():
    return FileResponse('index.html')

class Model_input(BaseModel):
    Pregnancies:int
    Glucose:int
    BloodPressure:int
    SkinThickness:int
    Insulin:int
    BMI:float
    DiabetesPedigreeFunction:float
    Age:int

diabetes_model=pickle.load(open("diabetes_model.sav","rb"))

@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters:Model_input):
    input_data=input_parameters.json()
    input_dictionary=json.loads(input_data)

    preg=input_dictionary['Pregnancies']
    glu=input_dictionary['Glucose']
    bp=input_dictionary['BloodPressure']
    skin=input_dictionary['SkinThickness']
    insulin=input_dictionary['Insulin']
    bmi=input_dictionary['BMI']
    dpf=input_dictionary['DiabetesPedigreeFunction']
    age=input_dictionary['Age']

    input_list=[preg,glu,bp,skin,insulin,bmi,dpf,age]

    result=diabetes_model.predict([input_list])

    if result[0]==0:
        return 'the person is not diabetic'
    else:
        return 'the person is diabetic'

