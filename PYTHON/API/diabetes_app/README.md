# Diabetes Prediction App

A machine learning-powered diabetes prediction application with both HTML and Streamlit frontends, powered by a FastAPI backend.

## 📋 Features

- **Dual Frontend Options**:
  - 🌐 **HTML Frontend**: Modern web interface with beautiful CSS styling
  - 🎨 **Streamlit Frontend**: Interactive Python-based web app with advanced features

- **FastAPI Backend**: High-performance API server with automatic documentation
- **Machine Learning Model**: Pre-trained diabetes prediction model
- **Real-time Predictions**: Instant predictions based on health parameters
- **CORS Enabled**: Cross-origin requests supported for both frontends

## 🚀 Quick Start

### Option 1: Run Everything at Once (Recommended)
```bash
# Run both FastAPI backend and Streamlit frontend
run_full_app.bat
```

### Option 2: Run Components Separately

#### Start FastAPI Backend
```bash
# Start the API server
run_server.bat
# OR manually:
uvicorn Main:app --reload --host 0.0.0.0 --port 8000
```

#### Start Streamlit Frontend
```bash
# Start Streamlit app (requires FastAPI server to be running)
run_streamlit.bat
# OR manually:
streamlit run streamlit_app.py
```

#### Access HTML Frontend
- Start FastAPI server first
- Open browser and go to: http://localhost:8000

## 📊 Application URLs

- **FastAPI Backend**: http://localhost:8000
- **HTML Frontend**: http://localhost:8000
- **Streamlit Frontend**: http://localhost:8501
- **API Documentation**: http://localhost:8000/docs
- **API Health Check**: http://localhost:8000/health

## 📝 Required Parameters

| Parameter | Description | Range |
|-----------|-------------|-------|
| **Pregnancies** | Number of times pregnant | 0-20 |
| **Glucose** | Plasma glucose concentration (mg/dL) | 0-300 |
| **Blood Pressure** | Diastolic blood pressure (mmHg) | 0-200 |
| **Skin Thickness** | Triceps skin fold thickness (mm) | 0-100 |
| **Insulin** | 2-Hour serum insulin (μU/mL) | 0-900 |
| **BMI** | Body mass index (kg/m²) | 0-70 |
| **Diabetes Pedigree Function** | Diabetes pedigree function | 0-3 |
| **Age** | Age in years | 1-120 |

## 🛠️ Installation

1. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify Model File**:
   - Ensure `diabetes_model.sav` is present in the directory

3. **Run the Application**:
   - Use `run_full_app.bat` for complete setup
   - Or run components individually as described above

## 🎯 Frontend Comparison

### HTML Frontend
- ✅ **Classic Web Interface**: Traditional HTML/CSS/JavaScript
- ✅ **Beautiful Design**: Custom styled with gradients and animations
- ✅ **Sample Data**: Double-click to fill sample data
- ✅ **Responsive**: Mobile-friendly design
- ✅ **Fast Loading**: Lightweight and quick

### Streamlit Frontend
- ✅ **Interactive Components**: Rich widgets and controls
- ✅ **Real-time Validation**: Input validation and helpful tooltips
- ✅ **Advanced Features**: Sidebar configuration, expandable sections
- ✅ **Visual Feedback**: Loading spinners, success animations
- ✅ **Server Configuration**: Configurable backend URL
- ✅ **Model Information**: Built-in model info display
- ✅ **Error Handling**: Comprehensive error messages
- ✅ **Sample Data**: One-click sample data filling

## 🔧 API Endpoints

### POST `/diabetes_prediction`
Predict diabetes risk based on health parameters.

**Request Body**:
```json
{
    "Pregnancies": 6,
    "Glucose": 148,
    "BloodPressure": 72,
    "SkinThickness": 35,
    "Insulin": 0,
    "BMI": 33.6,
    "DiabetesPedigreeFunction": 0.627,
    "Age": 50
}
```

**Response**:
```json
"the person is diabetic"
```

### GET `/health`
Check API health status.

### GET `/model-info`
Get information about the trained model.

### GET `/`
Serve the HTML frontend.

## 📁 Project Structure

```
diabetes_app/
├── Main.py                 # FastAPI backend
├── streamlit_app.py        # Streamlit frontend
├── index.html             # HTML frontend
├── diabetes_model.sav     # Trained ML model
├── modelinfo.txt          # Model information
├── requirements.txt       # Python dependencies
├── run_server.bat         # Start FastAPI server
├── run_streamlit.bat      # Start Streamlit app
├── run_full_app.bat       # Start both applications
└── README.md              # This file
```

## 🧪 Testing

### Sample Data for Testing
- **Pregnancies**: 6
- **Glucose**: 148
- **Blood Pressure**: 72
- **Skin Thickness**: 35
- **Insulin**: 0
- **BMI**: 33.6
- **Diabetes Pedigree Function**: 0.627
- **Age**: 50

Expected Result: "the person is diabetic"

## ⚠️ Important Notes

- **Educational Purpose**: This application is for educational purposes only
- **Medical Advice**: Always consult healthcare professionals for medical advice
- **Model Accuracy**: Predictions are based on a trained model and may not be 100% accurate
- **Server Dependency**: Streamlit frontend requires FastAPI server to be running

## 🔒 Security Considerations

- CORS is currently set to allow all origins (`*`) for development
- In production, replace with specific allowed domains
- Consider adding authentication and rate limiting for production use

## 📞 Troubleshooting

### Common Issues:

1. **"Import streamlit could not be resolved"**
   - Run: `pip install -r requirements.txt`

2. **"Connection Error" in Streamlit**
   - Ensure FastAPI server is running on http://localhost:8000
   - Check the server URL in Streamlit sidebar

3. **"Port already in use"**
   - Kill existing processes or use different ports
   - FastAPI: `uvicorn Main:app --port 8001`
   - Streamlit: `streamlit run streamlit_app.py --server.port 8502`

4. **Model file not found**
   - Ensure `diabetes_model.sav` is in the same directory as `Main.py`

## 🎓 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Scikit-learn Documentation](https://scikit-learn.org/)

---

Made with ❤️ for diabetes risk assessment and education.
