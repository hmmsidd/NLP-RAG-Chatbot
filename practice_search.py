import chromadb

# Concept 1: Purane database se wapas connect karna
# Hum wahi folder use kar rahe hain jo pichle step mein banaya tha
client = chromadb.PersistentClient(path="./my_vector_db")

# Concept 2: Apni banayi hui collection (table) ko open karna
collection = client.get_collection(name="siddharth_profile")

# Concept 3: User ka sawal (Note kar, main exact keywords use nahi kar raha)
user_question = "Which game does he play?"
print(f"User Question: {user_question}\n")

# Concept 4: Semantic Search lagana!
# n_results=1 ka matlab hai mujhe sirf 1 sabse best matching answer chahiye
results = collection.query(
    query_texts=[user_question],
    n_results=1
)

# Concept 5: Result ko nikalna aur print karna
# ChromaDB result ek dictionary (JSON) mein deta hai, hum usme se 'documents' nikal rahe hain
best_match = results['documents'][0][0]

print("Database se nikaala gaya best answer (Context):")
print(f"-> {best_match}")