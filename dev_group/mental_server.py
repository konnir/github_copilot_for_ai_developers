"""
Create a fastapi server that serves a pre-trained model model/text_classification_pipeline.pkl saved with joblib
load the model and create a predict endpoint that takes the input text from the request and
return the classification.
Read test line from model/test.txt (lines of text) and save it for later use.
add another get endpoint that reads the model/test.txt and randomly return a line from it in /test
don't forget to mount static folder.
make it run as uvicorn server.
also allow for index.html which is inside static folder to be served at the root endpoint.
"""
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import random
import uvicorn
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Load the pre-trained model
model_path = 'model/pipeline_model.pkl'
pipeline = joblib.load(model_path)

# Read test lines from file
test_lines_path = 'model/test.txt'
with open(test_lines_path, 'r') as file:
    test_lines = file.readlines()

# Define request model
class TextRequest(BaseModel):
    text: str

# Predict endpoint
@app.post("/predict")
def predict(request: TextRequest):
    prediction = pipeline.predict([request.text])
    return {"classification": prediction[0]}

# Test endpoint
@app.get("/test")
def get_test_line():
    return {"line": random.choice(test_lines).strip()}

# Mount static folder
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)