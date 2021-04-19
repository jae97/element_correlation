import streamlit as st
import numpy as np
import pandas as pd
pd.plotting.register_matplotlib_converters()
import time
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Element Correlation')
st.write("In this mini project, I will be seeing if there is any correlation between one's favorite element and their personality traits.")

core_data = pd.DataFrame({
  'Elements' : ['Electro', 'Hydro', 'Electro', 'Dendro', 'Pyro', 'Anemo', 'Hydro'],
  'Personality Types' : ['INFJ', 'ISTP', 'INFP', 'INFJ', 'ESFP', 'INFP', 'ISTP']
  })

if st.sidebar.checkbox('Show graph'):
  sns.barplot(x=core_data.index, y=core_data['Electro'])
