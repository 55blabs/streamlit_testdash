import streamlit as st
import pandas as pd
import numpy as np



st.header("Michaels Dashboard!")
st.subheader("Activity for 30 day observation")
st.write("How much time are we spending in 10 activities during the time of 30 days")
st.write(['Duration', 'Date', 'Activity'])


x = st.slider('x')
st.write(x, 'squared is', x * x)

st.text_input("Your name", key="name")
st.session_state.name

if st.checkbox('Show dataframe'):
  chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns= ['a', 'b', 'c'])
  
  chart_data

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
  np.random.randn(20, 3),
  columns=['a', 'b', 'c'])
st.line_chart(chart_data)

map_data =pd.DataFrame(
  np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
  columns=['lat', 'lon'])
st.map(map_data)


