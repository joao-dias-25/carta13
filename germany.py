import streamlit as st
import pandas as pd
import plotly.express as px

import time_series

def app():
    st.write('## Deutschland')
    st.write('Leben ist immer lebensgefährlich (Erich Kästner)')

    st.sidebar.write('Source')
    st.sidebar.write('https://www-genesis.destatis.de/')

    status = st.radio("Information: ", ('im Allgemeinen', 'Hauptdiagnose','Bevölkerungen'))

    if (status == 'im Allgemeinen'):
        df_mon = pd.read_csv("data/Deutschland/sterbefallzahlen_monatlich.csv", delimiter=';', skiprows=6, nrows=372,
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
            time_series.timeseries(df_mon,12, 'additive', 'Anzahl')

        df = pd.read_csv("data/Deutschland/sterbefallzahlen_w2.csv", delimiter=';',usecols=range(6))
        df2=pd.melt(df,id_vars=["Kalenderwoche"])
        df2['date'] = pd.to_datetime(df2.Kalenderwoche.astype(str)+ df2.variable.astype(str).add('-1') ,format='%V%G-%u')
        df2 = df2.set_index('date')
        df2 = df2.dropna()
        fig = px.line(df2, x=df2.index, y="value")
        fig.update_yaxes(title_text='Sterbefallzahlen wöchentlich')
        st.plotly_chart(fig)

        if st.checkbox('Extracting Seasonality and Trend from Data (woche)'):
            st.markdown('Trend, Saisonalität, Rest_')
            time_series.timeseries(df2,52, 'additive', 'value')


    elif (status == 'Bevölkerungen'):
        dfp = pd.read_csv("data/Deutschland/Bevölkerung_AG.csv", skiprows=102, nrows=20, encoding='utf-8', index_col=0)
        dfp = dfp.T
        dfp.index = pd.to_datetime(dfp.index, format='%d.%m.%Y')
        figb = px.line(dfp, x=dfp.index, y=['0-4-Jährige', '5-9-Jährige', '10-14-Jährige', '15-19-Jährige',
                                         '20-24-Jährige', '25-29-Jährige', '30-34-Jährige', '35-39-Jährige',
                                         '40-44-Jährige', '45-49-Jährige', '50-54-Jährige', '55-59-Jährige',
                                         '60-64-Jährige', '65-69-Jährige', '70-74-Jährige', '75-79-Jährige',
                                         '80-84-Jährige', '85 Jahre und mehr'],
                       title= 'Deutschland Bevölkerungsstand: Altersgruppe')
        st.markdown('---')
        st.plotly_chart(figb)
        figbt = px.line(dfp, x=dfp.index, y=['Insgesamt'])
        st.plotly_chart(figbt)