
🔎 AI Search Assistant (Google-like)
An AI-powered intelligent search assistant that works like Google. Just type your question and get accurate, real-time answers from the internet using AI + Web Search.

🚀 Demo
🖥️ Live Demo: [Add Streamlit Link after Deployment]

📌 Features
🔍 Ask any question like "What's the weather in Mumbai?" or "Latest news on Gaganyaan"

🌐 Real-time web search using DuckDuckGo/SerpAPI

🤖 AI summarization of search results using OpenAI or Mistral LLM

📄 Clean and simple UI with Streamlit

📦 Lightweight and easy to deploy (no backend needed)

🧠 Tech Stack
Tool	Usage
LangChain	RAG (Retrieval Augmented Generation) setup
DuckDuckGo Search / SerpAPI	Web search
OpenRouter (Mistral/OpenAI)	LLM (Language Model) response
Streamlit	Frontend & user interface
Python	Core programming language
.env	Secure API key management

📂 Project Structure

ai-search-assistant/
│
├── app.py                 # Main Streamlit app
├── search_agent.py        # LangChain agent setup (web search + LLM)
├── prompts.py             # Custom prompt template
├── requirements.txt       # All dependencies
└── .env                   # API keys and environment variables
⚙️ Installation & Run Locally

# Clone the repo
git clone https://github.com/ashwanidwivedi356/Assistant-AI
cd ai-search-assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate      # For Windows

# Install dependencies
pip install -r requirements.txt

# Create .env file and add your API keys
touch .env

# Run the app
streamlit run app.py
🔐 .env Example

OPENROUTER_API_KEY=your_openrouter_api_key
📸 Screenshots

🧑‍💻 How It Works
User inputs a query in the Streamlit interface.

Query is sent to DuckDuckGo/SerpAPI to get top 3-5 results.

Results are passed into the LLM (Mistral/OpenAI via OpenRouter).

AI gives a summarized, accurate answer.

Streamlit displays the result beautifully.

🛠️ Future Enhancements
Voice input support 🎤

Save search history 📚

Switch between different LLMs dynamically

Multi-language support 🌍

