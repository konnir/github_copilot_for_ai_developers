from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import random
import joblib
from fastapi.responses import FileResponse


# Define the request model
class SentenceRequest(BaseModel):
    sentence: str

# Initialize FastAPI app
app = FastAPI()

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the static files directory to /ui
app.mount("/ui", StaticFiles(directory="static", html=True), name="static")
app.mount("/images", StaticFiles(directory="images"), name="images")

@app.get("/")
async def main():
    return FileResponse('templates/index.html')

# Load the model and vectorizer from files
classifier_load = joblib.load('model/rf/naive_bayes_model.joblib')
vectorizer_load = joblib.load('model/rf/tfidf_vectorizer.joblib')

# Define the endpoint
@app.post("/predict")
async def predict(request: SentenceRequest):
    sentence = request.sentence
    
    # Convert the sentence to TF-IDF features
    sentence_tfidf = vectorizer_load.transform([sentence])

    # Make a prediction
    prediction = classifier_load.predict(sentence_tfidf)

    return {prediction[0]}