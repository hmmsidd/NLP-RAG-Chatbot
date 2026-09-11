import google.generativeai as genai

# Apni asli API key yahan daalna
genai.configure(api_key="AIzaSyDmeD75JzHcgVeWlU8HKFevDgD4o2glj-o")

print("Google ke server se models dhoondh rahe hain...\n")

# Jadoo: Hum Google se bol rahe hain "Wo models dikhao jo Embeddings support karte hain"
available_models = []
for m in genai.list_models():
    if 'embedContent' in m.supported_generation_methods:
        available_models.append(m.name)

print(f"Google ke paas ye models hain: {available_models}\n")

if len(available_models) > 0:
    # Jo sabse pehla sahi model milega, hum wahi use kar lenge
    best_model = available_models[-1] # -1 matlab sabse latest wala
    print(f"Hum '{best_model}' use karke 'Cricket' word ko numbers mein badal rahe hain...\n")
    
    my_word = "Cricket"
    result = genai.embed_content(
        model=best_model, 
        content=my_word
    )
    
    address_numbers = result['embedding']
    print("Maza aagaya! Ye rahe tere pehle 5 numbers (address):")
    print(address_numbers[:5]) # Pura jaal print nahi kar rahe, sirf pehle 5
    
    print(f"\nTotal numbers in this address (length): {len(address_numbers)}")
else:
    print("Bhai koi model nahi mila. API key check karni padegi.")