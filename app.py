import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load('models/spam_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

# App title
st.title("📩 SMS Spam Classifier")

# Input box
msg = st.text_area("Enter your message:")

if st.button("Predict"):
    data = vectorizer.transform([msg])
    result = model.predict(data)[0]

    if result == 1:
        st.error("🚫 Spam")
    else:
        st.success("✅ Not Spam")
