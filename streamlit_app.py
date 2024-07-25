import streamlit as st
import pandas as pd
import numpy as np

st.write("# Streamlit Calculator")

number_1 = st.number_input("number 1")
number_2 = st.number_input("number 2")
number_3 = number_1 + number_2

st.write("# Answer is ", number_3)


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)


url = 'https://drive.google.com/file/d/12GNv_tTdQBuFawJ0Jc9RW82-2qfMBmlS/view?usp=drive_link'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df = pd.read_csv(path)
df.set_index(0, inplace=True)
df.sort_index(inplace=True)

st.write(df.describe())

st.line_chart(df)
