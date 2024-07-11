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
