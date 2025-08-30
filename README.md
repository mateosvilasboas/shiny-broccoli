# Email Classifier

Sistema para classificação automática de emails em **Produtivos** ou **Não-Produtivos** usando machine learning.

## Objetivo

Automatizar a triagem de emails categorizando-os conforme necessidade de ação, utilizando modelo BERT treinado especificamente para português.

## Tecnologias

- **Backend:** FastAPI, Python 3.12
- **ML:** HuggingFace Transformers (BERT português)
- **Avaliação:** scikit-learn
- **Containerização:** Docker
- **Dependências:** Poetry

## Estrutura

```
autou/
├── app/                    # API FastAPI
│   ├── app.py             # Endpoints principais
│   ├── classifier.py      # Classificador de emails
│   └── schemas.py         # Modelos Pydantic
├── trainment/             # Pipeline de treinamento
│   ├── trainer.py         # Classe principal de treinamento
│   └── data.py           # Geração de datasets
├── utils.py              # Templates de emails
└── models/               # Modelos treinados
```

## Como Executar

### Com Docker
```bash
docker-compose up --build
```

### Desenvolvimento Local
```bash
poetry install
poetry run python -m trainment.trainer  # Treinar modelo
poetry run uvicorn app.app:app --reload  # API
```

## Classificação

### Produtivo
Emails que requerem ação:
- Solicitações de suporte
- Consultas sobre processos
- Reportes de problemas
- Solicitações urgentes

### Não-Produtivo
Emails informativos:
- Felicitações
- Agradecimentos
- Mensagens sociais

## API Endpoints

- `POST /classify` - Classificar email usando modelo treinado
- `GET /` - Status da aplicação

Documentação completa: `http://localhost:8000/docs`

### Schema da API

**Input:**
```json
{
  "text": "string"
}
```

**Output:**
```json
{
  "text": "string",
  "label": "productive | non_productive",
  "score": "float (0.0 - 1.0)"
}
```

## Treinamento

O modelo utiliza:
- **Modelo base:** neuralmind/bert-base-portuguese-cased
- **Split:** 70% treino, 15% validação, 15% teste
- **Métricas:** Accuracy, Precision, Recall, F1-score
- **Estratificação:** Mantém proporção das classes

### Executar Treinamento
```bash
python -m trainment.trainer
```

## Exemplo de Uso

```bash
curl -X POST "http://localhost:8000/classify" \
     -H "Content-Type: application/json" \
     -d '{"text": "Preciso do relatório mensal urgente"}'
```

Resposta:
```json
{
  "text": "Preciso do relatório mensal urgente",
  "label": "productive",
  "score": 0.89
}
```

## Desenvolvimento

```bash
poetry run python -m pytest    # Testes
poetry run black .             # Formatação
poetry run flake8 .            # Linting
```