import streamlit as st
import requests
import pandas as pd
from io import StringIO
import plotly.express as px
import json

def app():
    @st.cache(persist=True,allow_output_mutation=True)
    def load_data():
        url = requests.get('https://ndownloader.figshare.com/files/26051960').content
        csv_raw = StringIO(url.decode('utf-8'))
        df = pd.read_csv(csv_raw, low_memory=False, index_col=0)
        #df['fields.periodo'] = pd.to_datetime(df['fields.periodo'], format='%Y-%m')
        return df

    df=load_data()
    key=st.selectbox('columns',['fields.desc_capitulo','fields.faixa_etaria'])

    dfg=df.groupby(['fields.periodo',key], as_index=False).agg({'fields.obitos':'sum'})

    fig = px.line(dfg, x=dfg['fields.periodo'], y=['fields.obitos'], color=key)
    fig.update_yaxes(title_text='Mortes em unidades hospitalares')
    fig.update_layout(showlegend=True, height=800, width=1200,
                      title_text="Evolução mensal de óbitos por capitulo de diagnóstico principal da ICD9CM/ICD10CM/PCS.",
                      legend=dict(
                          x=1, y=0, traceorder="normal", font=dict(size=10), bgcolor="WhiteSmoke"))
    st.plotly_chart(fig)


    st.write()
    st.markdown("""

    <iframe src="https://transparencia.sns.gov.pt/explore/embed/dataset/morbilidade-e-mortalidade-hospitalar/analyze/?dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJsaW5lIiwiZnVuYyI6IlNVTSIsInlBeGlzIjoib2JpdG9zIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiIzhkYTBjYiJ9XSwieEF4aXMiOiJwZXJpb2RvIiwibWF4cG9pbnRzIjoiIiwidGltZXNjYWxlIjoibW9udGgiLCJzb3J0IjoiIiwiY29uZmlnIjp7ImRhdGFzZXQiOiJtb3JiaWxpZGFkZS1lLW1vcnRhbGlkYWRlLWhvc3BpdGFsYXIiLCJvcHRpb25zIjp7fX19XSwiZGlzcGxheUxlZ2VuZCI6dHJ1ZSwiYWxpZ25Nb250aCI6dHJ1ZSwidGltZXNjYWxlIjoiIn0%3D&static=false&datasetcard=false" width="800" height="500" frameborder="0"></iframe>
    """, unsafe_allow_html=True)
    st.markdown("""

    <iframe src="https://transparencia.sns.gov.pt/explore/embed/dataset/morbilidade-e-mortalidade-hospitalar/analyze/?sort=periodo&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJsaW5lIiwiZnVuYyI6IlNVTSIsInlBeGlzIjoiZGlhc19pbnRlcm5hbWVudG8iLCJzY2llbnRpZmljRGlzcGxheSI6dHJ1ZSwiY29sb3IiOiIjNjZjMmE1In0seyJ0eXBlIjoibGluZSIsImZ1bmMiOiJTVU0iLCJ5QXhpcyI6ImFtYnVsYXRvcmlvIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiI2ZjOGQ2MiJ9XSwieEF4aXMiOiJwZXJpb2RvIiwibWF4cG9pbnRzIjoiIiwidGltZXNjYWxlIjoibW9udGgiLCJzb3J0IjoiIiwiY29uZmlnIjp7ImRhdGFzZXQiOiJtb3JiaWxpZGFkZS1lLW1vcnRhbGlkYWRlLWhvc3BpdGFsYXIiLCJvcHRpb25zIjp7InNvcnQiOiJwZXJpb2RvIn19fV0sImRpc3BsYXlMZWdlbmQiOnRydWUsImFsaWduTW9udGgiOnRydWUsInRpbWVzY2FsZSI6IiJ9&static=false&datasetcard=false" width="800" height="500" frameborder="0"></iframe>

    """, unsafe_allow_html=True)