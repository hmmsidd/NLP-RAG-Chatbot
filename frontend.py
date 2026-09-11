import streamlit as st
import requests  # Naya Dakiya (API caller)

st.title("Siddharth's AI Chatbot 🤖")
st.write("Mera personal RAG assistant. Pucho jo puchna hai!")

# Tijori setup karna
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Purane messages screen par paint karna
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["text"])

# Niche ka chat box
user_sawal = st.chat_input("Apna sawal yahan likho...")

if user_sawal:
    # 1. User ka message dikhana aur save karna
    with st.chat_message("user"):
        st.write(user_sawal)
    st.session_state.chat_history.append({"role": "user", "text": user_sawal})
    
    # 2. AI ka Real Answer mangwana
    with st.chat_message("assistant"):
        with st.spinner("AI dimaag laga raha hai..."):
            try:
                # Backend ka exact address
                api_url = "http://127.0.0.1:8000/chat"
                
                # Chithi pack karke bhejna
                payload = {"question": user_sawal}
                response = requests.post(api_url, json=payload)
                
                # Backend se aaye hue jawab ko kholna
                if response.status_code == 200:
                    real_answer = response.json()["bot_answer"]
                else:
                    real_answer = "Bhai, backend mein kuch gadbad hai."
                    
            except Exception as e:
                real_answer = "Bhai, API connect nahi ho rahi. Kya FastAPI server chalu hai?"
                
        # Final answer screen par dikhana aur tijori mein save karna
        st.write(real_answer)
    st.session_state.chat_history.append({"role": "assistant", "text": real_answer})