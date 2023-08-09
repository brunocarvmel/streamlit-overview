import streamlit as st
import pages.client.Include as include
import pages.client.Consult as consult
import pages.client.Edit as edit

st.sidebar.title("Menu")
page_client = st.sidebar.selectbox('Cliente', ['Incluir', 'Consultar'])

if page_client == 'Incluir':
    st.experimental_set_query_params()
    include.Include()
    
if page_client == 'Alterar':
    edit.Edit()
    
if page_client == 'Consultar':
    consult.Consult()
    
    
