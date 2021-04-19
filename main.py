import streamlit as st
import numpy as np
import pandas as pd
import time
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

st.title('Element Correlation')
st.write("In this mini project, I will be seeing if there is any correlation between one's favorite element and their personality traits.")

core_data = pd.DataFrame({
  'Entry 1' : ['Electro', 'INFP'],
  'Entry 2' : ['Hydro', 'ISTP'],
  'Entry 3' : ['Electro', 'INFP'],
  'Entry 4' : ['Dendro', 'INFJ'],
  'Entry 5' : ['Pyro', 'INFJ'],
  'Entry 6' : ['Anemo', 'INFP'],
  'Entry 7' : ['Hydro', 'ISTP'], index = ['Element', 'Personality Type']})

if st.sidebar.checkbox('Show graph'):
  sns.barplot(x=core_data.index, y=core_data['Electro'])
