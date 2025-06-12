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

sms\_spam\_classifier/  
├── app.py  
├── models/  
│ ├── spam\_model.pkl  
│ └── vectorizer.pkl  
├── data/  
│ └── spam.csv  
├── notebooks/  
│ └── spam_detector.ipynb  
├── README.md  
├── requirements.txt


---

## 📷 Screenshot

![App Screenshot](https://github.com/maheshh-v/sms_spam_classifier/blob/2f1c6d0c92fba336a967dfa7d410c09c8bfbaccf/Screenshot%202025-06-12%20155817.png) 

---

##  How to Run Locally

1. Clone the repo  
2. Install requirements: `pip install -r requirements.txt`  
3. Run: `streamlit run app.py`

---

##  Author

Mahesh Vyas – B.Tech CS (AI) – Passionate ML Developer  
