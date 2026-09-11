from fastapi import FastAPI
from pydantic import BaseModel
import chromadb
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

app = FastAPI()

# 1. Local ChromaDB se connection
client = chromadb.PersistentClient(path="./my_vector_db")
collection = client.get_collection(name="siddharth_profile")

# 2. Gemini model setup (Apni key yahan replace karna)
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key="YOUR_API_KEY_HERE"
)

# 3. Strict Prompt Template
template = """
Tu ek strict data assistant hai. Sirf is CONTEXT ko padh kar niche diye gaye QUESTION ka jawab de.
Agar jawab CONTEXT mein nahi hai, toh bol de "Mujhe nahi pata". Khud se kahani mat banana.

CONTEXT: {context}
QUESTION: {question}
"""
prompt = PromptTemplate.from_template(template)

# Prompt aur LLM ko chain kiya
rag_chain = prompt | llm | StrOutputParser()

# Request validation
class UserQuery(BaseModel):
    question: str

# 4. Chat Route
@app.post("/chat")
def chat_with_data(data: UserQuery):
    # ChromaDB se match nikalna
    db_results = collection.query(
        query_texts=[data.question],
        n_results=1
    )
    
    # Safe check agar database khali ho
    if not db_results["documents"] or not db_results["documents"][0]:
        return {"status": "Error", "message": "Database mein koi match nahi mila."}
        
    best_context = db_results["documents"][0][0]

    # LangChain run karna
    ai_response = rag_chain.invoke({
        "context": best_context,
        "question": data.question
    })
# Return wale hisse mein .content hata de
    return {
        "status": "Success",
        "your_question": data.question,
        "bot_answer": ai_response  # Yahan se .content hata diya
    }