import streamlit as st
import pickle
import numpy as np

# -------------------------------
# Load Trained Model
# -------------------------------
model = pickle.load(open('cgpa_predictor_model.pkl', 'rb'))

# -------------------------------
# Streamlit Page Settings
# -------------------------------
st.set_page_config(
    page_title="Student CGPA Predictor",
    page_icon="🎓",
    layout="centered"
)

# -------------------------------
# Title
# -------------------------------
st.title("🎓 Student CGPA Predictor")
st.write("Enter the student details below to predict CGPA.")

# -------------------------------
# Input Fields
# -------------------------------
attendance = st.number_input(
    "Attendance Percentage",
    min_value=0.0,
    max_value=100.0,
    value=80.0
)

internal_marks = st.number_input(
    "Internal Marks",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

backlogs = st.number_input(
    "Number of Backlogs",
    min_value=0,
    max_value=10,
    value=0
)

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict CGPA"):

    # Prepare input data
    input_data = np.array([[attendance, internal_marks, backlogs]])

    # Predict
    prediction = model.predict(input_data)

    # Convert prediction to float safely
    predicted_cgpa = float(prediction[0])

    # Display result
    st.success(f"Predicted CGPA: {round(predicted_cgpa, 2)}") 