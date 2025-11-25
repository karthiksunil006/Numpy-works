import streamlit

streamlit.title("Streamlit Works")

streamlit.header("Machine Learning")

streamlit.subheader("Streamlit used to convert  python and ml into a web application")

name=streamlit.text_input("Enter your name please : ")

print(name)

streamlit.success(f"Hello {name}")

#streamlit.button("Say Hello")

num1=streamlit.text_input("Enter the first number : ")
num2=streamlit.text_input("Enter the second number : ")
am_gb = streamlit.slider("Select RAM (GB)", min_value=4, max_value=64, step=2, value=16)

#result=int(num1)+int(num2)

#streamlit.success(result)

if streamlit.button("Add"):

    result=int(num1)+int(num2)

    streamlit.success(result)

if streamlit.button("Substract"):
    result=int(num1)-int(num2)

    streamlit.success(result)