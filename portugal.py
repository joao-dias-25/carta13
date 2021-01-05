import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def app():
    st.write('## Portugal')
    st.write('Viver é muito perigoso...(Guimarães Rosa)')

    st.sidebar.write('https://www.macrotrends.net/countries/PRT/portugal/population')
    st.sidebar.write('https://evm.min-saude.pt/')

    df_pop = pd.read_csv("data/Portugal/pordata_pop.csv", skiprows=7, nrows=61, usecols=range(0, 5))
    df_pop.Total = df_pop.Total.str.replace(',', '.')

    df_dr = pd.read_csv("data/Portugal/pordata.csv", skiprows=7, nrows=61, usecols=range(0, 17))
    if st.checkbox('Show dataframe'):
        st.markdown('### Raw data')
        st.write(df_dr)
    '''dfs = {"populacao" : df_pop, "obitos": df_dr}
    fig = go.Figure()
    for i in dfs:
        fig = fig.add_trace(go.Scatter(x = dfs[i]["Unnamed: 0"],
                                       y = dfs[i]['Total'],
                                       name = i))
    st.plotly_chart(fig)'''

    fig1 = px.line(df_pop, x="Unnamed: 0", y="Total")
    fig1.update_yaxes(title_text='Total da População (em Milhares)')

    st.plotly_chart(fig1)

    fig2 = px.line(df_dr, x="Unnamed: 0", y=['Total', 'Menos de 01',
                                             '01-04', '05-09', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69',
                                             '70-79', '80-89', '90-99', '100 ou mais'])

    fig2.update_yaxes(title_text='Óbitos')

    fig2.update_layout(legend_title_text='Grupo Etário',
                       legend=dict(y=1))

    st.plotly_chart(fig2)
