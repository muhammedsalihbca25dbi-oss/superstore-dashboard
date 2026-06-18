import streamlit as st

st.title("BMI Calculator")

# User Details
name = st.text_input("Enter your name")

age = st.number_input(
    "Enter your age",
    min_value=10,
    max_value=100
)

gender = st.radio(
    "Select Gender",
    ["Male", "Female"]
)

weight = st.number_input(
    "Enter Weight (kg)",
    min_value=30.0
)

height = st.number_input(
    "Enter Height (cm)",
    min_value=100.0
)

# BMI Calculation
if height > 0:

    bmi = weight / ((height / 100) ** 2)

    st.header("BMI Result")

    st.write("Your BMI is:", round(bmi, 1))

    if bmi < 18.5:
        st.write("Category: Underweight")

    elif bmi < 25:
        st.write("Category: Normal Weight")

    elif bmi < 30:
        st.write("Category: Overweight")

    else:
        st.write("Category: Obese")

# Calories
st.header("Daily Calories")

activity = st.selectbox(
    "Choose Activity Level",
    [
        "Sedentary",
        "Lightly Active",
        "Moderately Active",
        "Very Active"
    ]
)

if gender == "Male":
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
else:
    bmr = 10 * weight + 6.25 * height - 5 * age - 161

if activity == "Sedentary":
    calories = bmr * 1.2

elif activity == "Lightly Active":
    calories = bmr * 1.375

elif activity == "Moderately Active":
    calories = bmr * 1.55

else:
    calories = bmr * 1.725

st.write("Daily Calories Needed:", round(calories))

# Summary
if st.button("Show Summary"):

    st.header("Summary")

    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Gender:", gender)
    st.write("Weight:", weight, "kg")
    st.write("Height:", height, "cm")
    
    st.write("BMI:", round(bmi, 1))
    st.write("Calories:", round(calories))