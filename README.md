# 🧠 AI-Powered CV Generator

The AI-Powered CV Generator is a web application built using Flask and integrated with Meta's LLaMA 3 model via a custom OpenAI-compatible API. It enables users to input personal and professional information and instantly receive a professionally formatted CV tailored to their provided details.

## 🚀 Features

- 📄 Generates a clean, concise, human-readable CV
- 🤖 Integrated with Meta's LLaMA 3 model
- 🎨 Dark-themed, responsive layout
- ⚡ Instant result display with proper formatting
- 💬 Customized prompts for role-specific summaries

## 🛠️ Built With

- Python (Flask)
- OpenAI API (chat.completions)
- HTML, CSS (custom styled)
- `dotenv` for secure API key management


## ⚙️ Setup Instructions

### 1. Clone the repository

git clone https://github.com/your-username/cv-generator.git
cd cv-generator

### 2. Install dependencies

pip install -r requirements.txt

### 3 .env Configuration
Update your .env file like this:

API_KEY=your_llama3_api_key
MODEL_NAME=llama3-8b-chat
BASE_URL=https://your-llama3-provider.com/v1

Replace your_llama3_api_key and BASE_URL with the credentials provided by your LLaMA 3 provider (e.g., Together AI, Groq, Replicate, etc.).

### 4. Run the app

python app.py

## 🔮 Future Enhancements
✅ PDF download functionality

✅ Editable resume preview

✅ Save and retrieve previous CVs

✅ Support for multiple languages

