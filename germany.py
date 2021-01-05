import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def app():
    st.write('## Germany')
    st.sidebar.write('https://www.destatis.de/DE/Themen/Querschnitt/Corona/_Grafik/_Interaktiv/woechentliche-sterbefallzahlen-jahre.html?nn=209016')

    df = pd.read_csv("data/Deutschland/sterbefallzahlen.csv", delimiter=';', index_col=0)

    df2 = pd.melt(df)
    df2
    fig = px.line(df2, x=df2.index, y="value")
    st.plotly_chart(fig)
