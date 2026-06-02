from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from medical_data import data, doctors
import sys

# 1. Prepare the Data
X_train = [item["symptoms"] for item in data]
y_train = [item["disease"] for item in data]

# 2. Build the Model
vectorizer = TfidfVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train_vectorized, y_train)

def get_medical_advice(user_symptoms):
    # Check for negations like "no fever", "not cough", "nahe fever"
    negations = ["no", "not", "nahe", "nahi", "nai", "nay"]
    words = user_symptoms.lower().split()
    
    found_negation = False
    for i, word in enumerate(words):
        if word in negations:
            # If a negation is found, we check if it's followed by something that looks like a symptom
            # or if it's just a general "no"
            found_negation = True
            break
            
    if found_negation:
        return "negation_detected"

    user_input_vectorized = vectorizer.transform([user_symptoms])
    predicted_disease = model.predict(user_input_vectorized)[0]
    
    for item in data:
        if item["disease"] == predicted_disease:
            return item

def start_chat():
    print("--- PAKISTANI MEDICAL AI CHATBOT ---")
    print("Disclaimer: Educational purposes only. Always consult a real doctor.")
    print("Type 'exit' to quit.\n")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Bot: Take care! Allah Hafiz.")
            break
            
        if not user_input.strip():
            continue
            
        advice = get_medical_advice(user_input)
        
        if advice == "negation_detected":
            print("\nBot: I noticed you're mentioning what you DON'T have. Please tell me the symptoms you ARE currently experiencing so I can assist you better.\n")
            continue
            
        doctor_name = advice['doctor']
        doctor_desc = doctors[doctor_name]
        
        print(f"\nBot: Based on your symptoms, it sounds like you might have '{advice['disease']}'.")
        print(f"Bot: Recommended Medicine (Pakistani Brands): {advice['medicine']}")
        print(f"Bot: Why? {advice['reason']}")
        print(f"\nBot: [RECOMMENDED DOCTOR]")
        print(f"Bot: Name: Dr. {doctor_name}")
        print(f"Bot: Profile: {doctor_desc}\n")

if __name__ == "__main__":
    start_chat()
