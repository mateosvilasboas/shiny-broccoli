import os
import pandas as pd
import numpy as np
from typing import Dict, Any, List
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    EvalPrediction,
    TrainingArguments,
    Trainer
)
from datasets import Dataset
from trainment.data import generate_dataset
from app.settings import settings

DATAFILE_PATH = os.path.join(settings.DATA_FOLDER, "email_dataset.csv")


class EmailClassifierTrainer:
    def __init__(self, model_name="neuralmind/bert-base-portuguese-cased"):
        self._model_name = model_name
        self._tokenizer = None
        self._model = None
        self._trainer = None
        self._train_dataset = None
        self._validation_dataset = None
        self._test_dataset = None

    def run(self) -> None:
        self._load_and_prepare_data()
        self._setup_model()
        self._tokenize_data()
        self._train()
        self._evaluate_on_test()

    def _load_and_prepare_data(self, csv_file:str=DATAFILE_PATH) -> None:
        dataframe = pd.read_csv(csv_file)
        texts = dataframe['text'].to_list()
        labels = dataframe['label'].to_list()

        train_val_texts, test_texts, train_val_labels, test_labels = train_test_split(
            texts, labels,
            test_size=0.15,
            stratify=labels,
            random_state=42
        )

        train_texts, validation_texts, train_labels, validation_labels = train_test_split(
            train_val_texts, train_val_labels,
            test_size=0.176,
            stratify=train_val_labels,
            random_state=42
        )

        self._train_dataset = Dataset.from_dict({
            "text": train_texts,
            "labels": train_labels,
        })
        self._validation_dataset = Dataset.from_dict({
            "text": validation_texts,
            "labels": validation_labels
        })
        self._test_dataset = Dataset.from_dict({
            "text": test_texts,
            "labels": test_labels
        })

    def _setup_model(self) -> None:
        try: 
            self._tokenizer = AutoTokenizer.from_pretrained(
                self._model_name
            )
            id_to_label = {
                0: "non_productive",
                1: "productive"
            }
            label_to_id = {
                "non_productive": 0,
                "productive": 1
            }

            self._model = AutoModelForSequenceClassification.from_pretrained(
                pretrained_model_name_or_path=self._model_name,
                num_labels=2,
                id2label=id_to_label,
                label2id=label_to_id
            )
        except Exception as e:
            raise e
    
    def _tokenize_data(self) -> None:
        def tokenize(examples: Dict) -> Dict:
            return self._tokenizer(
                examples["text"],
                padding="max_length",
                truncation=True,
                max_length=512,
                return_tensors="pt"
            )

        self._train_dataset = self._train_dataset.map(tokenize, batched=True)
        self._validation_dataset = self._validation_dataset.map(tokenize, batched=True)
        self._test_dataset = self._test_dataset.map(tokenize, batched=True)
    
    def _compute_metrics(self, eval_prediction: EvalPrediction) -> Dict[str, float]:
        predictions = eval_prediction.predictions
        references = eval_prediction.label_ids

        predicted_labels = np.argmax(predictions, axis=1)
        accuracy = accuracy_score(references, predicted_labels)
        report = classification_report(
            references,
            predicted_labels,
            output_dict=True,
            target_names=["non_productive", "productive"]
        )

        c_matrix = confusion_matrix(references, predicted_labels)
        productive_report = report["productive"]
        non_productive_report = report["non_productive"]
        macro_report = report["macro avg"]

        productive_precision = productive_report["precision"]
        productive_recall = productive_report["recall"]
        productive_f1 = productive_report["f1-score"]

        non_productive_precision = non_productive_report["precision"]
        non_productive_recall = non_productive_report["recall"]
        non_productive_f1 = non_productive_report["f1-score"]

        macro_precision = macro_report["precision"]
        macro_recall = macro_report["recall"]
        macro_f1 = macro_report["f1-score"]

        return {
            "accuracy": accuracy,
            "productive_precision": productive_precision,
            "productive_recall": productive_recall,
            "productive_f1": productive_f1,
            "non_productive_precision": non_productive_precision,
            "non_productive_recall": non_productive_recall,
            "non_productive_f1": non_productive_f1,
            "macro_precision": macro_precision,
            "macro_recall": macro_recall,
            "macro_f1": macro_f1,
            "true_negatives": float(c_matrix[0, 0]),
            "false_positives": float(c_matrix[0, 1]),
            "false_negatives": float(c_matrix[1, 0]),
            "true_positives": float(c_matrix[1, 1]), 
        }

    def _train(self, output_dir: str = "models/email_classifier") -> None:
        if self._tokenizer is None:
            raise ValueError("Tokenizer não foi inicializado. Chame setup_model() primeiro.")
        if self._model is None:
            raise ValueError("Modelo não foi inicializado. Chame setup_model() primeiro.")
        if self._train_dataset is None:
            raise ValueError("Dataset não foi carregado. Chame load_and_prepare_data() primeiro.")
        
        training_args = TrainingArguments(
            output_dir=output_dir,
            num_train_epochs=3,
            eval_strategy="epoch",
            save_strategy="epoch",
            load_best_model_at_end=True,
            logging_steps=50
        )

        trainer = Trainer(
            model=self._model,
            args=training_args,
            train_dataset=self._train_dataset,
            eval_dataset=self._validation_dataset,
            compute_metrics=self._compute_metrics
        )
        self._trainer = trainer

        trainer.train()
        trainer.save_model()
        self._tokenizer.save_pretrained(output_dir)

    def _evaluate_on_test(self) -> Dict[str, float]:
        if self._trainer is None:
            raise ValueError("Modelo não foi treinado. Execute train() primeiro.")
        
        # Avaliar no dataset de teste
        test_results = self._trainer.evaluate(eval_dataset=self._test_dataset)
        
        # Imprimir resultados
        print("📊 Resultados finais no dataset de teste:")
        for metric, value in test_results.items():
            if isinstance(value, float):
                print(f"  {metric}: {value:.4f}")
        
        return test_results

if __name__ == "__main__":
    trainer = EmailClassifierTrainer()
    trainer.run()
    
    print("✅ Modelo e dados carregados com sucesso!")