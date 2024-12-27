from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from prophet.config import Config
from prophet.data import Label
from prophet.text_classifier import TextClassifier


class PredictRequest(BaseModel):
    text: str


class PredictResponse(BaseModel):
    prediction: Label
    text: str


app = FastAPI(
    title="Prophet API",
    description="Predict the label of a text - just-do-it or stop",
    version="0.1.0",
)
model = TextClassifier.load(Config.Path.MODELS_DIR / Config.Model.FILE_NAME)


@app.post(
    "/predict",
    response_model=PredictResponse,
    summary="Predict the label of a text",
)
async def predict(request: PredictRequest):
    try:
        prediction = model.predict(request.text)
        return PredictResponse(prediction=Label(prediction), text=request.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
