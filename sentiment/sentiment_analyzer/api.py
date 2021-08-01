from typing import Dict
from fastapi import Depends, FastAPI
from pydantic import BaseModel

app = FastAPI()

from classifier.model import get_model


class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    probabilities: Dict[str, float]
    sentiment: str
    confidence: float

@app.post("/predict", response_model=SentimentResponse)
def predict(request: SentimentRequest, model: Model = Depends(get_model)):
    sentiment, confidence, probabilities = model.predict(request.text)
    return SentimentResponse(
        sentiment=sentiment,
        confidence=confidence,
        probabilities=probabilities
    )