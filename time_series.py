import streamlit as st
import statsmodels.api as sm
import plotly.graph_objects as go

def timeseries(df, periodo, modelo):

    res = sm.tsa.seasonal_decompose(df.value, model=modelo, period=periodo, extrapolate_trend='freq')

    fig = go.Figure()
    fig2 = go.Figure()

    # Add traces
    fig.add_trace(go.Scatter(x=df.index, y=df.value,
                             mode='markers',
                             name='Deaths_count'))
    fig.add_trace(go.Scatter(x=res.trend.index, y=res.trend,
                             mode='lines',
                             name='trend'))
    fig.add_trace(go.Scatter(x=res.seasonal.index, y=res.seasonal,
                             mode='lines',
                             name='Seasonality'))

    fig2.add_trace(go.Scatter(x=res.resid.index, y=res.resid,
                              mode='lines+markers',
                              name='Random'))

    st.plotly_chart(fig)
    #st.plotly_chart(fig2)
