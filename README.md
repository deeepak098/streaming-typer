# ⚡ Streaming Typer

A real-time AI text streaming application built with **Python**, **Streamlit**, and the **Groq API**. Instead of waiting for the complete response, the application displays the AI's output token by token, creating a smooth, ChatGPT-like typing experience.

---

## 🚀 Features

* ⚡ Real-time token streaming
* 🤖 Powered by the Groq API
* 💬 ChatGPT-style chat interface
* 📝 Conversation history
* 🎛️ Adjustable temperature
* 🧠 Model selection
* 📊 Response statistics

  * Character count
  * Word count
  * Generation time
* 📋 Copy generated response
* 🗑️ Clear chat functionality
* 🌙 Modern dark-themed UI
* ⚠️ Error handling for API failures

---

## 📸 Preview

> A responsive AI chat interface that streams text live, similar to ChatGPT.

---

## 🏗️ Project Structure

```text
streaming-typer/
│
├── app.py              # Streamlit frontend
├── streamer.py         # Groq streaming backend
├── .env                # API key (not committed)
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Groq API
* python-dotenv

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/streaming-typer.git
cd streaming-typer
```

### 2. Create a virtual environment

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
```

---

### 5. Run the application

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. The user enters a prompt.
2. The Streamlit frontend sends the prompt to the backend.
3. The backend calls the Groq Chat Completions API with `stream=True`.
4. Groq returns the response as a stream of text chunks.
5. Each chunk is immediately displayed in the UI.
6. Statistics such as response time, word count, and character count are shown after generation.

---

## 🔄 Application Workflow

```text
User Prompt
      │
      ▼
Streamlit Frontend
      │
      ▼
stream_response()
      │
      ▼
Groq API
(stream=True)
      │
      ▼
Token Stream
      │
      ▼
Live UI Updates
      │
      ▼
Final Response + Statistics
```

---

## 📚 Key Concepts Learned

This project demonstrates several important AI engineering concepts:

* Streaming API responses
* HTTP streaming
* Python generators (`yield`)
* Iterators
* Environment variables
* Streamlit state management
* Real-time UI rendering
* Incremental text updates
* Error handling
* Modular application design

---

## 🎯 Learning Outcomes

By building this project, you gain hands-on experience with:

* Building responsive AI applications
* Understanding why streaming improves user experience
* Working with Groq's streaming API
* Separating frontend and backend logic
* Creating modern interactive Streamlit interfaces

---

## 🚀 Future Improvements

* Markdown rendering
* Syntax highlighting for code blocks
* Export conversations
* Multiple chat sessions
* Theme switcher
* Speech-to-text input
* Text-to-speech output
* Streaming speed indicator
* Token usage tracking
* Chat history persistence

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository, open an issue, or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Deepak Saladi**

Built as part of a hands-on AI engineering learning journey using Python, Streamlit, and the Groq API.
