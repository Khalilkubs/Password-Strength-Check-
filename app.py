import streamlit as st


conversion_factors = {
    "Length": {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701},
    "Weight": {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274}
}

# Temperature conversion function
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit: return value
    conversions = {
        ("Celsius", "Fahrenheit"): (value * 9/5) + 32, ("Celsius", "Kelvin"): value + 273.15,
        ("Fahrenheit", "Celsius"): (value - 32) * 5/9, ("Fahrenheit", "Kelvin"): (value - 32) * 5/9 + 273.15,
        ("Kelvin", "Celsius"): value - 273.15, ("Kelvin", "Fahrenheit"): (value - 273.15) * 9/5 + 32
    }
    return conversions.get((from_unit, to_unit), value)

st.markdown("<h1 style='text-align: center;'>⚖️ Khalil Unit Converter 🔄</h1>", unsafe_allow_html=True)
st.write("### Service for Conversion of Temperature, Weight, & Length")
category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])
units = list(conversion_factors.get(category, ["Celsius", "Fahrenheit", "Kelvin"]))

col1, col2 = st.columns(2)
with col1: from_unit = st.selectbox("From", units)
with col2: to_unit = st.selectbox("To", units)
value = st.number_input("Enter Value", format="%.2f")

if st.button("Convert"):
    result = convert_temperature(value, from_unit, to_unit) if category == "Temperature" else value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])
    st.success(f"Converted Value: {result:.2f} {to_unit}")
