import streamlit as st
import pandas as pd
import plotly.express as px
from google.cloud import firestore


def app():
    st.header('Comments page')
    st.write('coming soon...')

    # Authenticate to Firestore with the JSON account key.
    #db = firestore.Client.from_service_account_json("data/firestore-key.json")

    # Create a reference to the Google post.
    #doc_ref = db.collection("votes").document("comentarios")

    # Then get the data at that reference.
    #doc = doc_ref.get()

    # Let's see what we got!
    #st.write("The id is: ", doc.id)
    #st.write("The contents are: ", doc.to_dict())

    st.write('What is your general feeling about this historical information?')

