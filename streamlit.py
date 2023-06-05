import streamlit as st
st.set_page_config(page_title="Calculator", page_icon="🐬")

st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .stNumberInput:first-child input {
        background-color:black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("Calculator")

num1 = st.number_input("Enter the first number:",step=1)
num2 = st.number_input("Enter the second number:",step=1)


operation = st.selectbox("Select an operation:", ["Addition", "Subtraction", "Multiplication", "Division","Remainder"])

if st.button("Click"):
    result=None
    if operation == "Addition":
        result = num1 + num2
        
    elif operation == "Subtraction":
        result = num1 - num2
        
    elif operation == "Multiplication":
        result = num1 * num2
        
    elif operation == "Division":
        result = num1 / num2 if num2 != 0 else "error : cannot be divided by zero"
    elif operation== "Remainder":
        result=num1%num2
        
    if result is not None:
        st.success("Result : {}".format(result))





