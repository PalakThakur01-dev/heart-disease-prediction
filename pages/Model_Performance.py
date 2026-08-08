import streamlit as st
import joblib
import pandas as pd
import numpy as np


# ==========================================
# Load Saved Files
# ==========================================

metrics = joblib.load(
    "D:/heart_disease_prediction/HeartDisease_metrics.joblib"
)

cm = joblib.load(
    "D:/heart_disease_prediction/confusion_matrix.joblib"
)

report = joblib.load(
    "D:/heart_disease_prediction/classification_report.joblib"
)


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)


# ==========================================
# Title
# ==========================================

st.title("📈 Model Performance")

st.write(
    "Performance evaluation of the Logistic Regression model."
)

st.divider()


# ==========================================
# Performance Cards
# ==========================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    with st.container(border=True):

        st.metric(
            label="🎯 Accuracy",
            value=f"{metrics['Accuracy'] * 100:.2f}%"
        )


with col2:

    with st.container(border=True):

        st.metric(
            label="🎯 Precision",
            value=f"{metrics['Precision'] * 100:.2f}%"
        )


with col3:

    with st.container(border=True):

        st.metric(
            label="🎯 Recall",
            value=f"{metrics['Recall'] * 100:.2f}%"
        )


with col4:

    with st.container(border=True):

        st.metric(
            label="🎯 F1 Score",
            value=f"{metrics['F1 Score'] * 100:.2f}%"
        )


st.divider()


# ==========================================
# Confusion Matrix
# ==========================================

with st.container(border=True):

    st.subheader("📉 Confusion Matrix")

    st.caption(
        "Shows the actual and predicted classification results."
    )

    cm_df = pd.DataFrame(
        cm,
        index=["Actual Low Risk", "Actual High Risk"],
        columns=["Predicted Low Risk", "Predicted High Risk"]
    )

    st.dataframe(
        cm_df,
        use_container_width=True
    )


st.divider()


# ==========================================
# Classification Report
# ==========================================

with st.container(border=True):

    st.subheader("📋 Classification Report")

    st.caption(
        "Precision, Recall, F1-score and Support for each class."
    )

    report_df = pd.DataFrame(
        classification_report_to_dict := {}
    )

    # Convert saved text report into display text
    st.code(
        report,
        language="text"
    )


st.divider()


# ==========================================
# Model Interpretation
# ==========================================

with st.container(border=True):

    st.subheader("🧠 Model Interpretation")

    st.markdown("""
    ### 🎯 Accuracy
    Measures the overall percentage of correct predictions.

    ### 🎯 Precision
    Measures how many predicted positive cases were actually positive.

    ### 🎯 Recall
    Measures how many actual positive cases were correctly identified.

    ### 🎯 F1 Score
    Provides a balance between Precision and Recall.

    ### 📉 Confusion Matrix
    Shows the number of correct and incorrect predictions
    for each class.
    """)


st.divider()


# ==========================================
# Model Workflow
# ==========================================

with st.container(border=True):

    st.subheader("🚀 Model Workflow")

    st.markdown("""
    📂 Dataset

    ↓

    🧹 Data Cleaning

    ↓

    🔤 Label Encoding

    ↓

    ✂️ Train-Test Split

    ↓

    🤖 Logistic Regression

    ↓

    🔮 Prediction

    ↓

    📊 Performance Evaluation

    ↓

    💾 Model Saved using Joblib
    """)


st.divider()


# ==========================================
# Model Summary
# ==========================================

with st.container(border=True):

    st.subheader("📌 Model Summary")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        ### 🤖 Algorithm

        **Logistic Regression**

        ### 🎯 Problem Type

        **Binary Classification**

        ### 🎯 Target Variable

        **HeartDisease**
        """)

    with col2:

        st.markdown("""
        ### 📊 Evaluation Metrics

        ✔ Accuracy  
        ✔ Precision  
        ✔ Recall  
        ✔ F1 Score  
        ✔ Confusion Matrix  
        ✔ Classification Report

        ### 🚀 Deployment

        Streamlit + Joblib
        """)