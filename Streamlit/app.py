import streamlit as st
import numpy as np
import pandas as pd

st.title("Hello World")

# dataFrame Exemple
df = pd.DataFrame({
    "name": ['John', 'Jane', 'Joe'],
    "age": [20, 21, 22],
    "city": ['New York', 'London', 'Paris']
})
st.write("Here's our first attempt at using data to create a table:")
st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(6, 3),
    columns=['a', 'b', 'c']
)
st.write('uniform')
st.line_chart(np.random.lognormal(mean=0, sigma=1, size=1000))

print(chart_data)

st.line_chart(chart_data)