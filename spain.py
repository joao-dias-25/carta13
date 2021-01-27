import streamlit as st
import pandas as pd
import plotly.express as px

import time_series
import Ger_gesundsystem

def app():
    st.write('## España')
    st.write('Vivir es lo más peligroso que tiene la vida (Alejandro Sanz)')

    st.sidebar.write('Source')
    st.sidebar.write('https://www.epdata.es/')

    status = st.radio("Information: ", ('general', 'diagnóstico','Población'))