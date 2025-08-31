# Email Classifier AI

Sistema inteligente para classificação automática de emails e geração de respostas contextuais usando machine learning e inteligência artificial.

## Sobre o Projeto

Aplicação que classifica emails como produtivos ou não-produtivos e gera sugestões de resposta usando BERT e Google Gemini.

### Funcionalidades

- Classificação automática de emails
- Geração de respostas com IA
- Interface web responsiva
- API REST documentada
- Pipeline de ML com BERT português

## Tecnologias

- **Backend**: FastAPI, Python 3.12, Uvicorn
- **Machine Learning**: HuggingFace Transformers, BERT, PyTorch
- **IA**: Google Gemini API
- **Frontend**: Jinja2, Bootstrap 5
- **DevOps**: Docker, Docker Compose, Poetry

## Como Executar

### Docker Compose (Recomendado)

### Desenvolvimento Local

**Para Desenvolvimento local** (com hot reload):
```bash
# Instalar dependências (CPU-only)
poetry install

# Ou instalar com suporte GPU (opcional)
poetry install --with gpu

# Treinar modelo (primeira execução)
poetry run python -m trainment.trainer

# Configure as variáveis de ambiente
cp .env.example .env

# Execute em modo desenvolvimento
docker compose up -d app-dev

# Acesse: http://localhost:8000
```

**Para Produção Local** (sem hot reload):
```bash
# Execute em modo produção
docker compose up -d app-prod
```

**Comandos úteis**:
```bash
# Ver logs
docker compose logs -f app-dev

# Parar containers
docker compose down

# Rebuild imagens
docker compose build
```

## Configuração

Variáveis de ambiente necessárias:

```bash
# .env
HUGGING_FACE_TOKEN=your_hf_token_here
GEMINI_API_KEY=your_gemini_api_key_here
DATA_FOLDER=./app/assets/ # onde os dados de treinamento serão salvos
```

## Sistema de Classificação

**Emails Produtivos**: Solicitações urgentes, consultas empresariais, reportes técnicos, pedidos de informação, propostas comerciais, escalações

**Emails Não-Produtivos**: Felicitações, agradecimentos, newsletters, aniversários, conversas casuais, anúncios corporativos

## API

Documentação disponível em `http://localhost:8000/docs`

## Machine Learning

### Treinamento

```bash
# Treinar novo modelo
poetry run python -m trainment.trainer
```

### Pipeline

1. BERT classifica o email
2. Gemini analisa contexto e classificação  
3. Gera explicação e sugestão de resposta
4. Aplica formatação markdown

## Deploy

### Docker Compose
```bash
# Teste produção localmente
docker compose up app-prod
```

### Fly.io
```bash
# Deploy direto (sem hot reload)
fly deploy
```