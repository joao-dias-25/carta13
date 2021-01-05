import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def app():
    st.write('## Deutschland')
    st.write('Leben ist immer lebensgefährlich (Erich Kästner)')
    st.sidebar.write('https://www.destatis.de/DE/Themen/Querschnitt/Corona/_Grafik/_Interaktiv/woechentliche-sterbefallzahlen-jahre.html?nn=209016')
    st.sidebar.write('https://www-genesis.destatis.de/genesis/online?operation=ergebnistabelleUmfang&levelindex=3&levelid=1609865429347&downloadname=12613-0005#abreadcrumb')

    df = pd.read_csv("data/Deutschland/sterbefallzahlen.csv", delimiter=';', index_col=0)
    df2 = pd.melt(df)
    df2
    fig = px.line(df2, x=df2.index, y="value")
    fig.update_yaxes(title_text='Sterbefallzahlen')
    st.plotly_chart(fig)

    df_mon = pd.read_csv("data/Deutschland/sterbefallzahlen_monatlich.csv", delimiter=';', skiprows=6, nrows=369,
                     encoding='ISO-8859-1')
    fig2 = px.line(df_mon, x=df_mon.index, y="Anzahl")
    fig.update_yaxes(title_text='Sterbefallzahlen monatlich')
    st.plotly_chart(fig2)

    dfpop = pd.read_csv("data/Deutschland/Bevölkerung.csv", delimiter=';', skiprows=5, nrows=70, encoding='ISO-8859-1')
    dfpop['Unnamed: 0'] = pd.to_datetime(dfpop['Unnamed: 0'])
    fig3 = px.line(dfpop, x='Unnamed: 0', y="Anzahl")
    st.plotly_chart(fig3)
