import pandas as pd
import streamlit as st

name: str = st.text_input("Name")

age: int = st.slider("Age", 0, 100, 25)

st.write(f"Age: {age}")

options = ['Python', 'Java', 'C++', 'JavaScript']
selected_option = st.selectbox("Select an option", options)
st.write(f"Selected option: {selected_option}")

df_file = st.file_uploader("Upload a file", type='csv')

if df_file is not None:
    df = pd.read_csv(df_file)
    st.write(df)

if name:
    st.write(f"Hello {name}")
