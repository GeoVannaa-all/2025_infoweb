import pandas as pd
import streamlit as st
from time import sleep
from views import View

class KeepClientUI:
    """Página do Admin para o Gerenciamento dos Clientes."""
    @staticmethod
    def main() -> None:
        st.set_page_config(
            page_title="Cadastro de Clientes",
            page_icon="👤"
        )
        
        st.header("👤 Cadastro de Clientes")

        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Deletar"])

        with tab1: KeepClientUI.list_clients()
        with tab2: KeepClientUI.insert_client()
        with tab3: KeepClientUI.update_client()
        with tab4: KeepClientUI.remove_client()
    
    @staticmethod
    def list_clients() -> None:
        clients = View.get_client_list()
        clients_data = [ [ c.id, c.name, c.email, c.phone, c.password ] for c in clients ]
        
        data = pd.DataFrame(
            clients_data,
            columns=["ID", "Nome", "Email", "Telefone", "Senha"]
        )

        st.table(data)

    @staticmethod
    def insert_client() -> None:
        name = st.text_input("Insira o Nome")
        email = st.text_input("Insira o Email")
        phone = st.text_input("Insira o Telefone")
        password = st.text_input("Insira a Senha", type="password")

        do_insert = st.button("Inserir Cliente")

        if do_insert:
            try:
                View.append_client(name, email, phone, password)
                st.success("Cliente Inserido com Sucesso!", icon="✔")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}", icon="🚨")
            sleep(2)
            st.rerun()

    @staticmethod
    def update_client() -> None:
        clients = View.get_client_list()

        if len(clients) <= 0:
            st.write("Nenhum Cliente Registrado.")
        else:
            client_selected = st.selectbox(
                "Selecione um Cliente para Atualizar",
                clients
            )
            new_name = st.text_input("Insira o Novo Nome", client_selected.name)
            new_email = st.text_input("Insira o Novo Email", client_selected.email)
            new_phone = st.text_input("Insira o Novo Telefone", client_selected.phone)
            new_password = st.text_input("Insira a Nova Senha", client_selected.password, type="password")
            do_update = st.button("Atualizar Cliente")

            if do_update:
                try:
                    View.update_client(client_selected.id, new_name, new_email, new_phone, new_password)
                    st.success("Cliente Atualizado com Sucesso!", icon="✔")
                except Exception as e:
                    st.error(f"Um Erro Ocorreu: {e}", icon="🚨")
                sleep(2)
                st.rerun()

    @staticmethod
    def remove_client() -> None:
        clients = View.get_client_list()

        if len(clients) <= 0:
            st.write("Nenhum Cliente Registrado.")
        else:
            client_selected = st.selectbox(
                "Selecione um Cliente para Deletar",
                clients
            )
            do_removal = st.button("Deletar Cliente", type="primary")

            if do_removal:
                try:
                    View.remove_client(client_selected.id)
                    st.success("Cliente Deletado com Sucesso!", icon="✔")
                except Exception as e:
                    st.error(f"Um Erro Ocorreu: {e}", icon="🚨")
                sleep(2)
                st.rerun()
