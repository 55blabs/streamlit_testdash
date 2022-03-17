import streamlit as st
import pandas as pd
import numpy as np


st.header("Michaels Dashboard!")
st.subheader("Activity for 30 day observation")

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)
