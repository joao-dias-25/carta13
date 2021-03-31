import streamlit as st

import portugal
import germany
import spain
import italy
import resources
import userschat


st.set_page_config(layout="wide",
                   page_icon=":skull:",
                   page_title="Carta 13")


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
