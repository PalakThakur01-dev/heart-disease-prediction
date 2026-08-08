import streamlit as st
import joblib
import pandas as pd
import os

# =========================================================
# 1. Load Model
# =========================================================

model = joblib.load(
    "HeartDisease_model.joblib"
)

# =========================================================
# 2. Load Encoders
# =========================================================

encoders = joblib.load(
    "HeartDisease_encoders.joblib"
)

# =========================================================
# 3. Prediction History File
# =========================================================

history_file = "prediction_history.csv"

# =========================================================
# 4. Page Configuration
# =========================================================

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="🩺",
    layout="wide"
)

# =========================================================
# 5. Page Title
# =========================================================

st.title("🩺 Heart Disease Prediction")
st.subheader("Enter Patient Details")
st.divider()

# =========================================================
# 6. Patient Information
# =========================================================

st.subheader("👤 Patient Information")

col1, col2 = st.columns(2)

# =========================================================
# 7. Column 1
# =========================================================

with col1:

    age = st.number_input(
        "👤 Age",
        placeholder="Enter your age",
        min_value=18,
        max_value=100,
        value=40,
        step=5
    )

    resting_bp = st.number_input(
        "🩸 Resting Blood Pressure (mmHg)",
        min_value=80,
        max_value=220,
        value=120,
        step=10
    )

    st.caption("Normal range: 90–120 mmHg")

    chest_pain = st.selectbox(
        "💓 Chest Pain Type",
        ["ATA", "NAP", "ASY", "TA"]
    )

    st.caption(
        "ATA: Atypical Angina | "
        "NAP: Non-Anginal Pain | "
        "ASY: Asymptomatic | "
        "TA: Typical Angina"
    )

    resting_ecg = st.selectbox(
        "📈 Resting ECG",
        ["Normal", "LVH", "ST"]
    )

    st.caption(
        "Normal: Normal ECG | "
        "LVH: Left Ventricular Hypertrophy | "
        "ST: ST-T Wave Abnormality"
    )

    exercise_angina = st.selectbox(
        "🏃 Exercise Induced Angina",
        ["No", "Yes"]
    )

    st.caption(
        "No: No chest pain during exercise | "
        "Yes: Chest pain during exercise"
    )

    st_slope = st.selectbox(
        "📊 ST Slope",
        ["Up", "Flat", "Down"]
    )

    st.caption(
        "Up: Upsloping | "
        "Flat: Flat | "
        "Down: Downsloping"
    )

# =========================================================
# 8. Column 2
# =========================================================

with col2:

    gender = st.selectbox(
        "🚻 Gender",
        ["Male", "Female"]
    )

    cholesterol = st.number_input(
        "🧪 Cholesterol (mg/dL)",
        min_value=0,
        max_value=700,
        value=200,
        step=50
    )

    st.caption("Normal cholesterol: Below 200 mg/dL")

    fasting_bs = st.selectbox(
        "🍬 Fasting Blood Sugar",
        ["No", "Yes"]
    )

    st.caption(
        "No: ≤120 mg/dL | "
        "Yes: >120 mg/dL"
    )

    max_hr = st.number_input(
        "❤️ Maximum Heart Rate",
        min_value=60,
        max_value=220,
        value=150,
        step=10
    )

    oldpeak = st.number_input(
        "📉 Oldpeak",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.1
    )

    st.caption(
        "Oldpeak represents ST depression "
        "induced by exercise compared to rest."
    )

# =========================================================
# 9. Prediction
# =========================================================

st.divider()

st.subheader("🔍 Predict Heart Disease")

predict = st.button(
    "🔍 Predict Heart Disease",
    use_container_width=True
)

# =========================================================
# 10. Prediction Logic
# =========================================================

if predict:

    # -----------------------------------------------------
    # Convert UI Gender to Original Dataset Value
    # -----------------------------------------------------

    gender_original = {
        "Male": "M",
        "Female": "F"
    }

    gender_value = gender

    # -----------------------------------------------------
    # Convert Exercise Angina
    # -----------------------------------------------------

    exercise_original = {
        "Yes": "Y",
        "No": "N"
    }

    exercise_value = exercise_original[exercise_angina]

    # -----------------------------------------------------
    # Encode values using saved encoders
    # -----------------------------------------------------

    sex_encoded = encoders["Sex"].transform(
        [gender_value]
    )[0]

    chest_pain_encoded = encoders["ChestPainType"].transform(
        [chest_pain]
    )[0]

    resting_ecg_encoded = encoders["RestingECG"].transform(
        [resting_ecg]
    )[0]

    exercise_angina_encoded = encoders["ExerciseAngina"].transform(
        [exercise_value]
    )[0]

    st_slope_encoded = encoders["ST_Slope"].transform(
        [st_slope]
    )[0]

    # FastingBS is already numeric
    fasting_bs_encoded = 1 if fasting_bs == "Yes" else 0

    # -----------------------------------------------------
    # Create Input DataFrame
    # -----------------------------------------------------

    input_data = pd.DataFrame(
        [[
            age,
            sex_encoded,
            chest_pain_encoded,
            resting_bp,
            cholesterol,
            fasting_bs_encoded,
            resting_ecg_encoded,
            max_hr,
            exercise_angina_encoded,
            oldpeak,
            st_slope_encoded
        ]],
        columns=[
            "Age",
            "Sex",
            "ChestPainType",
            "RestingBP",
            "Cholesterol",
            "FastingBS",
            "RestingECG",
            "MaxHR",
            "ExerciseAngina",
            "Oldpeak",
            "ST_Slope"
        ]
    )

    # -----------------------------------------------------
    # Prediction
    # -----------------------------------------------------

    prediction = model.predict(input_data)

    # -----------------------------------------------------
    # Prediction Probability
    # -----------------------------------------------------

    probability = model.predict_proba(input_data)

    risk_probability = probability[0][1] * 100

    # -----------------------------------------------------
    # Convert Prediction
    # -----------------------------------------------------

    if prediction[0] == 1:

        result = "High Risk"

    else:

        result = "Low Risk"

    # =====================================================
    # SAVE PREDICTION HISTORY
    # =====================================================

    new_record = pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "RestingBP": [resting_bp],
        "Cholesterol": [cholesterol],
        "MaxHR": [max_hr],
        "HeartDisease": [prediction[0]],
        "Result": [result],
        "RiskProbability": [round(risk_probability, 2)]
    })

    # -----------------------------------------------------
    # If history file exists → append
    # Otherwise → create new file
    # -----------------------------------------------------

    if os.path.exists(history_file):

        new_record.to_csv(
            history_file,
            mode="a",
            header=False,
            index=False
        )

    else:

        new_record.to_csv(
            history_file,
            mode="w",
            header=True,
            index=False
        )

    # =====================================================
    # DISPLAY RESULT
    # =====================================================

    st.divider()

    if prediction[0] == 1:

        st.error(
            "🔴⚠️ High Risk of Heart Disease Detected.\n\n"
            "Please consult a healthcare professional."
        )

    else:

        st.success(
            "🟢✅ Low Risk of Heart Disease Detected.\n\n"
            "Maintain a healthy lifestyle."
        )

    st.metric(
        "Estimated Risk",
        f"{risk_probability:.2f}%"
    )

    st.info(
        "📊 This prediction has been added to the "
        "Visualization dashboard."
    )