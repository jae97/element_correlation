import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('Element Correlation')
st.write("In this mini project, I will be seeing if there is any correlation between one's favorite element and their personality traits.")

core_data = pd.DataFrame({
  'Entry 1' : ['Electro', 'INFP'],
  'Entry 2' : ['Hydro', 'ISTP'],
  'Entry 3' : ['Electro', 'INFP'],
  'Entry 4' : ['Dendro', 'INFJ'],
  'Entry 5' : ['Pyro', 'INFJ'],
  'Entry 6' : ['Anemo', 'INFP'],
  'Entry 7' : ['Hydro', 'ISTP']})

if st.sidebar.checkbox('Show graph'):
  st.bar_graph(core_data)
