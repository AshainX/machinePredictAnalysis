'''
Model prediction code here  

        there are two model files named as 
        MODEL_FILE = 'decisontreeclassifier.pkl'
        MODEL_FILE = 'logisticregression.pkl'

        in which decisiontree shows in 1.0 confidence most of the time in the synthetic data while some float values come in logisticregression.pkl so I used that only 

'''


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os
import pandas as pd


#MODEL_FILE = 'decisontreeclassifier.pkl'
MODEL_FILE = 'logisticregression.pkl'
app = FastAPI()


def loadModel():
    if not os.path.exists(MODEL_FILE):
        raise FileNotFoundError(f"File '{MODEL_FILE}' not found.")
    return joblib.load(MODEL_FILE)


try:
    model = loadModel()
except FileNotFoundError as e:
    model = None
    print(f"Error: {e}")



'''root endpoint'''
@app.get("/")
async def read_root():
    return {"message": "Welcome"}



'''   favicon endpoint  '''
@app.get("/favicon.ico")
async def favicon():
    return {"message": "No favicon is there"}

# Schema for prediction input
class PredictionInput(BaseModel):
    Temperature: float
    Run_Time: float

@app.post("/predict")
async def makePrediction(input: PredictionInput):
    global model
    if model is None:
        raise HTTPException(status_code=503, detail="Model is not available. Try again")
    input_data = pd.DataFrame([input.dict()])   #changing to i/p data to dataframe
    
    try:
        prediction = model.predict(input_data)
        confidence = model.predict_proba(input_data).max()
        confidence = round(confidence, 2) #two values after the decimal
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

    return {"Downtime": "Yes" if prediction[0] == 1 else "No", "Confidence": confidence}

