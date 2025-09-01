import re
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.classifier import EmailClassifier
from app.ai_responder import AIResponder
from app.schemas import Input, Output

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


def nl2br(text):
    if not text:
        return ""
    return text.replace('\n', '<br>\n')

def convert_markdown(text):
    if not text:
        return ""
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\n\n+', '</p><p>', text)
    text = f'<p>{text}</p>'
    text = text.replace('\n', '<br>')
    
    return text

templates.env.filters["nl2br"] = nl2br
templates.env.filters["markdown"] = convert_markdown

@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        request=request
    )

@app.post('/suggestion', response_model=Output)
async def suggestion(input: Input):
    try:
        text = input.text
        email_classifier = EmailClassifier()
        classified_text = email_classifier.classify_text(
            text=text
        )
        label = classified_text[0].get("label", None)
        score = classified_text[0].get("score", None)
        classified_text_dict = {
            "text": text,
            "label": label,
            "score": score
        }
        responder = AIResponder()
        explanation = responder.suggest_answer(
            classification=classified_text_dict)

        return {
            "explanation": explanation
        }
    except Exception as e:
        raise e
