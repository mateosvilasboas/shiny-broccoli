# 🤖 Email Classifier AI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?style=for-the-badge&logo=docker)
![ML](https://img.shields.io/badge/ML-BERT-orange?style=for-the-badge&logo=pytorch)
![AI](https://img.shields.io/badge/AI-Gemini-purple?style=for-the-badge&logo=google)

</div>

## 📖 Sobre o Projeto

Sistema inteligente para **classificação automática de emails** e **geração de respostas contextuais** usando machine learning avançado e inteligência artificial generativa.

### 🎯 Funcionalidades Principais

- ✅ **Classificação Automática**: Categoriza emails como produtivos ou não-produtivos
- ✅ **IA Generativa**: Gera explicações e sugestões de resposta usando Google Gemini
- ✅ **Interface Web**: Dashboard responsivo e intuitivo
- ✅ **API REST**: Endpoints documentados para integração
- ✅ **ML Pipeline**: Treinamento personalizado com BERT português

## 🛠️ Stack Tecnológica

### Backend & API
- **FastAPI** - Framework web moderno e rápido
- **Python 3.12** - Linguagem principal
- **Pydantic** - Validação e serialização de dados
- **Uvicorn** - Servidor ASGI de alta performance

### Machine Learning & AI
- **HuggingFace Transformers** - BERT para classificação
- **neuralmind/bert-base-portuguese-cased** - Modelo base português
- **Google Gemini API** - IA generativa para respostas
- **scikit-learn** - Métricas e avaliação
- **torch** - Framework de deep learning

### Frontend & UI
- **Jinja2** - Template engine
- **Bootstrap 5** - Framework CSS responsivo
- **JavaScript (Vanilla)** - Interatividade dinâmica

### DevOps & Tools
- **Docker & Docker Compose** - Containerização
- **Poetry** - Gerenciamento de dependências

## 🚀 Como Executar

### 🐳 **Opção 1: Docker (Recomendado)**

```bash
# Clone o repositório
git clone <repo-url> ./shiny-broccoli
cd /shiny-broccoli

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o .env com suas API keys

# Execute com Docker
docker-compose up --build

# Treine o modelo quando o container estiver executando (primeira execução)
poetry run python -m trainment.trainer

# Acesse: http://localhost:8000
```

### 💻 **Opção 2: Desenvolvimento Local**

```bash
# Instale as dependências
poetry install

# Configure o ambiente Python
poetry shell

# Treine o modelo (primeira execução)
poetry run python -m trainment.trainer

# Execute a API
poetry run uvicorn app.app:app --reload --host 0.0.0.0 --port 8000

# Acesse: http://localhost:8000
```

### ⚙️ **Configuração das Variáveis de Ambiente**

```bash
# .env
HUGGING_FACE_TOKEN=your_hf_token_here
GEMINI_API_KEY=your_gemini_api_key_here
DATA_FOLDER=./app/assets/
```

## 🧠 Sistema de Classificação

### 📧 **Emails Produtivos**
Requerem ação imediata ou resposta:
- 🚨 Solicitações urgentes de suporte
- ❓ Consultas sobre processos empresariais
- 🐛 Reportes de problemas técnicos
- 📊 Pedidos de relatórios ou informações
- 🤝 Propostas comerciais
- ⚠️ Escalações e reclamações

### 💬 **Emails Não-Produtivos**
Informativos ou sociais:
- 🎉 Mensagens de felicitação
- 🙏 Agradecimentos e reconhecimentos
- 📰 Newsletters e comunicados gerais
- 🎂 Mensagens de aniversário
- ☕ Conversas casuais
- 📢 Anúncios corporativos

## 🌐 API Endpoints

A documentação da API está disponível em `http://localhost:8000/docs`, através do Swagger

## 🏋️ Pipeline de Machine Learning

### 🎯 **Arquitetura do Modelo**

- **Modelo Base**: `neuralmind/bert-base-portuguese-cased`
- **Task**: Classificação binária (productive/non_productive)
- **Fine-tuning**: Transformer com cabeça de classificação
- **Otimizador**: AdamW com learning rate scheduling

### 📊 **Dados e Treinamento**

- **Split**: 70% treino, 15% validação, 15% teste
- **Estratificação**: Mantém proporção balanceada das classes
- **Métricas**: Accuracy, Precision, Recall, F1-score, Confusion Matrix
- **Epochs**: Treinamento com early stopping
- **Batch Size**: Otimizado para performance

### 🔄 **Executar Treinamento**

```bash
# Treinar novo modelo
poetry run python -m trainment.trainer

# O modelo será salvo em: models/email_classifier/
```

### ⚙️ **Como Funciona**

1. **Classificação ML**: BERT classifica o email
2. **Análise IA**: Gemini analisa o contexto e classificação
3. **Geração**: Cria explicação + sugestão de resposta
4. **Formatação**: Aplica markdown para melhor apresentação

## 🎨 Interface de Usuário

### 🖥️ **Dashboard Web**

- **Design Responsivo**: Funciona em desktop, tablet e mobile
- **Interface Intuitiva**: UX otimizada para produtividade
- **Feedback Visual**: Indicadores de loading e status
- **Markdown Rendering**: Formatação rica nas respostas da IA

### 🎯 **Recursos da Interface**

- 📝 Editor de texto com syntax highlighting
- 🚀 Processamento assíncrono com feedback visual
- 📊 Visualização clara da classificação
- 💡 Sugestões de resposta formatadas
- 📱 Design mobile-first

## 🛠️ Desenvolvimento e Testes

### 🧪 **Comandos de Desenvolvimento**

```bash
# Instalar dependências de desenvolvimento
poetry install --with dev

# Executar linting
poetry run ruff check

# Executar formatação
poetry run ruff format

# Executar testes
poetry run pytest -v

# Cobertura de testes
poetry run pytest --cov=app --cov-report=html

# Executar em modo desenvolvimento
poetry run task run
```

### 📦 **Scripts Poetry (taskipy)**

```bash
# Comandos disponíveis via poetry run task <comando>
poetry run task lint       # Verificar código
poetry run task format     # Formatar código
poetry run task test       # Executar testes
poetry run task run        # Executar aplicação
```

## 🚢 Deploy e Produção

### 🐳 **Docker Production**

```dockerfile
# Build para produção
docker build -t email-classifier .

# Run em produção
docker run -p 8000:8000 \
  -e GEMINI_API_KEY=your_key \
  -e HUGGING_FACE_TOKEN=your_token \
  email-classifier
```

### ☁️ **Deploy Platforms**

O projeto está pronto para deploy em:

- **Google Cloud Run** ⭐ (Recomendado - GPU support)
- **Railway** ⭐ (Simples e eficiente)
- **Fly.io** (Volumes persistentes)
- **AWS ECS** (Enterprise)
- **Azure Container Instances**

### 🔧 **Configurações de Produção**

```bash
# Variáveis de ambiente necessárias
GEMINI_API_KEY=your_gemini_api_key
HUGGING_FACE_TOKEN=your_hf_token
DATA_FOLDER=./app/assets/
PORT=8000  # Para Heroku/Railway
```

## 📊 Performance e Métricas

### ⚡ **Performance**

- **API Response Time**: < 2s para classificação
- **ML Inference**: ~500ms para BERT
- **IA Generation**: ~1-3s para Gemini
- **Memory Usage**: ~2GB (com modelo carregado)
- **CPU Usage**: Otimizado para inferência

### 📈 **Monitoramento**

```python
# Logs estruturados (implementar)
import logging
logging.info(f"Classification: {label}, Score: {score}")

# Métricas personalizadas (implementar)
from prometheus_client import Counter
classification_counter = Counter('classifications_total')
```

## 🤝 Contribuição

### 🔄 **Workflow de Contribuição**

1. **Fork** o repositório
2. **Clone** sua fork: `git clone <your-fork>`
3. **Branch**: `git checkout -b feature/nova-funcionalidade`
4. **Commit**: `git commit -m "feat: adiciona nova funcionalidade"`
5. **Push**: `git push origin feature/nova-funcionalidade`
6. **Pull Request** para a branch `main`

### 📋 **Guidelines**

- Seguir padrões de código (ruff/black)
- Adicionar testes para novas funcionalidades
- Documentar mudanças no README
- Usar conventional commits

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Autor

**Mateus Vilas Boas**
- 📧 Email: mateuscamposdantas@gmail.com
- 💼 GitHub: [@mateosvilasboas](https://github.com/mateosvilasboas)
- 🌐 LinkedIn: [Mateus Vilas Boas](https://linkedin.com/in/mateosvilasboas)

---

<div align="center">

**Feito com ❤️ e muita ☕ usando Python, FastAPI e IA**

⭐ **Star este repositório se ele foi útil para você!**

</div>