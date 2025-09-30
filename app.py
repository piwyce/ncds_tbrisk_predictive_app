import streamlit as st
import pickle
import pandas as pd

# Load trained model
with open("random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("TB Risk Prediction App")

# User inputs
age = st.number_input("Age", 0, 120, 30)
sex = st.selectbox("Sex", ["Male", "Female"])
who_stage = st.selectbox("WHO Stage", [1, 2, 3, 4])
current_cd4 = st.number_input("Current CD4 Count", 0, 2000, 500)
viral_load = st.number_input("Current Viral Load", 0, 1000000, 1000)
hb = st.number_input("Hemoglobin (Hb)", 0.0, 20.0, 13.0)

# Encode categorical
sex_val = 1 if sex == "Male" else 0

# Prepare input dataframe
sample = pd.DataFrame([{
    "Age": age,
    "Sex": sex_val,
    "WHO Stage": who_stage,
    "Current CD4 Count": current_cd4,
    "Current Viral Load": viral_load,
    "Hb": hb
}])

# Predict
if st.button("Predict"):
    pred = model.predict(sample)[0]
    st.write("### Prediction:", "High TB Risk" if pred == 1 else "Low TB Risk")
