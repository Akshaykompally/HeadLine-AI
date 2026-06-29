# 📰 AI News Summarizer

An AI-powered news summarization application that retrieves the latest news articles based on a user query and generates concise, easy-to-read summaries using **Mistral AI**, **LangChain**, **Tavily Search**, and **Streamlit**.

The application combines real-time web search with Large Language Models (LLMs) to help users quickly understand current events without reading lengthy articles.

---

## 📌 Overview

AI News Summarizer allows users to search for the latest news on any topic and receive an AI-generated summary in seconds.

The application:

* Retrieves real-time news using the Tavily Search API.
* Processes search results with LangChain.
* Generates concise summaries using Mistral AI.
* Displays both the summarized content and raw search results in an interactive Streamlit interface.

---

## ✨ Features

* 🔍 Search news by any topic
* 📰 Real-time news retrieval
* 🤖 AI-powered news summarization
* 📄 Bullet-point summaries for easy reading
* ⚡ Fast and responsive Streamlit interface
* 📊 View raw search results
* 🔒 Secure API key management using environment variables

---

## 🛠️ Tech Stack

| Category              | Technology    |
| --------------------- | ------------- |
| Frontend              | Streamlit     |
| Programming Language  | Python        |
| LLM Framework         | LangChain     |
| Large Language Model  | Mistral AI    |
| Search API            | Tavily Search |
| Environment Variables | Python Dotenv |

---

## 📂 Project Structure

```text
AI-News-Summarizer/
│
├── main.py
├── requirements.txt
├── summarize.py
├── .gitignore
├── .env                
└── assets/            
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-News-Summarizer.git
```

```bash
cd AI-News-Summarizer
```

---

### Create a Virtual Environment

Using Python

```bash
python -m venv .venv
```

or using uv

```bash
uv venv .venv
```

---

### Activate the Virtual Environment

**Windows (PowerShell)**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt)**

```cmd
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
uv pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

> **Important:** Never upload your `.env` file to GitHub.

---

## ▶️ Running the Application

```bash
streamlit run main.py
```

or

```bash
python -m streamlit run main.py
```

The application will be available at:

```
http://localhost:8501
```

---

## 🔄 Application Workflow

```
User enters a topic
          │
          ▼
Tavily Search API
          │
          ▼
Latest News Articles
          │
          ▼
LangChain Prompt
          │
          ▼
Mistral AI
          │
          ▼
Summarized News
          │
          ▼
Streamlit Interface
```

---

## 📦 Dependencies

* Streamlit
* LangChain
* LangChain Core
* LangChain MistralAI
* LangChain Tavily
* Python Dotenv

---

## 📸 Application Preview

### Home Screen

* Enter a news topic.
* Click **Summarize News**.
* View AI-generated summaries instantly.

### Output

The application displays:

* AI-generated summary
* Raw search results
* Latest news information

---

## 🚀 Future Enhancements

* Multi-language summarization
* News categorization
* Sentiment analysis
* Save summary history
* PDF export
* Email summaries
* Voice summaries
* Trending news dashboard
* Source citations with clickable links

---

## 👨‍💻 Author

**Akshay Kompally**

Computer Science Student | AI & Full-Stack Developer

GitHub: https://github.com/Akshaykompally

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful:

* ⭐ Star this repository
* 🍴 Fork the repository
* 💡 Share feedback and suggestions

Your support helps improve the project and motivates future development.
