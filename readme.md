# Medical Chatbot

<div align="center">
  <img src="https://img.icons8.com/color/96/robot-2.png" alt="Medical Chatbot Logo" width="100"/>

  <h1>Medical Chatbot</h1>
  <p><em>An AI-powered assistant for safe and informative medical guidance.</em></p>

  <img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg" alt="Python Version"/>
  <img src="https://img.shields.io/badge/Flask-2.x-green.svg" alt="Flask"/>
  <img src="https://img.shields.io/badge/Docker-ready-blue.svg" alt="Docker Ready"/>
</div>

---

<p align="center">
  <img src="https://via.placeholder.com/1200x300?text=Medical+Chatbot+Banner" alt="Medical Chatbot Banner" width="80%"/>
</p>

---

## 🚀 Overview

**Medical Chatbot** is a modern conversational AI web application built using **Flask** and **Python**. It assists users by providing general medical information in a friendly, safe, and accessible manner. Its clean and responsive UI, along with a modular backend design, makes it ideal for research, experimentation, and deployment.

---

## ✨ Features

- 🤖 **Conversational AI** — Natural and safe medical Q&A
- 🖥️ **Modern Web UI** — Clean responsive chat interface
- 🧩 **Modular Architecture** — Easily extend chatbot logic or UI components
- 🐳 **Docker Support** — One-command deployment
- 📚 **Research Ready** — Jupyter notebooks for experimentation

---

## 🗂️ Project Structure

```
Medical-Chatbot/
│
├── app.py                     # Main Flask application
├── Dockerfile                 # Docker image setup
├── requirements.txt           # Python dependencies
├── setup.py                   # Packaging configuration
├── store_index.py             # Indexing / utility script
│
├── Data/                      # Optional dataset directory
├── medibot/                   # Virtual environment (ignored)
├── medical_chatbot.egg-info/  # Package metadata
│
├── research/                  # Jupyter notebooks
├── src/                       # Core chatbot logic
│   ├── helper.py
│   └── prompt.py
│
├── static/                    # CSS and static assets
│   └── style.css
│
└── templates/                 # HTML interface
    └── chat.html
```

---

## ⚡ Quickstart

### **Prerequisites**
- Python **3.8+**
- `pip`
- *(Optional)* Docker

---

## 🛠️ Installation

```sh
git clone https://github.com/yourusername/Medical-Chatbot.git
cd Medical-Chatbot

python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

---

## ▶️ Run the Application

```sh
python app.py
```

Open your browser and visit:
```
http://localhost:5000
```

---

## 🐳 Run with Docker

```sh
docker build -t medical-chatbot .
docker run -p 5000:5000 medical-chatbot
```

---

## 📁 Important Files

| File | Description |
|------|-------------|
| `app.py` | Main Flask backend |
| `templates/chat.html` | Chat interface UI |
| `static/style.css` | Frontend styles |
| `src/helper.py` | Backend utility functions |
| `src/prompt.py` | Prompt templates and NLP logic |
| `research/trials.ipynb` | Jupyter experiments |
| `Dockerfile` | Docker configuration |
| `requirements.txt` | Python dependencies |

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an **issue** or submit a **pull request** for improvements, fixes, or new features.

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

# 🩺 Medical-Chatbot
A lightweight, extensible AI-based medical assistant.

