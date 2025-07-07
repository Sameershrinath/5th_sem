from fastapi import FastAPI, Path, HTTPException, Query
import json
from typing import Annotated, Literal
from pydantic import BaseModel, Field,
from fastapi.responses import JSONResponse

app = FastAPI()

# --- Patient Input Model ---
class Patient(BaseModel):
    id: Annotated[str, Field(..., description="Id of the patient", examples=["P001"])]
    name: Annotated[str, Field(..., description="Name of the patient", examples=["samir Srinath"])]
    city: Annotated[str, Field(..., description="Address of the patient", examples=["jaipur"])]
    age: Annotated[int, Field(..., gt=0, lt=120, description="Enter the age", examples=[45])]
    gender: Annotated[Literal["male", "female", "others"], Field(..., description="male, female, others")]
    height: Annotated[float, Field(..., gt=0, description="Height in meters")]
    weight: Annotated[float, Field(..., gt=1, description="Weight in kg")]

# --- Load patient data ---
def load_data():
    try:
        with open('Patient_details.json', "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# --- Save patient data ---
def save_data(data):
    with open('Patient_details.json', "w") as f:
        json.dump(data, f, indent=4)

# --- Home route ---
@app.get("/")
def hello():
    return {"Message": "Welcome to the patient management system."}

# --- About route ---
@app.get("/about")
def about():
    return {"message": "A fully functional API to manage patients."}

# --- View all patients ---
@app.get("/view")
def view():
    data = load_data()
    return data

# --- View specific patient ---
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description="Enter the patient ID")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found.")

# --- Sort patients by height, weight or BMI ---
@app.get("/sort")
def sort_patient(
    sort_by: str = Query(..., description="Sort by: height, weight or BMI"),
    order: str = Query('asc', description='Sort order: asc or dsc')
):
    valid_fields = ['height', 'weight', 'BMI']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field. Choose from {valid_fields}')
    if order not in ['asc', 'dsc']:
        raise HTTPException(status_code=400, detail='Invalid order. Choose from asc or dsc')

    sort_order = True if order == "dsc" else False
    data = load_data()

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data

# --- Create new patient ---
@app.post("/create")
def create_patient(patient: Patient):
    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already exists')

    bmi = round(patient.weight / (patient.height ** 2), 2)
    verdict = (
        "Under-weight" if bmi < 18.5 else
        "Normal" if bmi < 30 else
        "Obese"
    )

    data[patient.id] = {
        "name": patient.name,
        "city": patient.city,
        "age": patient.age,
        "gender": patient.gender,
        "height": patient.height,
        "weight": patient.weight,
        "BMI": bmi,
        "Verdict": verdict
    }

    save_data(data)
    return JSONResponse(status_code=201, content={'message': "Patient created successfully"})
