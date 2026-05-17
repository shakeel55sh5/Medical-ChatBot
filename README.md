# Medical AI Chatbot (Prototype)

This is a simple AI-powered medical chatbot that predicts potential diseases based on user-described symptoms and recommends medicines with explanations.

## Features
- **Symptom Analysis**: Uses a Random Forest Classifier to identify diseases.
- **Natural Language Processing**: Employs TF-IDF Vectorization to understand text input.
- **Detailed Recommendations**: Provides the name of the medicine and the scientific reason for its use.

## Project Structure
- `medical_bot.py`: The main chatbot application script.
- `medical_data.py`: The knowledge base containing symptoms, diseases, and medicines.
- `project_log.txt`: A step-by-step log of the commands used to build this project.

## How to Run
To start the chatbot, use the following command:
```bash
./my_ai_env/bin/python3 medical_chatbot/medical_bot.py
```

## Disclaimer
**Important**: This project is for educational purposes only. The AI model is a prototype and should not be used for real medical diagnosis. Always consult a professional healthcare provider.
