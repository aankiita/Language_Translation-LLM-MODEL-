import requests
import streamlit as st

def get_groq_response(input_text, language):
    json_body = {
        "input": {
            "language": language,   
            "text": input_text
        },
        "config": {},
        "kwargs": {}
    }

    response = requests.post(
        "https://language-translation-llm-model.onrender.com/chain/invoke",
        json=json_body
    )

    result = response.json()
    return result.get("output", "No output found")

## Streamlit app
st.title("LLM Language Translator Using LCEL")

# User input
input_text = st.text_input("Enter the text you want to translate")

# Dropdown for language selection
language = st.selectbox(
   "Select target language",
    [
        "French", "Spanish", "German", "Italian", "Portuguese", 
        "Dutch", "Russian", "Japanese", "Chinese", "Korean",
        "Hindi", "Bengali", "Urdu", "Arabic", "Turkish",
        "Swedish", "Norwegian", "Polish", "Greek", "Vietnamese",
        "Thai", "Indonesian"
    ]
)

# Translate on input
if input_text:
    translation = get_groq_response(input_text, language)

    st.write("**Translated Text:**", translation)
