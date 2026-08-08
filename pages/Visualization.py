import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# =========================================================
# 1. Load Original Dataset
# =========================================================

dataset_path = (
    "dataset/""heart_disease_prediction_500.csv"
)

df = pd.read_csv(dataset_path)


# =========================================================
# 2. Load Prediction History
# =========================================================

history_file = (
    "prediction_history.csv"
)


if os.path.exists(history_file):

    prediction_df = pd.read_csv(history_file)

else:

    prediction_df = pd.DataFrame(
        columns=[
            "Age",
            "Gender",
            "RestingBP",
            "Cholesterol",
            "MaxHR",
            "HeartDisease",
            "Result",
            "RiskProbability"
        ]
    )


# =========================================================
# 3. Page Configuration
# =========================================================

st.set_page_config(
    page_icon="📊",
    page_title="Heart Disease Data Visualization",
    layout="wide"
)


# =========================================================
# 4. Page Title
# =========================================================

st.title("📊 Heart Disease Data Visualization")

st.divider()


# =========================================================
# 5. LIVE PREDICTION DASHBOARD
# =========================================================

st.header("📂 Original Dataset Analysis")

# =========================================================
# Calculate Live Statistics
# =========================================================

total_predictions = len(prediction_df)

if total_predictions > 0:

    live_male = (
        prediction_df["Gender"] == "Male"
    ).sum()

    live_female = (
        prediction_df["Gender"] == "Female"
    ).sum()

    live_high_risk = (
        prediction_df["HeartDisease"] == 1
    ).sum()

    live_low_risk = (
        prediction_df["HeartDisease"] == 0
    ).sum()

else:

    live_male = 0
    live_female = 0
    live_high_risk = 0
    live_low_risk = 0


# =========================================================
# Live Cards
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    with st.container(border=True):

        st.metric(
            "👥 Total Predictions",
            total_predictions
        )


with col2:

    with st.container(border=True):

        st.metric(
            "👨 Male Predictions",
            live_male
        )


with col3:

    with st.container(border=True):

        st.metric(
            "👩 Female Predictions",
            live_female
        )


with col4:

    with st.container(border=True):

        st.metric(
            "🔴 High Risk",
            live_high_risk
        )


# =========================================================
# Second Live Row
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:

    with st.container(border=True):

        st.metric(
            "🟢 Low Risk",
            live_low_risk
        )


with col2:

    with st.container(border=True):

        if total_predictions > 0:

            high_risk_percentage = (
                live_high_risk /
                total_predictions
            ) * 100

        else:

            high_risk_percentage = 0

        st.metric(
            "❤️ High Risk %",
            f"{high_risk_percentage:.1f}%"
        )


with col3:

    with st.container(border=True):

        st.metric(
            "📊 Original Dataset",
            len(df)
        )
st.divider()




# =========================================================
# 10. Heart Disease + Gender
# =========================================================

col1, col2 = st.columns(2)


with col1:

    st.subheader(
        "📈 Heart Disease Distribution"
    )

    heart_counts = df[
        "HeartDisease"
    ].value_counts()

    labels = [
        "Low Risk",
        "High Risk"
    ]

    sizes = [
        heart_counts.get(0, 0),
        heart_counts.get(1, 0)
    ]

    fig, ax = plt.subplots(
        figsize=(3.5, 3)
    )

    ax.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90,
        textprops={"fontsize": 9}
    )

    ax.set_title(
        "Heart Disease Distribution",
        fontsize=11
    )

    ax.axis("equal")

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=False
    )


with col2:

    st.subheader(
        "📊 Gender Distribution"
    )

    gender_counts = df[
        "Sex"
    ].value_counts()

    labels = [
        "Female",
        "Male"
    ]

    values = [
        gender_counts.get(0, 0),
        gender_counts.get(1, 0)
    ]

    fig, ax = plt.subplots(
        figsize=(4, 3)
    )

    ax.bar(
        labels,
        values
    )

    ax.set_title(
        "Gender Distribution",
        fontsize=12
    )

    ax.set_xlabel("Gender")
    ax.set_ylabel("Patients")

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=False
    )


st.divider()


# =========================================================
# 11. Age + Chest Pain
# =========================================================

col1, col2 = st.columns(2)


with col1:

    st.subheader(
        "📉 Age Distribution"
    )

    fig, ax = plt.subplots(
        figsize=(4, 3)
    )

    ax.hist(
        df["Age"],
        bins=10
    )

    ax.set_title(
        "Age Distribution",
        fontsize=12
    )

    ax.set_xlabel("Age")
    ax.set_ylabel("Frequency")

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=False
    )


with col2:

    st.subheader(
        "❤️ Chest Pain Distribution"
    )

    cp_counts = df[
        "ChestPainType"
    ].value_counts()

    fig, ax = plt.subplots(
        figsize=(4, 3)
    )

    ax.barh(
        cp_counts.index,
        cp_counts.values
    )

    ax.set_title(
        "Chest Pain Distribution",
        fontsize=12
    )

    ax.set_xlabel("Patients")
    ax.set_ylabel("Chest Pain Type")

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=False
    )


st.divider()


# =========================================================
# 12. Cholesterol + Max Heart Rate
# =========================================================

col1, col2 = st.columns(2)


with col1:

    st.subheader(
        "🩸 Cholesterol Distribution"
    )

    fig, ax = plt.subplots(
        figsize=(4, 3)
    )

    ax.boxplot(
        df["Cholesterol"]
    )

    ax.set_title(
        "Cholesterol Distribution",
        fontsize=12
    )

    ax.set_ylabel("mg/dL")

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=False
    )


with col2:

    st.subheader(
        "❤️ Maximum Heart Rate"
    )

    heart_rate = df[
        "MaxHR"
    ].sort_values()

    fig, ax = plt.subplots(
        figsize=(4, 3)
    )

    ax.plot(
        heart_rate
    )

    ax.set_title(
        "Maximum Heart Rate",
        fontsize=12
    )

    ax.set_xlabel("Patients")
    ax.set_ylabel("Heart Rate")

    plt.tight_layout()

    st.pyplot(
        fig,
        use_container_width=False
    )


st.divider()
# =========================================================
# 13. Correlation Heatmap
# =========================================================

st.subheader(
    "🔥 Correlation Heatmap"
)

correlation = df.corr(
    numeric_only=True
)

fig, ax = plt.subplots(
    figsize=(6, 4)
)

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    ax=ax
)

plt.tight_layout()

st.pyplot(
    fig,
    use_container_width=False
)


st.divider()

# prediction history table 
st.subheader("📋 Prediction History")


if total_predictions > 0:

    st.dataframe(
        prediction_df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "Prediction history will appear here "
        "after users make predictions."
    )


st.divider()


# =========================================================
# 14. AI Insights
# =========================================================

st.subheader(
    "🤖 AI Insights"
)

with st.container(border=True):

    st.write(
        f"🩺 **Total Patients:** {len(df)}"
    )

    st.write(
        f"❤️ **Heart Disease Cases:** "
        f"{(df['HeartDisease'] == 1).sum()}"
    )

    st.write(
        f"💚 **Healthy Patients:** "
        f"{(df['HeartDisease'] == 0).sum()}"
    )

    st.write(
        f"👨 **Male Patients:** "
        f"{(df['Sex'] == 1).sum()}"
    )

    st.write(
        f"👩 **Female Patients:** "
        f"{(df['Sex'] == 0).sum()}"
    )

    st.write(
        f"🎂 **Average Age:** "
        f"{round(df['Age'].mean(), 1)} Years"
    )

    st.write(
        f"🩸 **Average Cholesterol:** "
        f"{round(df['Cholesterol'].mean(), 1)} mg/dL"
    )

    st.write(
        f"❤️ **Average Heart Rate:** "
        f"{round(df['MaxHR'].mean(), 1)} bpm"
    )

    st.write(
        f"📈 **Average Resting BP:** "
        f"{round(df['RestingBP'].mean(), 1)} mmHg"
    )

    st.write(
        f"📊 **Heart Disease Percentage:** "
        f"{round((df['HeartDisease'].sum() / len(df)) * 100, 2)}%"
    )