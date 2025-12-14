````markdown
# 🤖 AI Chatbot Management System

A lightweight, intelligent task management and chatbot system powered by **Python (Flask)** and **Google Gemini AI**. 

This project demonstrates how to build a management console where an AI agent can organize tasks, research topics automatically, and change its personality instantly via "Training Mode."

![Project Status](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![AI](https://img.shields.io/badge/AI-Google%20Gemini-orange)

## ✨ Features

* **🧠 Smart Task Management:** Add, delete, and mark tasks as done using natural language.
* **🎭 Training Mode:** Instantly change the chatbot's personality (e.g., "Train: You are a pirate").
* **💡 Auto-Research Notes:** Ask the bot to "Save a note about [Topic]," and it will research the topic and save a summary automatically.
* **🔒 Secure:** Uses `.env` for safe API key management.
* **⚡ Lightweight:** No database required (uses session-based memory).
* **🎨 Modern UI:** Clean, responsive interface built with HTML/CSS/JS.

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **AI Engine:** Google Gemini (via `google-generativeai` library)
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Environment:** `python-dotenv`

## 📂 Project Structure

```text
ai_assistant/
│
├── .env                 # API Key (Not uploaded to GitHub)
├── app.py               # Main Python Application
├── requirements.txt     # List of dependencies
├── README.md            # Project Documentation
└── templates/
    └── index.html       # User Interface
````

## 🚀 Installation & Setup

### 1\. Clone the Repository

```bash
git clone [https://github.com/your-username/ai-chatbot-manager.git](https://github.com/your-username/ai-chatbot-manager.git)
cd ai-chatbot-manager
```

### 2\. Install Dependencies

```bash
pip install flask google-generativeai python-dotenv
```

### 3\. Configure API Key

Create a file named `.env` in the root directory and add your Google Gemini API key:

```ini
GOOGLE_API_KEY=your_actual_api_key_here
```

> **Note:** You can get a free API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 4\. Run the Application

```bash
python app.py
```

### 5\. Open in Browser

Visit `http://127.0.0.1:5000` in your web browser.

## 📖 Usage Guide

Once the app is running, try these commands in the chat window:

| Action | Example Command | What happens? |
| :--- | :--- | :--- |
| **Add Task** | "Remind me to buy milk" | Adds "Buy milk" to the list. |
| **Research Note** | "Save a note about Elon Musk" | AI researches Elon Musk and saves a summary note. |
| **Train Bot** | "Train: You are a grumpy cat" | The bot's personality changes immediately. |
| **Mark Done** | "Mark milk as done" | Crosses out the task in the list. |
| **Chat** | "What is the capital of France?" | Normal conversation with the bot. |

## 🛡️ Security Note

The `.env` file is included in `.gitignore` to prevent your API key from being accidentally uploaded to GitHub. Never share your API key publicly.

## 🤝 Contributing

Contributions are welcome\! Please feel free to submit a Pull Request.

1.  Fork the project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request
