# 🏥 Medical Chatbot

> An intelligent conversational AI designed to provide insightful, safe, and helpful responses to medical inquiries. Built with cutting-edge language models and vector databases for accurate, context-aware medical guidance.

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

🤖 **AI-Powered Responses** - Leverages advanced language models for accurate medical information  
🔍 **Semantic Search** - Uses vector embeddings to find the most relevant medical documents  
💬 **Interactive Chat** - Clean, intuitive web interface for seamless conversation  
🔐 **Privacy-First** - Secure environment variable configuration for sensitive API keys  
📚 **RAG Architecture** - Retrieval-Augmented Generation for grounded, reliable answers  
🐳 **Docker Ready** - Containerized deployment for easy scaling  
🧩 **Modular Design** - Well-organized code structure for easy extension and maintenance  

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend Framework** | Flask 3.1.1 |
| **LLM Integration** | LangChain 0.3.26 |
| **AI Model** | AI21 Labs (via LangChain) |
| **Vector Database** | Pinecone + LangChain |
| **Embeddings** | Sentence Transformers 4.1.0 |
| **Document Processing** | PyPDF 5.6.1 |
| **Environment Config** | Python-dotenv 1.1.0 |
| **Frontend** | HTML5, CSS3 |
| **Containerization** | Docker |

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10+** - [Download here](https://www.python.org/downloads/)
- **pip** (comes with Python)
- **Git** - For cloning the repository
- **Docker** (optional) - For containerized deployment

### API Keys Required

You'll need accounts and API keys for:
- **Pinecone** - Vector database for semantic search ([Sign up](https://www.pinecone.io/))
- **AI21 Labs** - Language model API ([Sign up](https://www.ai21.com/))

---

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Abdullah-dev2/Medical-Chatbot.git
cd Medical-Chatbot
```

### 2. Create Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```env
PINECONE_API_KEY=your_pinecone_api_key_here
AI21_API_KEY=your_ai21_api_key_here
```

---

## 💻 Usage

### Run Locally
```bash
python app.py
```
Visit [http://16.171.11.135:8080/](http://16.171.11.135:8080/) in your browser

### Run with Docker
```bash
docker build -t medical-chatbot .
docker run -p 8080:8080 --env-file .env medical-chatbot
```

---

## 📂 Project Structure

```
Medical-Chatbot/
├── app.py                      # Main Flask application
├── store_index.py              # Pinecone index management
├── requirements.txt            # Python dependencies
├── setup.py                    # Package configuration
├── Dockerfile                  # Docker container config
├── .env.example                # Environment variables template
├── Data/                       # Medical documents/data
├── src/
│   ├── __init__.py
│   ├── helper.py              # Helper functions (embeddings, etc.)
│   ├── prompt.py              # LLM prompt templates
│   └── __pycache__/
├── templates/
│   └── chat.html              # Chat UI template
├── static/
│   └── style.css              # UI styling
├── research/
│   └── trials.ipynb           # Jupyter notebooks for experiments
└── LICENSE                     # MIT License
```

---

## 📚 Core Dependencies

### Framework & Server
- **Flask 3.1.1** - Lightweight web framework for building the API and serving the UI

### AI & Language Models
- **LangChain 0.3.26** - Framework for building LLM-powered applications
- **LangChain-Community 0.3.26** - Community integrations for LangChain
- **LangChain-AI21 1.2.0** - AI21 Labs integration with LangChain
- **LangChain-Pinecone 0.2.8** - Pinecone vector database integration

### Embeddings & NLP
- **Sentence-Transformers 4.1.0** - State-of-the-art sentence embeddings for semantic search

### Data Processing
- **PyPDF 5.6.1** - Extract text and metadata from PDF medical documents

### Configuration
- **Python-dotenv 1.1.0** - Load environment variables from .env file securely

---

## ⚙️ Configuration

### Environment Variables

```env
# Pinecone Configuration
PINECONE_API_KEY=your_key_here

# AI21 Labs Configuration
AI21_API_KEY=your_key_here

# Optional: Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
```

### Key Application Constants (in app.py)
- `index_name = "medical-chatbot"` - Pinecone index name
- `app.run(host="0.0.0.0", port=8080)` - Server configuration

---

## 🔄 How It Works

1. **User Query** → User sends a medical question through the chat interface
2. **Embedding** → Query is converted to embeddings using Sentence Transformers
3. **Vector Search** → Pinecone retrieves relevant medical documents
4. **Prompt Building** → LangChain constructs a detailed prompt with retrieved context
5. **LLM Response** → AI21 Labs generates a response based on context
6. **Response Delivery** → Answer is streamed back to the user in real-time

---

## 🤝 Contributing

Contributions are welcome and appreciated! Here's how to contribute:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request with a detailed description

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for complete details.

---

## 💡 Tips for Development

- Keep your `.env` file secure and never commit it to version control
- Test with the Jupyter notebook in `research/trials.ipynb` for experimentation
- Use the modular structure in `src/` to extend functionality
- Refer to [LangChain Documentation](https://python.langchain.com/) for advanced features
- Update `requirements.txt` when adding new dependencies: `pip freeze > requirements.txt`

---

**Made with ❤️ for better healthcare through AI**
