import streamlit as st
import pandas as pd
import plotly.express as px

import time_series

def app():
    st.write('## Portugal')
    st.write('Viver é muito perigoso...(Guimarães Rosa)')

    st.sidebar.write('Source')
    st.sidebar.write('https://evm.min-saude.pt/')

    df_pop = pd.read_csv("data/Portugal/pordata_pop.csv", skiprows=7, nrows=61, usecols=range(0, 5))
    df_pop.Total = df_pop.Total.str.replace(',', '.').astype(float)


    dfd = pd.read_csv("data/Portugal/Dados_SICO_2021-01-06.csv")
    dfd = pd.melt(dfd, id_vars=["Data"])
    dfd = dfd.dropna()
    dfd.Data = dfd.Data.replace(regex={'Jan': '1', 'Fev': '2', 'Mar': '3', 'Abr': '4', 'Mai': '5', 'Jun': '6',
                                       'Jul': '7', 'Ago': '8', 'Set': '9', 'Out': '10', 'Nov': '11', 'Dez': '12'})
    dfd['date'] = dfd["Data"] + '-' + dfd["variable"].astype(str)
    dfd.date = pd.to_datetime(dfd.date, format="%m-%d-%Y")
    dfd = dfd.set_index('date')
    figo = px.line(dfd, x=dfd.index, y="value",title="Mortalidade diária em Portugal (números oficiais)")
    figo.update_yaxes(title_text='Óbitos')
    st.plotly_chart(figo)

    if st.checkbox('Extracting Seasonality and Trend from Data'):
        st.markdown('tendência, sazonalidade, ruído')
        time_series.timeseries(dfd,365,'additive')


    '''fig1 = px.line(df_pop, x="Unnamed: 0", y="Total")
    fig1.update_yaxes(title_text='Total da População (em Milhares)')

    st.plotly_chart(fig1)'''
