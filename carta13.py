import streamlit as st

import portugal
import germany
import locale

page_bg_img = '''
<style>
  body {
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
  }

.css-1aumxhk {
background-image: url("https://www.lavanguardia.com/r/GODO/LV/p3/Portada/2016/12/12/Recortada/img_aaguilarm_20161212-192817_imagenes_lv_otras_fuentes_tarot_de_marseille_major13_death-kXHE--656x1271@LaVanguardia-Web.jpg");
color: white;
background-color: #cccccc;
background-repeat: repeat-x;
background-attachment: fixed;
background-position: 50px 0px;
background-size: 130px 260px;
}


</style>
'''
locale.setlocale(category=locale.LC_ALL, locale="de_DE.UTF-8" )

st.sidebar.markdown(page_bg_img, unsafe_allow_html=True)

st.sidebar.title('Carta 13')
st.sidebar.markdown('---')

PAGES = {
    "Portugal": portugal,
    "Germany": germany }

country = st.sidebar.radio("Country", list(PAGES.keys()))

page = PAGES[country]

page.app()
