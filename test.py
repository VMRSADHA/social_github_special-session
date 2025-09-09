import streamlit as st

# Title of the app
st.title("🎉 My First Streamlit App")

# Input for name
name = st.text_input("Enter your name")

# Input for age
age = st.number_input("Enter your age", min_value=0, max_value=120, step=1)

# Button to trigger greeting
if st.button("Say Hello"):
    if name and age:
        st.success(f"Hello {name}, aged {int(age)} — Welcome to my page! 🎈")
    elif not name:
        st.warning("Please enter your name.")
    elif age == 0:
        st.warning("Please enter a valid age.")
