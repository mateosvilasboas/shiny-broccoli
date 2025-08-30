from fastapi import FastAPI
from app.classifier import EmailClassifier
from trainment.trainer import EmailClassifierTrainer
from app.schemas import Input, Output

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.post('/classify', response_model=Output)
async def test(input: Input):
    """
    Classifica email usando o modelo treinado
    """
    email_classifier = EmailClassifier()  # Agora carrega modelo treinado
    classified_text = email_classifier.classify_text(
        text=input.text
    )

    return {
        "text": input.text,
        "label": classified_text[0]["label"],
        "score": classified_text[0]["score"]
    }
    