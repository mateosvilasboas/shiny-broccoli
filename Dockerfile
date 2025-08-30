FROM python:3.12.3-slim
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

# Instalar Poetry
RUN pip install poetry

# Copiar arquivos de dependências primeiro (para cache)
COPY pyproject.toml poetry.lock ./

# Instalar dependências
RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi

# Copiar código da aplicação (models/ está no .dockerignore)
COPY . .

# Configurações de otimização para produção
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV HF_HOME=/tmp/hf_cache

EXPOSE 8000

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
