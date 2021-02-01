import streamlit as st
import pandas as pd
import plotly.express as px

import time_series
import Ger_gesundsystem

def app():
    st.write('## Deutschland')
    st.write('Leben ist immer lebensgefährlich (Erich Kästner)')

    st.sidebar.write('Source')
    st.sidebar.write('https://www-genesis.destatis.de/')
    st.sidebar.write('https://www.gbe-bund.de/')

    status = st.radio("Information: ", ('im Allgemeinen', 'Hauptdiagnose','Bevölkerungen'))

    if (status == 'im Allgemeinen'):

        df = pd.read_csv("data/Deutschland/sonderauswertung-sterbefaelle_taglich2.csv", skiprows=7, usecols=range(367),
                         encoding='utf-8', index_col=0)
        df = df.T
        df = pd.melt(df, id_vars='Jahr')
        df['date'] = df["Jahr"] + df["variable"]
        df = df[df.value != 'X']
        df = df.dropna()
        df.value = df.value.astype(int)

        df.date = pd.to_datetime(df.date, format="%d.%m.%Y")
        dft = df.sort_values('date')
        dft = dft.set_index('date')
        figo = px.line(dft, x=dft.index, y=dft.value, title="Sterbefälle nach Tagen")
        st.plotly_chart(figo)

        if st.checkbox('Extracting Seasonality and Trend from Data (täglich)'):
            st.markdown('Trend, Saisonalität, Rest_')
            time_series.timeseries(dft,365, 'additive', 'value')



        df1 = pd.read_csv("data/Deutschland/sterbefallzahlen.csv", delimiter=';',usecols=range(6))
        df2=pd.melt(df1,id_vars=["Kalenderwoche"])
        df2['date'] = pd.to_datetime(df2.Kalenderwoche.astype(str)+ df2.variable.astype(str).add('-1') ,format='%V%G-%u')
        df2 = df2.set_index('date')
        df2 = df2.dropna()
        fig = px.line(df2, x=df2.index, y="value")
        fig.update_yaxes(title_text='Sterbefallzahlen wöchentlich')
        st.plotly_chart(fig)

        if st.checkbox('Extracting Seasonality and Trend from Data (woche)'):
            st.markdown('Trend, Saisonalität, Rest_')
            time_series.timeseries(df2,52, 'additive', 'value')

        df = pd.read_csv("data/Deutschland/sonderauswertung-sterbefaelle_w_AG.csv", skiprows=8, usecols=range(1, 56),
                         encoding='utf-8')
        df = pd.melt(df, id_vars=["Unnamed: 1", "unter … Jahren"])
        df['date'] = pd.to_datetime(df.variable.astype(str) + df["Unnamed: 1"].astype(str).add('-1'), format='%V%G-%u')
        df = df[df.value != 'X ']
        df = df.dropna()
        df = df[df['unter … Jahren'] != 'Insgesamt']
        df.value = df.value.astype(int)
        df = df.sort_values('date')
        df = df.set_index('date')
        fig5 = px.line(df, x=df.index, y=df.value, color="unter … Jahren",
                       title='Sterbefälle nach Altersgruppen in Deutschland')
        fig5.update_yaxes(title_text='Sterbefallzahlen wöchentlich')
        st.plotly_chart(fig5)

        if st.checkbox('Extracting Seasonality and Trend from Data(Altersgruppen)'):
            st.markdown('tendência, sazonalidade__')
            valor=st.selectbox('Altersgruppen',df['unter … Jahren'].value_counts().index,
                               index=1)
            time_series.timeseries(df[df["unter … Jahren"]==valor],52,'additive','value')


        df_mon = pd.read_csv("data/Deutschland/sterbefallzahlen_monatlich.csv", delimiter=';', skiprows=6, nrows=370,
                         encoding='ISO-8859-1')
        md = {'Januar': 1, 'Februar': 2, 'März': 3, 'April': 4, 'Mai': 5, 'Juni': 6, 'Juli': 7, 'August': 8, 'September': 9,
              'Oktober': 10, 'November': 11, 'Dezember': 12}
        # month
        df_mon["Unnamed: 1"] = df_mon["Unnamed: 1"].map(md).astype(int)
        df_mon['date'] = df_mon["Unnamed: 1"].astype(str) + '-' + df_mon["Unnamed: 0"].astype(str)
        df_mon.date = pd.to_datetime(df_mon.date, format='%m-%Y')
        df_mon = df_mon.set_index('date')
        df_mon.value = df_mon.Anzahl

        fig2 = px.line(df_mon, x=df_mon.index, y="Anzahl", title="Mortalität in Deutschland seit 1990")
        fig2.update_yaxes(title_text='Sterbefallzahlen monatlich')
        st.plotly_chart(fig2)


        if st.checkbox('Extracting Seasonality and Trend from Data (Monat)'):
            st.markdown('Trend, Saisonalität, Rest')
            time_series.timeseries(df_mon,12, 'additive', 'Anzahl')

        df_A = pd.read_csv("data/Deutschland/sterbefallzahlen_Altersjahre.csv", skiprows=329, encoding='utf-8',
                           index_col=1)
        fig3 = px.line(df_A.T, x=df_A.T.index,
                       y=['Insgesamt', 'unter 1 Jahr', '1-9-Jährige', '10-19-Jährige', '20-29-Jährige',
                          '30-39-Jährige', '40-49-Jährige', '50-59-Jährige', '60-69-Jährige',
                          '70-79-Jährige', '80-89-Jährige', '90-99-Jährige',
                          '100 Jahre und mehr'])
        fig3.update_yaxes(title_text='Sterbefallzahlen Jahrlich')
        fig3.update_xaxes(
            tickangle=90,
            title_text="Death counts per age group: Germany",
            title_font={"size": 20},
            title_standoff=25)
        fig3.update_layout(legend_title_text='Altersgruppe',
                           legend=dict(y=1),
                           autosize=True,
                           # width=600,  # height=400,
                           margin=dict(l=20, r=20, b=20, t=20)
                           )
        fig3.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01))

        st.markdown('---')
        st.plotly_chart(fig3)

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

    else:
        Ger_gesundsystem.app()