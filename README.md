
<div align="center">
	<img src="https://img.icons8.com/color/96/000000/robot-2.png" alt="Medical Chatbot Logo" width="100"/>
	<h1>Medical Chatbot</h1>
	<p><em>Your AI-powered assistant for medical queries and health information.</em></p>

## 🚀 Overview

Medical Chatbot is a modern conversational AI web app designed to provide safe, informative, and friendly responses to health-related questions. Built with Flask and Python, it features a clean chat interface and is easily extensible for research or production use.

---

## ✨ Features

- 🤖 **Conversational AI**: Natural language chat for medical Q&A
- 🖥️ **Modern Web UI**: Responsive chat interface (HTML/CSS)
- 🧩 **Modular Design**: Easy to extend and customize
- 🐳 **Docker Support**: One-command deployment
- 📝 **Research Ready**: Jupyter notebooks for experiments

---

## 🗂️ Project Structure

```text
app.py                  # Main Flask application
Dockerfile              # Docker container configuration
requirements.txt        # Python dependencies
setup.py                # Package setup
store_index.py          # Indexing utility
Data/                   # Data files (if any)
medibot/                # Python virtual environment (do not edit)
medical_chatbot.egg-info/ # Package metadata
research/               # Research notebooks and experiments
src/                    # Source code (helper functions, prompts)
static/                 # Static files (CSS)
templates/              # HTML templates
```

---

## ⚡ Quickstart

### Prerequisites
- Python 3.8+
- pip
- (Optional) Docker

### Installation
```sh
git clone https://github.com/yourusername/Medical-Chatbot.git
cd Medical-Chatbot
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
pip install -r requirements.txt
```

### Run the App
```sh
python app.py
# Visit http://localhost:5000 in your browser
```

### Run with Docker
```sh
docker build -t medical-chatbot .
docker run -p 5000:5000 medical-chatbot
```

---

## 📁 Key Files

- **app.py**: Main Flask server
- **src/helper.py**: Chatbot logic utilities
- **src/prompt.py**: Prompt templates and NLP logic
- **templates/chat.html**: Chat UI
- **static/style.css**: UI styles
- **requirements.txt**: Python dependencies
- **Dockerfile**: Containerization
- **research/trials.ipynb**: Experiments & research

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or pull request for suggestions, improvements, or bug fixes.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

# Medical-Chatbot
