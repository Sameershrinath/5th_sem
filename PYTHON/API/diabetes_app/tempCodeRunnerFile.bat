@echo off
echo Starting FastAPI Diabetes Prediction Server...
echo.
echo Make sure you have installed the requirements:
echo pip install -r requirements.txt
echo.
echo Server will be available at: http://localhost:8000
echo.
call conda activate base
uvicorn Main:app --reload --host 0.0.0.0 --port 8000
