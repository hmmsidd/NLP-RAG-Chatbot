#  NLP-Based RAG Engine for Unstructured Data

An Enterprise-grade Full-Stack Retrieval-Augmented Generation (RAG) pipeline designed to extract, summarize, and retrieve highly accurate insights from unstructured text data while eliminating AI hallucinations.

##  Key Features
- **Semantic Search:** Converts unstructured text into high-dimensional vector embeddings for rapid and accurate similarity matching.
- **Zero Hallucination (Data Reliability):** Strict Prompt Engineering via LangChain (LCEL) ensures the LLM answers *strictly* from the provided context. 
- **Decoupled Architecture:** A lightweight interactive Streamlit frontend communicating with a high-performance FastAPI backend via RESTful APIs.
- **Session State Management:** Retains chat history for a seamless conversational experience.

##  Tech Stack (Data & ML Focused)
* **LLM:** Google Gemini 3.6 Flash API
* **Orchestration:** LangChain (Prompt Templates, Output Parsers)
* **Vector Database:** ChromaDB (Local Persistent Storage)
* **Backend:** FastAPI, Pydantic, Uvicorn
* **Frontend:** Streamlit, Requests

##  System Architecture & Data Flow

1. **User Query:** The user inputs a question via the **Streamlit UI**.
2. **API Call:** The frontend sends a JSON payload via an HTTP POST request to the **FastAPI Backend**.
3. **Semantic Retrieval:** The backend queries **ChromaDB** using the input text to fetch the most semantically relevant text chunks (Context).
4. **Prompt Engineering:** **LangChain** merges the retrieved Context and User Query into a strict prompt template.
5. **LLM Generation:** The **Gemini LLM** processes the prompt and generates a grounded response.
6. **Clean Output:** `StrOutputParser` sanitizes the response and sends it back through the API to the UI.

##  Local Setup & Installation

### 1. Clone the repository
```bash
git clone [https://github.com/YourUsername/NLP-RAG-Chatbot.git](https://github.com/YourUsername/NLP-RAG-Chatbot.git)
cd NLP-RAG-Chatbot

python -m venv env
# On Windows
env\Scripts\activate
# On Mac/Linux
source env/bin/activate

pip install fastapi uvicorn chromadb langchain langchain-google-genai streamlit requests pydantic

google_api_key="YOUR_GEMINI_API_KEY_HERE"

uvicorn main:app --reload

streamlit run frontend.py
