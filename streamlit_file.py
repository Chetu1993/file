
import streamlit as st

st.title("this is my home page")
name=st.text_input("enter your name")
st.write(f"your name is: {name}")