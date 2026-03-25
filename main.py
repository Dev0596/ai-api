from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    data: str

@app.post("/predict")
def predict(input: InputData):
    if "good" in input.data.lower():
        result = "positive"
    else:
        result = "negative"
    return {"prediction": result}