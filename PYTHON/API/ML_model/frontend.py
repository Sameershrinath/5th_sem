import streamlit as st 
import requests

API_url= "http://13.62.47.96:8000/predict"
st.title("Insurance Premium category Predictor")

st.markdown("Enter your details below :")


age=st.number_input("Age",min_value=1,max_value=119,value=30)
weight=st.number_input("Weight (kg)",min_value=1.0,max_value=120.0,value=65.0)
height=st.number_input("Height (m)",min_value=1.0,value=1.7)
income_lpa=st.number_input("Income (LPA)",min_value=0.1,value=1.0)
smoker=st.selectbox("Are you smoker?",options=["true","false"])
city=st.text_input("City",value="Delhi")
occupation=st.selectbox("Occupation",options=['retired', 'freelancer', 'student', 'government_job','business_owner', 'unemployed', 'private_job'])

if st.button("Predict Premium Category"):
    input_data={
        "age":age,
        "weight":weight,
        "height":height,
        "income_lpa":income_lpa,
        "smoker":smoker,
        "city":city,
        "occupation":occupation
    }
    try:
        response=requests.post(API_url,json=input_data)
        if response.status_code==200:
            result=response.json()
            st.success(f"Predicted Insurance Premium Category: **{result['predicted_category']}**")
        else:
            st.error(f"API Error: {response.status_code}-{response.text}")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the FastAPI server. Make sure it's running on port 8000.")
        