
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("energy_forecast_model.pkl")

st.title("Energy Forecasting App")

st.write("Enter input details below to get the predicted energy consumption:")

# Input fields
machine_hours = st.number_input("Machine Hours")
material_processed = st.number_input("Material Processed (tons)")
temperature = st.slider("Temperature (°C)", -10.0, 50.0, 25.0)
humidity = st.slider("Humidity (%)", 0.0, 100.0, 50.0)
shift = st.selectbox("Shift", ["Morning", "Evening", "Night"])
machine_type = st.selectbox("Machine Type", ["Hauler", "Crusher", "Excavator"])

# Prediction function
def predict_energy(machine_hours, material_processed, temperature, humidity, shift, machine_type):
    input_data = {
        'Machine_Hours': [machine_hours],
        'Material_Processed_tons': [material_processed],
        'Temperature_C': [temperature],
        'Humidity_%': [humidity],
        'Machine_Type_Crusher': [1 if machine_type == 'Crusher' else 0],
        'Machine_Type_Excavator': [1 if machine_type == 'Excavator' else 0],
        'Machine_Type_Hauler': [1 if machine_type == 'Hauler' else 0],
        'Shift_Evening': [1 if shift == 'Evening' else 0],
        'Shift_Morning': [1 if shift == 'Morning' else 0],
        'Shift_Night': [1 if shift == 'Night' else 0],
    }

    input_df = pd.DataFrame(input_data)
    return model.predict(input_df)[0]

# Button and result
if st.button("Predict"):
    result = predict_energy(machine_hours, material_processed, temperature, humidity, shift, machine_type)
    st.write(f"Predicted Energy Consumption: {result:.2f} kWh")