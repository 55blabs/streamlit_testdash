import streamlit as st
import pandas as pd
import numpy as np



st.header("Michaels Dashboard!")
st.subheader("Activity for 30 day observation")
st.write("Demo dashboard that displays daily activity measures in each activity", "Date & Duration")

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

dataframe = pd.DataFrame(
  np.random.randn(10, 20) ,
  columns =('col %d' % i for i in range(20)))
st.dataframe(dataframe.style.highlight_max(axis=0))

dataframe = pd.DataFrame(
  np.random.randn(10, 20),
  columns= ('col %d' % i for i in range(20)))
st.table(dataframe)

chart_data = pd.DataFrame(
  np.random
