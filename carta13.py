import streamlit as st

import portugal
import germany
import spain
import italy
import resources
import userschat


st.set_page_config(layout="wide",
                   page_icon="http://clipartsign.com/upload/2016/06/19/rip-headstone-graveyard-clipart-rip-clipart-graveicon-tv.jpg",
                   page_title="Carta 13")

page_bg_img = '''
<style>
  body {
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
  }

.css-1aumxhk {
background-image: url("https://www.lavanguardia.com/r/GODO/LV/p3/Portada/2016/12/12/Recortada/img_aaguilarm_20161212-192817_imagenes_lv_otras_fuentes_tarot_de_marseille_major13_death-kXHE--656x1271@LaVanguardia-Web.jpg");
color: black;
background-color: wheat;
background-repeat: repeat-x;
background-attachment: fixed;
background-position: px 0px;
background-size: 90px 180px;
}


</style>
'''


st.sidebar.markdown(page_bg_img, unsafe_allow_html=True)

st.sidebar.markdown("""<font color='white' size=7  >Carta 13</font>""", unsafe_allow_html=True)




st.title('Historical data on death counts and death causes')

PAGES = {
    "Portugal": portugal,
    "Germany": germany,
    "Spain": spain,
    "Italy": italy,
    "- [Resources]": resources,
    "voting": userschat}

country = st.sidebar.selectbox("Country", ["Portugal", "Germany", "Spain", "Italy"])
# easier way is:list(PAGES.keys()))

res= st.sidebar.button('Comments Page')

if res:
    country = "voting"

page = PAGES[country]

page.app()
