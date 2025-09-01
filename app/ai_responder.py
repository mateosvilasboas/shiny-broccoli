from transformers import pipeline
import google.generativeai as genai
from app.settings import settings

class AIResponder:
    def __init__(self):
        if settings.GEMINI_API_KEY:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            self._model = genai.GenerativeModel('gemini-1.5-flash')
        
    def suggest_answer(self, classification: dict[str, str | float]) -> str:
        try:
            email_text = classification.get("text", "")
            label = classification.get("label", "")
            prompt = f"""Você é meu assistente de respostas de email
            em uma grande empresa que recebe alto volume
            de emails diariamente, podendo eles ser 
            productive (produtivo) ou non_productive (não produtivo).

            Caso o email possua vocativo, assine a resposta com o sujeito
            do vocativo.

            Explique porque provavelmente esse email é {label} e 
            sugira respostas para o texto de email presente abaixo,
            levando em consideração que ele é considerado um email {label}.
            
            Email: {email_text}"""
            response = self._model.generate_content(prompt)
            explanation = response.text
            return explanation
        except Exception as e:
            raise e