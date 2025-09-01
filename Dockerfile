FROM python:3.12.3-slim AS builder

ARG ENVIRONMENT=production

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi
# Instalar modelo spaCy para português
# Baixar recursos NLTK
RUN poetry run python -m spacy download pt_core_news_sm
RUN poetry run python -c "import nltk; nltk.download('stopwords'); nltk.download('rslp'); nltk.download('punkt')"

COPY . .

# =====================================================
# STAGE 2: Runtime - Imagem final otimizada
# =====================================================
FROM python:3.12.3-slim AS runtime

# Copiar Python e dependências do builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copiar dados NLTK
COPY --from=builder /root/nltk_data /root/nltk_data

# Variáveis de ambiente para produção
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV HF_HOME=/tmp/hf_cache

WORKDIR /app

# Copiar apenas o código da aplicação
COPY --from=builder /app .

EXPOSE 8000

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
