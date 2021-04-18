import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('Element Correlation')
st.write("In this mini project, I will be seeing if there is any correlation between one's favorite element and their personality traits.")

core_data = pd.DataFrame({
  'Pyro' : [1, 'ESFP'],
  'Hydro' : [2, 'ISTP'],
  'Anemo' : [1, 'INFP'],
  'Electro' : [2, 'INFP'],
  'Dendro' : [1, 'INFJ'],
  'Cryo' : [0],
  'Geo' : [0]})

core_data
