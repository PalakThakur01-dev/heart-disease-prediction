import streamlit as st

st.set_page_config(page_title="About Project", page_icon="📖", layout="wide")

# ---------------- Hero Section ---------------- #
st.title("📖 About Heart Disease Prediction System")

st.markdown("""
The **Heart Disease Prediction System** is an AI-powered Machine Learning application
designed to predict the likelihood of heart disease using medical information.
It provides fast, reliable, and user-friendly predictions through an interactive
Streamlit web application.
""")

st.divider()

# ---------------- Project Overview ---------------- #
st.header("🎯 Project Overview")

st.write("""
Heart disease is one of the leading causes of death worldwide.
This project uses Machine Learning techniques to predict whether a patient
is at risk of heart disease based on important medical parameters.

The objective of this project is to demonstrate the practical application
of Artificial Intelligence in healthcare by providing quick and accurate
predictions that can support early diagnosis.
""")

st.divider()

# ---------------- Key Features ---------------- #
st.header("✨ Key Features")

col1, col2 = st.columns(2)

with col1:
    st.success("🩺 Instant Heart Disease Prediction")
    st.success("📊 Interactive Data Visualization")
    st.success("🤖 Machine Learning Based")
    st.success("⚡ Fast Prediction")

with col2:
    st.success("📈 Model Performance Analysis")
    st.success("📋 User-Friendly Interface")
    st.success("🎯 High Accuracy")
    st.success("💻 Responsive Dashboard")

st.divider()

# ---------------- Technologies ---------------- #
st.header("🛠 Technologies Used")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Programming")
    st.write("""
- Python
- NumPy
- Pandas
""")

with col2:
    st.subheader("Machine Learning")
    st.write("""
- Scikit-Learn
- Random Forest
- Logistic Regression
""")

with col3:
    st.subheader("Visualization & Web")
    st.write("""
- Streamlit
- Matplotlib
- Seaborn
- Joblib
""")

st.divider()

# ---------------- Dataset ---------------- #
st.header("📂 Dataset Information")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Dataset", "Heart Disease")

with c2:
    st.metric("Features", "11+")

with c3:
    st.metric("Target", "Heart Disease")

st.write("""
### Dataset Includes

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
- Target Variable
""")

st.divider()

# ---------------- Workflow ---------------- #
st.header("🔄 Machine Learning Workflow")

st.markdown("""""")

st.divider()

# ---------------- Algorithms ---------------- #
st.header("🤖 Machine Learning Algorithm")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    ### Logistic Regression

    ✔ Supervised Learning Algorithm

    ✔ Binary Classification

    ✔ Used for Heart Disease Prediction

    ✔ Produces 0/1 classification output
    """)

with col2:
    st.success("""
    ### 🎯 Model Used

    **Logistic Regression**

    The model is trained using medical
    features such as Age, Blood Pressure,
    Cholesterol, Chest Pain Type,
    Maximum Heart Rate and other
    clinical parameters.
    """)
st.divider()

# ---------------- Evaluation ---------------- #
st.header("📈 Model Evaluation")

st.write("""
The Logistic Regression model is evaluated using:

- 🎯 Accuracy
- 🎯 Precision
- 🎯 Recall
- 🎯 F1 Score
- 📉 Confusion Matrix
- 📋 Classification Report
""")

st.divider()

# ---------------- Visualizations ---------------- #
st.header("📊 Data Visualizations")

v1, v2 = st.columns(2)

with v1:
    st.write("""
- Age Distribution
- Gender Distribution
- Cholesterol Distribution
- Heart Rate Distribution
""")

with v2:
    st.write("""
- Correlation Heatmap
- Heart Disease Count
- Feature Importance
- Chest Pain Analysis
""")

st.divider()

# ---------------- Prediction Process ---------------- #
st.header("🎯 Prediction Process")

st.markdown("""
1️⃣ User enters medical information.

⬇️

2️⃣ Data is processed and validated.

⬇️

3️⃣ Trained Machine Learning model analyzes the input.

⬇️

4️⃣ Prediction is generated.

⬇️

5️⃣ Result is displayed instantly.
""")

st.divider()

# ---------------- Benefits ---------------- #
st.header("💡 Benefits")

b1, b2 = st.columns(2)

with b1:
    st.success("Early Risk Detection")
    st.success("Easy to Use")
    st.success("Fast Predictions")
    st.success("Educational Purpose")

with b2:
    st.success("Supports Healthcare Awareness")
    st.success("Interactive Dashboard")
    st.success("Reliable ML Prediction")
    st.success("Modern User Interface")

st.divider()

# ---------------- Future ---------------- #
st.header("🚀 Future Improvements")

st.write("""
- User Authentication
- Patient History Database
- PDF Report Generation
- Email Prediction Report
- Doctor Dashboard
- Cloud Deployment
- Mobile Application
- Explainable AI
- AI Health Assistant Chatbot
- Multi-language Support
""")

st.divider()

# ---------------- Developer ---------------- #
st.header("👩‍💻 Developer Information")

left, right = st.columns([1,2])

with left:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=170
    )

with right:

    st.subheader("Palak Salaria")

    st.write("""
**Course:** Bachelor of Computer Applications (BCA)

**Role:** Python & Machine Learning Developer

**Skills**

- Python
- Machine Learning
- Streamlit
- Flask
- HTML
- CSS
- SQL
- Git & GitHub
""")

st.divider()

# ---------------- Libraries ---------------- #
st.header("📚 Libraries Used")

st.code("""
pandas
numpy
matplotlib
seaborn
scikit-learn
streamlit
joblib
""")

st.divider()

# ---------------- Disclaimer ---------------- #
st.header("🔒 Disclaimer")

st.warning("""
This project is developed for educational purposes only.
The prediction generated by this application should not be
considered as professional medical advice.
Always consult a qualified healthcare professional for
proper diagnosis and treatment.
""")

st.divider()

# ---------------- Contact ---------------- #
st.header("📞 Contact")

c1, c2 = st.columns(2)

with c1:
    st.markdown("""
📧 **Email**

your_email@gmail.com
""")

with c2:
    st.markdown("""
💻 **GitHub**

https://github.com/yourusername
""")

st.divider()

# ---------------- Footer ---------------- #
st.markdown(
    """
    <center>
    <h4>❤️ Heart Disease Prediction System</h4>
    <p>Built with Python • Streamlit • Scikit-Learn • Pandas • NumPy • Matplotlib</p>
    <p>© 2026 All Rights Reserved.</p>
    </center>
    """,
    unsafe_allow_html=True
)