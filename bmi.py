# user name
# height
# weight
# bmi=weight/(height)^2

import streamlit

streamlit.title("BMI calculator")

streamlit.subheader("Enter your details for calculation ")

user_name=streamlit.text_input("Enter your user_name : ")

height=streamlit.number_input("Enter your height : ")

weight=streamlit.number_input("Enter your weight : ")

if streamlit.button("Calculate BMI"):

    bmi=weight/height**2

    streamlit.success(f"for {user_name} your BMI is : {bmi}")