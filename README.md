# 🫀 Heart Disease Prediction System

An AI-powered Heart Disease Prediction web application built using Python, Machine Learning, and Streamlit.

The system uses a Logistic Regression model to predict the risk of heart disease based on various medical parameters.

---

## 🚀 Live Demo

Coming Soon...

---

## 📌 Project Overview

Heart Disease Prediction System is a Machine Learning based web application that analyzes important medical parameters and predicts whether a patient is at low risk or high risk of heart disease.

The application is designed for educational and portfolio purposes and demonstrates a complete end-to-end Machine Learning workflow.

> ⚠️ This project is for educational purposes only and should not be used as a substitute for professional medical diagnosis.

---

## ✨ Features

- 🫀 Heart Disease Risk Prediction
- 🤖 Logistic Regression Machine Learning Model
- 📊 Model Performance Dashboard
- 📈 Accuracy, Precision, Recall and F1 Score
- 🎯 Confusion Matrix
- 📋 Classification Report
- 📜 Prediction History
- ⚡ Real-time Prediction
- 🎨 Interactive Streamlit Interface
- 💾 Joblib Model & Encoder Storage

---

## 🧠 Machine Learning

### Algorithm

Logistic Regression

### Dataset

The project uses a heart disease dataset containing 300 patient records.

### Features

The model uses the following features:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise Induced Angina
- Oldpeak
- ST Slope

### Target

`HeartDisease`

Where:

- `0` = No Heart Disease
- `1` = Heart Disease

---

## 📊 Model Performance

The trained Logistic Regression model achieved approximately:

| Metric | Score |
|---|---:|
| Accuracy | 78.33% |
| Precision | 78.26% |
| Recall | 92.31% |
| F1 Score | 84.71% |

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib
- Streamlit

---

## 📂 Project Structure

```text
heart_disease_prediction/
│
├── dataset/
│   └── heart_disease_prediction_300.csv
│
├── images/
│   └── hero_banner_img/
│
├── pages/
│   ├── prediction.py
│   ├── visualization.py
│   └── about.py
│
├── main.py
├── train.py
├── HeartDisease_model.joblib
├── HeartDisease_encoders.joblib
├── HeartDisease_metrics.joblib
├── confusion_matrix.joblib
├── classification_report.joblib
├── requirements.txt
├── .gitignore
└── README.md