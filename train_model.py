import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

from sklearn.preprocessing import LabelEncoder


# ==========================================
# 1. Load Dataset
# ==========================================

df = pd.read_csv(
    "dataset/heart_disease_prediction_500.csv"
)

print("Dataset loaded successfully!")
print("Dataset Shape:", df.shape)


# ==========================================
# 2. Basic Dataset Information
# ==========================================

print("\nFirst 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isna().sum())

print("\nDuplicate Values:")
print(df.duplicated().sum())


# ==========================================
# 3. Label Encoding + Save Encoders
# ==========================================

encoders = {}

columns_to_encode = [
    "Sex",
    "ChestPainType",
    "RestingECG",
    "ExerciseAngina",
    "ST_Slope"
]

for col in columns_to_encode:

    le = LabelEncoder()

    # Original text values nu encode karo
    df[col] = le.fit_transform(df[col])

    # Original values wala encoder save karo
    encoders[col] = le

    print(f"{col} classes:", le.classes_)


# ==========================================
# Save Encoders
# ==========================================

joblib.dump(
    encoders,
    "HeartDisease_encoders.joblib"
)

print("\nEncoders saved successfully!")


# ==========================================
# 5. Features and Target
# ==========================================

X = df.drop("HeartDisease", axis=1)

y = df["HeartDisease"]


print("\nFeatures:")
print(X.head())

print("\nTarget:")
print(y.head())


# ==========================================
# 6. Train-Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    train_size=0.8,
    random_state=42
)


print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)


# ==========================================
# 7. Train Logistic Regression
# ==========================================

model = LogisticRegression(
    max_iter=1000
)

model.fit(
    X_train,
    y_train
)
print("\nModel trained successfully!")

# ==========================================
# 8. Prediction
# ==========================================

y_pred = model.predict(X_test)


print("\nActual Disease:")
print(y_test.values)

print("\nPredicted Disease:")
print(y_pred)


# ==========================================
# 9. Evaluation Metrics
# ==========================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

precision = precision_score(
    y_test,
    y_pred
)

recall = recall_score(
    y_test,
    y_pred
)

f1_score_value = f1_score(
    y_test,
    y_pred
)


print("\n========== MODEL PERFORMANCE ==========")

print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall   :", recall)
print("F1 Score :", f1_score_value)


# ==========================================
# 10. Confusion Matrix
# ==========================================

cm = confusion_matrix(
    y_test,
    y_pred
)

print("\nConfusion Matrix:")
print(cm)


# ==========================================
# 11. Classification Report
# ==========================================

report = classification_report(
    y_test,
    y_pred
)

print("\nClassification Report:")
print(report)


# ==========================================
# 12. Save Model
# ==========================================

joblib.dump(
    model,
    "HeartDisease_model.joblib"
)

print("\nModel saved successfully!")


# ==========================================
# 13. Save Metrics
# ==========================================

metrics = {
    "Accuracy": accuracy,
    "Precision": precision,
    "Recall": recall,
    "F1 Score": f1_score_value
}

joblib.dump(
    metrics,
    "HeartDisease_metrics.joblib"
)
# ==========================================
# 14. Save Confusion Matrix
# ==========================================

joblib.dump(
    cm,
    "confusion_matrix.joblib"
)


# ==========================================
# 15. Save Classification Report
# ==========================================

joblib.dump(
    report,
    "classification_report.joblib"
)


print("\nAll model files saved successfully!")