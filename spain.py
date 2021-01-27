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

    status = st.radio("Information: ", ('General', 'diagnóstico','Población'))

    if (status == 'General'):
        st.markdown("""
                    <iframe id='ep-chart-148d86e3-cf82-4b83-bedb-ce12f71c3510' src='https://www.epdata.es/embed/148d86e3-cf82-4b83-bedb-ce12f71c3510/450' style='width: 100%; min-height: 450px; overflow: hidden;' frameborder='0' scrolling='no' height='450'></iframe>
                    """, unsafe_allow_html=True)

        st.markdown("""
            <iframe id='ep-chart-a5804d18-8359-43f5-b6e9-05b93e037452' src='https://www.epdata.es/embed/a5804d18-8359-43f5-b6e9-05b93e037452/450' style='width: 100%; min-height: 450px; overflow: hidden;' frameborder='0' scrolling='no' height='450'></iframe>
            """, unsafe_allow_html=True)