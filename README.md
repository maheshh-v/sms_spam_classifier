# 📩 SMS Spam Classifier (NLP + Streamlit)

A simple NLP project that classifies SMS messages as **Spam** or **Not Spam** using machine learning and text processing.

---

##  Problem Statement

SMS spam is a common issue in communication. The goal is to build a model that can accurately detect spam messages based on text patterns.

---

##  Model & Tools Used

- **Multinomial Naive Bayes**
- **CountVectorizer** (for text feature extraction)
- **Pandas, NumPy** (data handling)
- **Scikit-learn** (model training + evaluation)
- **Streamlit** (for live app deployment)

---

## Dataset

- [Kaggle SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- 5,572 SMS messages labeled as "spam" or "ham"

---

##  Project Highlights

- Cleaned and preprocessed text data  
- Transformed messages into numerical features using `CountVectorizer`  
- Achieved **97% accuracy** using `MultinomialNB` model  
- Built a simple **Streamlit web app** for real-time message prediction

---

## 🖥️ Live App

- [Try the Live Demo Here](https://maheshh-v-sms-spam-classifier-app-ohdkro.streamlit.app/)

---

## 📁 Folder Structure

sms_spam_classifier/
├── app.py
├── models/
│ ├── spam_model.pkl
│ └── vectorizer.pkl
├── data/
│ └── spam.csv
├── notebooks/
│ └── eda.ipynb
├── README.md
├── requirements.txt



---

## 📷 Screenshot

![App Screenshot](Screenshot 2025-06-12 155817.png) 

---

##  How to Run Locally

1. Clone the repo  
2. Install requirements: `pip install -r requirements.txt`  
3. Run: `streamlit run app.py`

---

##  Author

Mahesh Vyas – B.Tech CS (AI) – Passionate ML Developer  
