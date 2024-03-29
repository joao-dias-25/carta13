import streamlit as st
import pandas as pd
import plotly.express as px

import time_series

import Port_hosp

def app():
    st.write('## Portugal')
    st.write('Viver é muito perigoso...(Guimarães Rosa)')

    status = st.sidebar.radio("informacao: ", ('Geral', 'dados hospitalares', 'Populacao'))

    st.sidebar.write('Source')
    st.sidebar.write('https://evm.min-saude.pt/')
    st.sidebar.write('https://www.pordata.pt/')
    st.sidebar.write('https://transparencia.sns.gov.pt/')


    #status = st.sidebar.radio("informacao: ", ('Geral',  'dados hospitalares','Populacao'))

    if (status == 'Geral'):

        df_pop = pd.read_csv("data/Portugal/pordata_pop.csv", skiprows=7, nrows=61, usecols=range(0, 5))
        df_pop.Total = df_pop.Total.str.replace(',', '.').astype(float)

        dfd = pd.read_csv("data/Portugal/Dados_SICO_2022-07-05.csv")
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
            time_series.timeseries(dfd,365,'additive','value')


        dates=['2014','2015','2016', '2017' , '2018' ,'2019' ,'2020', '2021', '2022']

        def merging_dates(list_dates):
            df = pd.read_csv(f'data/Portugal/Dados_SICO_2021-01-12_{list_dates[0]}.csv').copy()
            df['Data (mm-dd)'] = df['Data (mm-dd)'].replace(
                regex={'Jan': '1', 'Fev': '2', 'Mar': '3', 'Abr': '4', 'Mai': '5', 'Jun': '6',
                       'Jul': '7', 'Ago': '8', 'Set': '9', 'Out': '10', 'Nov': '11', 'Dez': '12'})
            df = df.assign(date=pd.to_datetime(df['Data (mm-dd)'] + '-' + list_dates[0], format='%m-%d-%Y'))
            for date in list_dates[1:]:
                df2 = pd.read_csv(f'data/Portugal/Dados_SICO_2021-01-12_{date}.csv').copy()
                df2 = df2.dropna()
                df2['Data (mm-dd)'] = df2['Data (mm-dd)'].replace(
                    regex={'Jan': '1', 'Fev': '2', 'Mar': '3', 'Abr': '4', 'Mai': '5', 'Jun': '6',
                           'Jul': '7', 'Ago': '8', 'Set': '9', 'Out': '10', 'Nov': '11', 'Dez': '12'})
                df2 = df2.assign(date=pd.to_datetime(df2['Data (mm-dd)'] + '-' + date, format='%m-%d-%Y'))
                df = pd.concat([df, df2])

            df = df.set_index('date')

            return df

        dfg= merging_dates(dates)

        figg = px.line(dfg, x=dfg.index, y=['< 1 ano', '1-4 anos', '5-14 anos', '15-24 anos', '25-34 anos', '35-44 anos', '45-54 anos', '55-64 anos', '65-74 anos', '75-84 anos', '≥ 85 anos']
                       ,title="Mortalidade diária em Portugal (faixa etária)")
        figg.update_yaxes(title_text='Óbitos')
        st.plotly_chart(figg)

        if st.checkbox('Extracting Seasonality and Trend from Data(grupo etário)'):
            st.markdown('tendência, sazonalidade')
            valor=st.selectbox('Grupo etário',['< 1 ano', '1-4 anos', '5-14 anos', '15-24 anos', '25-34 anos', '35-44 anos', '45-54 anos', '55-64 anos', '65-74 anos', '75-84 anos', '≥ 85 anos'],
                               index=8)
            time_series.timeseries(dfg,365,'additive',valor)

        df_dr = pd.read_csv("data/Portugal/pordata_obitos.csv", skiprows=7, nrows=41, usecols=range(0, 15))
        fig2 = px.line(df_dr, x="Unnamed: 0", y=['Total', 'Menos de 01',
                                                 '01-04', '05-09', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69',
                                                 '70-79', '80-89', '90-99', '100 ou mais'])

        fig2.update_yaxes(title_text='Óbitos')
        fig2.update_xaxes(
            tickangle=90,
            title_text="Death counts per age group: Portugal",
            title_font={"size": 20},
            title_standoff=25)
        fig2.update_layout(legend_title_text='Grupo Etário',
                           autosize=True,
                           # width=500,  # height=400,
                           margin=dict(l=20, r=20, b=20, t=20),
                           )
        fig2.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01))

        st.plotly_chart(fig2)

    elif (status == 'dados hospitalares'):
        Port_hosp.app()

    else:
        dfp = pd.read_csv("data/Portugal/pordata_2021_12.csv", skiprows=7, nrows=52, usecols=range(20), index_col=0)
        figp = px.line(dfp, x=dfp.index, y=['0-04', '05-09', '10-14', '15-19', '20-24', '25-29', '30-34',
                                            '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74',
                                            '75-79', '80-84', '85 ou mais'],
                       title='População Portuguesa por faixa etária')
        # figp.update_yaxes(title_text='População')
        st.markdown('---')
        st.plotly_chart(figp)
        figpt = px.line(dfp, x=dfp.index, y=['Total'], title='População total portuguesa')
        st.plotly_chart(figpt)




