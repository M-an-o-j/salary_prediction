from fastapi import FastAPI, Depends
from fastapi import APIRouter
# from app.utils import 
from pickle import load
from contextlib import asynccontextmanager
import os

from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]


model = None

@asynccontextmanager
async def load_model(app: FastAPI):
    global model
    try:
        # Print the model path to confirm it's correct
        model_path = "D:/projects/salary_prediction/backend/salary_prediction/app/utils/linear_regression_model.pkl"
        print(f"Attempting to load model from: {model_path}")
        
        # Check if the file exists
        if not os.path.exists(model_path):
            print(f"Model file not found at {model_path}")
        else:
            # Open and load the model
            with open(model_path, "rb") as model_file:
                model = load(model_file)
                print("Model loaded successfully!")
    except Exception as e:
        print(f"Error loading model: {e}")
    
    yield  # Yield control back to FastAPI

    # Handle cleanup on shutdown
    print("Application is shutting down, unloading model...")
    model = None


app = FastAPI(debug=True,summary="Example route", title="Welcome to fastapi", lifespan= load_model)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Specifies the allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

def get_model():
    if model is None:
        raise Exception("Model is not loaded!")
    return model