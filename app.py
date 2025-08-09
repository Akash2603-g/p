import streamlit as st
import pickle
import pandas as pd

# Load the model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🌾 Climate Impact on Crop Production")

st.write("Predict crop yield based on climate conditions.")

# Input fields
temperature = st.number_input("Average Temperature (°C)", value=25.0)
rainfall = st.number_input("Rainfall (mm)", value=100.0)
humidity = st.number_input("Humidity (%)", value=60.0)

# Prediction button
if st.button("Predict Crop Yield"):
    # Prepare input for the model
    input_df = pd.DataFrame({
        "Temperature": [temperature],
        "Rainfall": [rainfall],
        "Humidity": [humidity]
    })

    prediction = model.predict(input_df)
    st.success(f"Predicted Crop Yield: {prediction[0]:.2f} tons/ha")

