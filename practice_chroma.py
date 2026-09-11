import chromadb

# Concept 1: Database Engine Start Karna
# PersistentClient ka matlab hai ki data delete nahi hoga, tere laptop par ek naye folder 'my_vector_db' mein save ho jayega.
client = chromadb.PersistentClient(path="./my_vector_db")

# Concept 2: Collection (Table) Banana
# Hum 'siddharth_profile' naam ki table bana rahe hain. 
collection = client.get_or_create_collection(name="siddharth_profile")

# Concept 3: Humara Chunked Data
my_chunks = [
    "Siddharth is studying Food Technology at Jadavpur University.",
    "Siddharth is building a voice-controlled laptop automation system using Python.",
    "Siddharth loves to play cricket with his friends when he goes home."
]

# Har chunk (paragraph) ki ek unique ID honi chahiye, taki kal ko delete ya update karna ho toh asaan rahe.
chunk_ids = ["chunk1", "chunk2", "chunk3"]

print("Data ko Vector Database mein daal rahe hain (Ingesting)...")

# Concept 4: Data ko DB ke andar push (add) karna
collection.add(
    documents=my_chunks,
    ids=chunk_ids
)

print("Success! Data successfully Vector Database mein save ho gaya hai.")