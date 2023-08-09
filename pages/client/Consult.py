import streamlit as st
import controllers.ClientController as clientcontroller
import pages.client.Include as PageIncludeClient

def Consult():
    paramId = st.experimental_get_query_params()
    if paramId.get("id") == None:
        st.experimental_set_query_params()
        colums = st.columns((1, 2, 1, 2, 1, 1))
        costumerList = ['Nº', 'Nome', 'Idade', 'Profissão', 'Excluir', 'Alterar']
        for column, costumer in zip(colums, costumerList):
            column.write(costumer) 
        
        for i in clientcontroller.SelectAllClients():
            col1, col2, col3, col4, col5, col6 = st.columns((1, 2, 1, 2, 1, 1))
            col1.write(i.id)
            col2.write(i.name)
            col3.write(i.age)
            col4.write(i.occupation)
            button_space_exclude = col5.empty()
            on_click_exclude = button_space_exclude.button('Excluir', 'btnExcluir' + str(i.id))
            button_space_edit = col6.empty()
            on_click_edit = button_space_edit.button('Alterar', 'btnAlterar' + str(i.id))
            
            if on_click_exclude:
                clientcontroller.ExcludeClient(i.id)
                st.experimental_rerun()
                
            if on_click_edit:
                st.experimental_set_query_params(
                    id=[i.id]
                )
                st.experimental_rerun()
    else:
        on_click_back = st.button("Voltar")
        if on_click_back:
            st.experimental_set_query_params()
            st.experimental_rerun()
        PageIncludeClient.Include()
            
            
