import streamlit as st

st.set_page_config(page_title="Bro's Calc", page_layout="centered")
st.title("📱 My Calculator")

# Use a container for a clean look
with st.container():
    num1 = st.number_input("First Number", value=0.0)
    num2 = st.number_input("Second Number", value=0.0)
    
    operation = st.selectbox("Choose Operation", ["+", "-", "×", "÷"])
    
    if st.button("Calculate", use_container_width=True):
        if operation == "+":
            res = num1 + num2
        elif operation == "-":
            res = num1 - num2
        elif operation == "×":
            res = num1 * num2
        elif operation == "÷":
            res = num1 / num2 if num2 != 0 else "Error: Div by 0"
            
        st.success(f"Result: {res}")
