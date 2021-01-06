import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import locale

def app():
    st.write('## Deutschland')
    st.write('Leben ist immer lebensgefährlich (Erich Kästner)')
    st.sidebar.write('https://www.destatis.de/DE/Themen/Querschnitt/Corona/_Grafik/_Interaktiv/woechentliche-sterbefallzahlen-jahre.html?nn=209016')
    st.sidebar.write('https://www-genesis.destatis.de/genesis/online?operation=ergebnistabelleUmfang&levelindex=3&levelid=1609865429347&downloadname=12613-0005#abreadcrumb')

    locale.setlocale(locale.LC_ALL, 'de_DE')


    df_mon = pd.read_csv("data/Deutschland/sterbefallzahlen_monatlich.csv", delimiter=';', skiprows=6, nrows=369,
                     encoding='ISO-8859-1')
    df_mon['date'] = df_mon["Unnamed: 1"].astype(str) + '-' + df_mon["Unnamed: 0"].astype(str)
    df_mon.date = pd.to_datetime(df_mon.date, format='%B-%Y')


    fig2 = px.line(df_mon, x=df_mon.date, y="Anzahl", title="Mortalität in Deutschland seit 1990 (Offizielle Daten)")
    fig2.update_yaxes(title_text='Sterbefallzahlen monatlich')
    st.plotly_chart(fig2)

    df = pd.read_csv("data/Deutschland/sterbefallzahlen.csv", delimiter=';',usecols=range(6))
    df2=pd.melt(df,id_vars=["Kalenderwoche"])
    df2['date'] = pd.to_datetime(df2.Kalenderwoche.astype(str)+ df2.variable.astype(str).add('-1') ,format='%V%G-%u')
    fig = px.line(df2, x=df2.date, y="value")
    fig.update_yaxes(title_text='Sterbefallzahlen wöchentlich')
    st.plotly_chart(fig)




    #dfpop = pd.read_csv("data/Deutschland/Bevölkerung.csv", delimiter=';', skiprows=5, nrows=70, encoding='ISO-8859-1')
    #dfpop['Unnamed: 0'] = pd.to_datetime(dfpop['Unnamed: 0'])
    #fig3 = px.line(dfpop, x='Unnamed: 0', y="Anzahl")
    #st.plotly_chart(fig3)
