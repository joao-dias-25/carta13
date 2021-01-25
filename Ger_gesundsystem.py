import streamlit as st
import requests
import pandas as pd
from io import StringIO
import plotly.express as px


def app():
    df = pd.read_csv("data/Deutschland/sterbefall_bis_2018.csv", delimiter=';', skiprows=11, nrows=18,
                     # usecols=range(22),
                     encoding='ISO-8859-1')
    df = df.T
    df.index = pd.to_datetime(df.index, errors='coerce')

    df = df.drop(['A00-T98 Alle Krankheiten und Folgen äußerer Ursachen',
                  '        O00-O99 Schwangerschaft, Geburt und Wochenbett'], axis=1)
    df = df.replace(to_replace=r'[.]', value='', regex=True)
    df = df.dropna()
    df = df.astype(int, errors='raise')

    fig = px.line(df, x=df.index, y=df.columns)
    fig.update_yaxes(title_text='	Sterbefälle, Sterbeziffern (ab 1998)')
    fig.update_layout(showlegend=True, height=600, width=1200,
                      title_text="Mortalität und Todesursachen",
                      legend=dict(
                          x=2, y=1, traceorder="normal", font=dict(size=10), bgcolor="WhiteSmoke"))
    st.plotly_chart(fig)