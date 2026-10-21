import streamlit as st

st.set_page_config(
    page_title='heartdisease_prediction',
    page_icon="🫀",
    layout="wide"
)

col1,col2,col3 = st.columns([3,1,1])
with col1:
    st.title("🫀 Heart Disease Prediction System")
    st.subheader("AI-Powered Early Risk Detection using Machine Learning")
    st.subheader("📌 Project Overview")
    st.markdown(''' 
    <p>Heart Disease Prediction System is an AI-powered web application that predicts the likelihood of heart disease using a trained Machine Learning model. The application analyzes important medical parameters such as age, blood pressure, cholesterol level, chest pain type, heart rate, and other clinical features to provide an instant prediction. This project is designed to assist in early risk assessment and demonstrate how Machine Learning can support healthcare decision-making. It is intended for educational and learning purposes and should not replace professional medical diagnosis.</p> 
    ''',unsafe_allow_html=True)
           
    st.subheader("✨ Key Features")
    st.markdown("""
- ❤️ Predicts the risk of heart disease instantly.
- 🤖 Powered by a trained Logistic Regression model.
- 📊 Uses multiple medical features for prediction.
- ⚡ Fast and user-friendly interface.
- 💾 Machine Learning model saved using Joblib.
- 📈 Displays prediction results in real time.
- 🧠 Suitable for educational and portfolio projects.
""")
with col2:
    st.image("images/hero_banner_img/hero_banner1.jpg",width=450)
    st.image("images/hero_banner_img/heart.jpg", width=450)
with col3:
    st.image("images/hero_banner_img/hero_banner2.jpg",width=450)
    st.image("images/hero_banner_img/hero_banner3.jpg",width=450)

st.subheader("⚙️ How It Works")
st.markdown('''
- Enter the patient's medical information.
- Provide details such as age, gender, blood pressure, cholesterol, chest pain type, heart rate, and other health parameters.
- Click the Predict button.
- The trained Logistic Regression model processes the input data.
- The system instantly predicts whether the patient is at Low Risk or High Risk of heart disease.
    ''')

st.subheader("🚀 Why Use This Project?")
st.markdown("""
- 🫀 Encourages awareness of heart disease risk factors.
- ⚡ Provides instant prediction using Machine Learning.
- 📚 Demonstrates a complete end-to-end ML workflow.
- 💻 Ideal for students, beginners, and portfolio projects.
- 📈 Helps understand the practical use of Logistic Regression.
- 🎯 Easy to use with a simple and interactive interface.
""")

st.subheader("👨‍💻 Developed By")
st.markdown("""
Palak Salaria

- 🎓 Bachelor of Computer Applications (BCA)
- 💻 Python Developer
- 🤖 Machine Learning Enthusiast
- 🌐 Streamlit & Flask Developer
- 🚀 Passionate about building real-world AI and ML applications
""")

st.divider()
st.subheader("❤️ Footer")
st.markdown("""
🫀 Heart Disease Prediction System

Made with ❤️ using Python, Scikit-learn, Pandas, NumPy, and Streamlit.

© 2026 Palak Salaria | All Rights Reserved
""")