import streamlit as st
import controllers.ClientController as clientcontroller
import models.Client as client

def Include():
    idChange = st.experimental_get_query_params()
    st.experimental_set_query_params()
    clientRecovered = None
    if idChange.get("id") != None:
        idChange = idChange.get("id")[0]
        clientRecovered = clientcontroller.SelectClientById(idChange)
        st.experimental_set_query_params(
            id=[clientRecovered.id]
        )
        st.title(f"Alterar Cliente {clientRecovered.name}")
    else:
        st.title("Incluir Cliente")
        
    with st.form(key="include_client"):
        listOccupation = ["Desenvolvimento", "Músico", "Designer", "Professor"]
        if clientRecovered == None:
            input_name = st.text_input(label="Insira seu nome")
            input_age = st.number_input(label="Insira sua idade", format="%d", step=1)
            input_occupation = st.selectbox("Selecione sua profissão", options=listOccupation)
        else:
            input_name = st.text_input(label="Insira seu nome", value=clientRecovered.name)
            input_age = st.number_input(label="Insira sua idade", format="%d", step=1, value=clientRecovered.age)
            input_occupation = st.selectbox("Selecione sua profissão", options=listOccupation, index=listOccupation.index(clientRecovered.occupation))
            
        input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
        if clientRecovered == None:
            clientcontroller.IncludeClient(client.Client(0, input_name, input_age, input_occupation)) 
            st.success("Cliente incluido com sucesso!!")
        else:
            st.experimental_set_query_params()
            clientcontroller.EditClient(client.Client(idChange, input_name, input_age, input_occupation))
            st.success("Cliente alterado com sucesso!!")
