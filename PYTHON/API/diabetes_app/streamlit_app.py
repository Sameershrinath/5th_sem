import streamlit as st
import requests
import json

# Page configuration
st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="🏥",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E86AB;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        color: #6C757D;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .info-box {
        background-color: #E3F2FD;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #2196F3;
        margin-bottom: 2rem;
            
    }
    .prediction-success {
        background-color: #D4EDDA;
        color: #155724;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #28A745;
        margin-top: 1rem;
    }
    .prediction-warning {
        background-color: #FFF3CD;
        color: #856404;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #FFC107;
        margin-top: 1rem;
    }
    .prediction-error {
        background-color: #F8D7DA;
        color: #721C24;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #DC3545;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">🏥 Diabetes Prediction App</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Enter your health parameters to predict diabetes risk</p>', unsafe_allow_html=True)

# Info box
st.markdown("""
<div class="info-box" style="color: #000;">
    <h3>ℹ️ How to use:</h3>
    <p>Fill in all the required health parameters below. The AI model will analyze your data and predict whether you might be at risk for diabetes. This is for educational purposes only and should not replace professional medical advice.</p>
</div>
""", unsafe_allow_html=True)

# Sidebar for additional information
st.sidebar.title("📊 Parameter Information")
st.sidebar.markdown("""
**Parameter Ranges:**
- **Pregnancies**: 0-20
- **Glucose**: 0-300 mg/dL
- **Blood Pressure**: 0-200 mmHg
- **Skin Thickness**: 0-100 mm
- **Insulin**: 0-900 μU/mL
- **BMI**: 0-70 kg/m²
- **Diabetes Pedigree Function**: 0-3
- **Age**: 1-120 years
""")

# Add sample data button in sidebar
if st.sidebar.button("📋 Fill Sample Data"):
    st.session_state['pregnancies'] = 6
    st.session_state['glucose'] = 148
    st.session_state['blood_pressure'] = 72
    st.session_state['skin_thickness'] = 35
    st.session_state['insulin'] = 0
    st.session_state['bmi'] = 33.6
    st.session_state['dpf'] = 0.627
    st.session_state['age'] = 50

# Server configuration
st.sidebar.title("⚙️ Server Configuration")
server_url = st.sidebar.text_input("Server URL", value="http://localhost:8000")

# Create input form
st.header("📝 Enter Your Health Parameters")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input(
        "Pregnancies",
        min_value=0,
        max_value=20,
        value=st.session_state.get('pregnancies', 0),
        help="Number of times pregnant"
    )
    
    glucose = st.number_input(
        "Glucose Level (mg/dL)",
        min_value=0,
        max_value=300,
        value=st.session_state.get('glucose', 120),
        help="Plasma glucose concentration"
    )
    
    blood_pressure = st.number_input(
        "Blood Pressure (mmHg)",
        min_value=0,
        max_value=200,
        value=st.session_state.get('blood_pressure', 80),
        help="Diastolic blood pressure"
    )
    
    skin_thickness = st.number_input(
        "Skin Thickness (mm)",
        min_value=0,
        max_value=100,
        value=st.session_state.get('skin_thickness', 20),
        help="Triceps skin fold thickness"
    )

with col2:
    insulin = st.number_input(
        "Insulin Level (μU/mL)",
        min_value=0,
        max_value=900,
        value=st.session_state.get('insulin', 80),
        help="2-Hour serum insulin"
    )
    
    bmi = st.number_input(
        "BMI (kg/m²)",
        min_value=0.0,
        max_value=70.0,
        value=float(st.session_state.get('bmi', 25.0)),
        step=0.1,
        help="Body mass index"
    )
    
    dpf = st.number_input(
        "Diabetes Pedigree Function",
        min_value=0.000,
        max_value=3.000,
        value=float(st.session_state.get('dpf', 0.500)),
        step=0.001,
        help="Diabetes pedigree function"
    )
    
    age = st.number_input(
        "Age (years)",
        min_value=1,
        max_value=120,
        value=st.session_state.get('age', 30),
        help="Age in years"
    )

# Prediction button
if st.button("🔮 Predict Diabetes Risk", type="primary", use_container_width=True):
    # Prepare data for API call
    data = {
        "Pregnancies": int(pregnancies),
        "Glucose": int(glucose),
        "BloodPressure": int(blood_pressure),
        "SkinThickness": int(skin_thickness),
        "Insulin": int(insulin),
        "BMI": float(bmi),
        "DiabetesPedigreeFunction": float(dpf),
        "Age": int(age)
    }
    
    try:
        # Show spinner while making request
        with st.spinner('Analyzing your data...'):
            # Make API call
            response = requests.post(
                f"{server_url}/diabetes_prediction",
                json=data,
                headers={"Content-Type": "application/json"},
                timeout=10
            )
            
            if response.status_code == 200:
                prediction = response.text.strip('"')
                
                # Display results
                if 'not diabetic' in prediction.lower():
                    st.markdown(f"""
                    <div class="prediction-success">
                        <h3>✅ Good News!</h3>
                        <p>The model predicts you are <strong>not diabetic</strong>.</p>
                        <p><small>Keep maintaining a healthy lifestyle!</small></p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Show balloons for good news
                    st.balloons()
                    
                else:
                    st.markdown(f"""
                    <div class="prediction-warning">
                        <h3>⚠️ Warning</h3>
                        <p>The model predicts you might be <strong>diabetic</strong>.</p>
                        <p><small>Please consult a healthcare professional for proper diagnosis and treatment.</small></p>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Show the raw prediction for reference
                st.info(f"Raw prediction: {prediction}")
                
            else:
                st.markdown(f"""
                <div class="prediction-error">
                    <h3>❌ Error</h3>
                    <p>Server returned error code: {response.status_code}</p>
                    <p><small>Please check if the server is running and try again.</small></p>
                </div>
                """, unsafe_allow_html=True)
                
    except requests.exceptions.ConnectionError:
        st.markdown("""
        <div class="prediction-error">
            <h3>❌ Connection Error</h3>
            <p>Could not connect to the server.</p>
            <p><small>Please make sure the FastAPI server is running on the specified URL.</small></p>
        </div>
        """, unsafe_allow_html=True)
        
    except requests.exceptions.Timeout:
        st.markdown("""
        <div class="prediction-error">
            <h3>❌ Timeout Error</h3>
            <p>The request timed out.</p>
            <p><small>The server might be busy. Please try again.</small></p>
        </div>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        st.markdown(f"""
        <div class="prediction-error">
            <h3>❌ Unexpected Error</h3>
            <p>An unexpected error occurred: {str(e)}</p>
            <p><small>Please try again or contact support.</small></p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6C757D; margin-top: 2rem;">
    <p>🔬 This application is for educational purposes only.</p>
    <p>Always consult with healthcare professionals for medical advice.</p>
</div>
""", unsafe_allow_html=True)

# Display model information in expander
with st.expander("📋 Model Information", expanded=False):
    try:
        # Try to read model info if it exists
        with open("modelinfo.txt", "r") as f:
            model_info = f.read()
            st.text(model_info)
    except FileNotFoundError:
        st.write("Model information file not found.")
    except Exception as e:
        st.write(f"Error reading model information: {e}")
