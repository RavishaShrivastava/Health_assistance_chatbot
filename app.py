import nltk
import streamlit as st
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize  # Correct import

nltk.download('punkt')  # Download required NLTK data
nltk.download('stopwords')

chatbot = pipeline("text-generation", model="distilgpt2")


def healthcare_chatbot(user_input):
    
    if "symptoms" in user_input:  # Correct spelling
        return "Please consult Doctor for accurate results, As I'm not a doctor, but these symptoms can result from infections or due to climate changes. Other causes include allergies, respiratory issues, or environmental factors. Stay hydrated, get enough rest, and monitor symptoms. Over-the-counter medication may help, but if symptoms persist, worsen, or include breathing difficulties, chest pain, or high fever, consult a doctor immediately. A healthcare professional can provide an accurate diagnosis and recommend appropriate treatment. In the meantime, maintaining good hygiene, eating a balanced diet, and avoiding irritants like smoke can help support recovery."
    elif "medication" in user_input:
        return "Medications help manage various health conditions, from mild illnesses to chronic diseases. Take antibotic medicine.Over-the-counter (OTC) medications can provide relief, but prescription drugs may be needed for specific conditions. It’s essential to follow dosage instructions, avoid self-medication, and consult a doctor for prolonged or severe symptoms. Some medications may have side effects, so monitoring your body’s response is important. A balanced diet, hydration, and rest can also support recovery alongside medication."
    elif "safdf" in user_input:
        return "A healthy diet includes a balanced mix of fruits, vegetables, whole grains, lean proteins, and healthy fats. Staying hydrated, limiting processed foods, and controlling portion sizes help maintain overall well-being. Proper nutrition supports immunity, energy levels, and disease prevention. A well-balanced diet, combined with exercise, promotes long-term health."
    else:
        response = chatbot(user_input, max_length=100, num_return_sequences=1)
        return response[0]['generated_text']  # Correct key

def main():
    st.title("HealthCare Assistant Chatbot")
    user_input = st.text_input("How can I assist you today?")
    if st.button("Submit"):
        if user_input:
            st.write("User:", user_input)
            with st.spinner("Processing your query, Please wait...."):
                response = healthcare_chatbot(user_input)
            st.write("HealthCare Assistant:", response)
        else:
            st.write("Please enter text")

if __name__ == "__main__":
    main()
