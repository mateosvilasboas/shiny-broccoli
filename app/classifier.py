from typing import Any, List
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    pipeline,
    Pipeline
)

class EmailClassifier:
    def __init__(self, model_path: str = "models/email_classifier"):
        """
        Carrega o modelo treinado para classificação produtivo/não-produtivo
        """
        try:
            self._tokenizer = AutoTokenizer.from_pretrained(model_path)
            self._model = AutoModelForSequenceClassification.from_pretrained(model_path)
            self._pipe = pipeline(
                "text-classification", 
                model=self._model, 
                tokenizer=self._tokenizer
            )
        except Exception:
            model_name = "neuralmind/bert-base-portuguese-cased"
            self._tokenizer = AutoTokenizer.from_pretrained(model_name)
            self._model = AutoModelForSequenceClassification.from_pretrained(
                model_name,
                num_labels=2,
                id2label={0: "non_productive", 1: "productive"},
                label2id={"non_productive": 0, "productive": 1}
            )
            self._pipe = pipeline(
                "text-classification",
                model=self._model,
                tokenizer=self._tokenizer
            )
    
    @property
    def pipe(self) -> Pipeline:
        return self._pipe
    
    def classify_text(self, text: str) -> List[dict[str, Any]]:
        return self.pipe(text)
    