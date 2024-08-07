import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly

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
df.set_index('timestamp', inplace=True)
df.sort_index(inplace=True)

st.write(df.describe())

st.line_chart(df)

st.write("Now we can look at this time-series plot with Plotly")

plotly_figure = px.line(df, title="MSFT RH Holding")

st.plotly_chart(plotly_figure)