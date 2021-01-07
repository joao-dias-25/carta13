import streamlit as st
import pandas as pd
import plotly.express as px

import time_series

def app(modelo):
    st.write('## Deutschland')
    st.write('Leben ist immer lebensgefährlich (Erich Kästner)')

    st.sidebar.write('Source')
    st.sidebar.write('https://www-genesis.destatis.de/')


    df_mon = pd.read_csv("data/Deutschland/sterbefallzahlen_monatlich.csv", delimiter=';', skiprows=6, nrows=369,
                     encoding='ISO-8859-1')
    md = {'Januar': 1, 'Februar': 2, 'März': 3, 'April': 4, 'Mai': 5, 'Juni': 6, 'Juli': 7, 'August': 8, 'September': 9,
          'Oktober': 10, 'November': 11, 'Dezember': 12}
    # month
    df_mon["Unnamed: 1"] = df_mon["Unnamed: 1"].map(md).astype(int)
    df_mon['date'] = df_mon["Unnamed: 1"].astype(str) + '-' + df_mon["Unnamed: 0"].astype(str)
    df_mon.date = pd.to_datetime(df_mon.date, format='%m-%Y')
    df_mon = df_mon.set_index('date')
    df_mon.value = df_mon.Anzahl

    fig2 = px.line(df_mon, x=df_mon.index, y="Anzahl", title="Mortalität in Deutschland seit 1990 (Offizielle Daten)")
    fig2.update_yaxes(title_text='Sterbefallzahlen monatlich')
    st.plotly_chart(fig2)

    if st.checkbox('Extracting Seasonality and Trend from Data (Monat)'):
        st.markdown('Trend, Saisonalität, Rest')
        time_series.timeseries(df_mon,12, modelo)

    df = pd.read_csv("data/Deutschland/sterbefallzahlen.csv", delimiter=';',usecols=range(6))
    df2=pd.melt(df,id_vars=["Kalenderwoche"])
    df2['date'] = pd.to_datetime(df2.Kalenderwoche.astype(str)+ df2.variable.astype(str).add('-1') ,format='%V%G-%u')
    df2 = df2.set_index('date')
    df2 = df2.dropna()
    fig = px.line(df2, x=df2.index, y="value")
    fig.update_yaxes(title_text='Sterbefallzahlen wöchentlich')
    st.plotly_chart(fig)

    if st.checkbox('Extracting Seasonality and Trend from Data (woche)'):
        st.markdown('Trend, Saisonalität, Rest_')
        time_series.timeseries(df2,52, modelo)

    df_A = pd.read_csv("data/Deutschland/sterbefallzahlen_Altersjahre.csv", skiprows=329, encoding='utf-8', index_col=1)
    fig3 = px.line(df_A.T, x=df_A.T.index, y=['Insgesamt', 'unter 1 Jahr', '1-9-Jährige', '10-19-Jährige', '20-29-Jährige',
                                          '30-39-Jährige', '40-49-Jährige', '50-59-Jährige', '60-69-Jährige',
                                          '70-79-Jährige', '80-89-Jährige', '90-99-Jährige',
                                          '100 Jahre und mehr'])
    fig3.update_yaxes(title_text='Sterbefallzahlen Jahrlich')
    fig3.update_layout(legend_title_text='Altersgruppe',
                       legend=dict(y=1))
    st.plotly_chart(fig3)



    #dfpop = pd.read_csv("data/Deutschland/Bevölkerung.csv", delimiter=';', skiprows=5, nrows=70, encoding='ISO-8859-1')
    #dfpop['Unnamed: 0'] = pd.to_datetime(dfpop['Unnamed: 0'])
    #fig3 = px.line(dfpop, x='Unnamed: 0', y="Anzahl")
    #st.plotly_chart(fig3)
