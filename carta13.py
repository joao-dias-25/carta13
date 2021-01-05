import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



import portugal
import germany

page_bg_img = '''
<style>
.css-1aumxhk {
background-image: url("https://www.lavanguardia.com/r/GODO/LV/p3/Portada/2016/12/12/Recortada/img_aaguilarm_20161212-192817_imagenes_lv_otras_fuentes_tarot_de_marseille_major13_death-kXHE--656x1271@LaVanguardia-Web.jpg");
color: white;
background-size: cover;
background-size: 350px 700px
}
</style>
'''

st.sidebar.markdown(page_bg_img, unsafe_allow_html=True)

st.sidebar.title('Carta 13')
st.sidebar.markdown('---')

PAGES = {
    "Portugal": portugal,
    "Germany": germany }

country = st.sidebar.radio("Country", list(PAGES.keys()))

page = PAGES[country]

page.app()
