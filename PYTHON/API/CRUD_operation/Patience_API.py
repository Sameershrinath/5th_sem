from fastapi import FastAPI,Path,HTTPException,Query
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

@app.get("/patient/{patient_id}")
def view_patient(patient_id:str=Path(...,description="enter the patient ID")):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    # else:
    #     return {"message":"Patient not found"} (it will be done in case dont want the success code 200)
    raise HTTPException(status_code=404,detail="Patient not found.")

@app.get("/sort")
def sort_patient(sort_by:str=Query(...,description="sort on the basis of height, weight and bmi"),order:str=Query('asc',description='sort in ascending and descending order')):
    valid_fields=['height','weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f'Invalid field , select from {valid_fields}')
    if order not in ['asc','dsc']:
        raise HTTPException(status_code=400,detail='Invalid order , select from asc or dsc')
    
    sort_order=True if order=="dsc" else False 
    data=load_data()

    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)

    return sorted_data
