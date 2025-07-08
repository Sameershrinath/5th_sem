# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy file
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "Insurance_predictor:app", "--host", "0.0.0.0", "--port", "8000"]
