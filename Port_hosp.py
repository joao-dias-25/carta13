import streamlit as st
import requests
import pandas as pd
from io import StringIO
import plotly.express as px


def app():
    @st.cache(persist=True,allow_output_mutation=True)
    def load_data():
        url = requests.get('https://carta13.s3.filebase.com/morbilidade-e-mortalidade-hospitalar-2021_12.csv').content
        csv_raw = StringIO(url.decode('utf-8'))
        df = pd.read_csv(csv_raw, low_memory=False, index_col=0)
        df['desc_capitulo'] = df['desc_capitulo'].str.lower()
        df['desc_capitulo'] = df['desc_capitulo'].str.replace("códigos para fins especiais",
                                                              "códigos para fins especiais (COVID-19??)")
        df['desc_capitulo'] = df['desc_capitulo'].str.replace("algumas ",
                                                              "")
        # df['fields.periodo'] = pd.to_datetime(df['fields.periodo'], format='%Y-%m')
        return df

    df=load_data()
    #top = df.loc[df['fields.periodo'] == 'Jun 2020']['fields.desc_capitulo'].value_counts().loc[lambda x: x > 200].index.tolist()

    dfg=df.groupby(['periodo','desc_capitulo'], as_index=False).agg({'obitos':'sum'})

    #dfg = dfg.loc[dfg['fields.desc_capitulo'].isin(top)]
    fig = px.line(dfg, x=dfg['periodo'], y=['obitos'], color='desc_capitulo')
    fig.update_yaxes(title_text='Mortes em unidades hospitalares')
    fig.update_layout(showlegend=True, height=600, width=1200,
                      title_text="Total de episódios de internamento, ambulatório e óbitos por capitulo de diagnóstico principal da ICD9CM/ICD10CM/PCS",
                      legend=dict(
                          x=1, y=0, traceorder="normal", font=dict(size=8), bgcolor="WhiteSmoke"))

    st.plotly_chart(fig)


    st.markdown("""

    <iframe src="https://transparencia.sns.gov.pt/explore/embed/dataset/morbilidade-e-mortalidade-hospitalar/analyze/?dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJsaW5lIiwiZnVuYyI6IlNVTSIsInlBeGlzIjoib2JpdG9zIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiIzhkYTBjYiJ9XSwieEF4aXMiOiJwZXJpb2RvIiwibWF4cG9pbnRzIjoiIiwidGltZXNjYWxlIjoibW9udGgiLCJzb3J0IjoiIiwiY29uZmlnIjp7ImRhdGFzZXQiOiJtb3JiaWxpZGFkZS1lLW1vcnRhbGlkYWRlLWhvc3BpdGFsYXIiLCJvcHRpb25zIjp7fX19XSwiZGlzcGxheUxlZ2VuZCI6dHJ1ZSwiYWxpZ25Nb250aCI6dHJ1ZSwidGltZXNjYWxlIjoiIn0%3D&static=false&datasetcard=false" width="800" height="500" frameborder="0"></iframe>
    """, unsafe_allow_html=True)
    st.markdown("""

    <iframe src="https://transparencia.sns.gov.pt/explore/embed/dataset/morbilidade-e-mortalidade-hospitalar/analyze/?sort=periodo&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJsaW5lIiwiZnVuYyI6IlNVTSIsInlBeGlzIjoiZGlhc19pbnRlcm5hbWVudG8iLCJzY2llbnRpZmljRGlzcGxheSI6dHJ1ZSwiY29sb3IiOiIjNjZjMmE1In0seyJ0eXBlIjoibGluZSIsImZ1bmMiOiJTVU0iLCJ5QXhpcyI6ImFtYnVsYXRvcmlvIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiI2ZjOGQ2MiJ9XSwieEF4aXMiOiJwZXJpb2RvIiwibWF4cG9pbnRzIjoiIiwidGltZXNjYWxlIjoibW9udGgiLCJzb3J0IjoiIiwiY29uZmlnIjp7ImRhdGFzZXQiOiJtb3JiaWxpZGFkZS1lLW1vcnRhbGlkYWRlLWhvc3BpdGFsYXIiLCJvcHRpb25zIjp7InNvcnQiOiJwZXJpb2RvIn19fV0sImRpc3BsYXlMZWdlbmQiOnRydWUsImFsaWduTW9udGgiOnRydWUsInRpbWVzY2FsZSI6IiJ9&static=false&datasetcard=false" width="800" height="500" frameborder="0"></iframe>

    """, unsafe_allow_html=True)

    st.write()
    url = 'https://transparencia.sns.gov.pt/api/records/1.0/search/?dataset=atividade-gripe-inem&q=&rows=5000&sort=periodo&facet=periodo'
    result = requests.get(url)
    data = result.json()
    df=pd.json_normalize(data["records"])
    df['fields.periodo'] = pd.to_datetime(df['fields.periodo'], format='%Y-%m')
    fig2 = px.line(df, x=df['fields.periodo'], y='fields.n_o_registos')
    fig2.update_yaxes(title_text='N. de registos')
    fig2.update_layout(showlegend=True, height=500, width=900,
                      title_text="Evolução Diária das Chamadas de Emergência Atendidas no Centro de Orientação de Doentes Urgentes (CODU)",
                      )
    st.plotly_chart(fig2)
