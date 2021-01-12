import streamlit as st
import pandas as pd
import plotly.express as px

import time_series

def app():


    df_dr = pd.read_csv("data/Portugal/pordata.csv", skiprows=7, nrows=61, usecols=range(0, 17))
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
                       #width=500,  # height=400,
                       margin=dict(l=20, r=20, b=20, t=20),
                       )
    fig2.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01))

    st.write('Portugal')
    st.plotly_chart(fig2)

    df_A = pd.read_csv("data/Deutschland/sterbefallzahlen_Altersjahre.csv", skiprows=329, encoding='utf-8', index_col=1)
    fig3 = px.line(df_A.T, x=df_A.T.index, y=['Insgesamt', 'unter 1 Jahr', '1-9-Jährige', '10-19-Jährige', '20-29-Jährige',
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
                       #width=600,  # height=400,
                       margin=dict(l=20, r=20, b=20, t=20)
                       )
    fig3.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01))

    st.markdown('---')
    st.write('Germany')
    st.plotly_chart(fig3)



