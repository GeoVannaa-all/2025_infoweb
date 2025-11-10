import pandas as pd
import streamlit as st
from time import sleep
from views import View

class KeepServiceUI:
    """Página do Admin para o Gerenciamento dos Serviços."""
    @staticmethod
    def main() -> None:
        st.set_page_config(
            page_title="Cadastro de Serviços",
            page_icon="🛠️"
        )

        st.header("🛠️ Cadastro de Serviços")

        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Deletar"])

        with tab1: KeepServiceUI.list_services()
        with tab2: KeepServiceUI.insert_service()
        with tab3: KeepServiceUI.update_service()
        with tab4: KeepServiceUI.remove_service()
    
    @staticmethod
    def list_services() -> None:
        services = View.get_service_list()
        services_data = [ [ s.id, s.description, s.value ] for s in services ]
        
        data = pd.DataFrame(
            services_data,
            columns=["ID", "Descrição", "Valor"]
        )

        st.table(data)

    @staticmethod
    def insert_service() -> None:
        description = st.text_input("Insira a Descrição")
        value = st.number_input("Insira o Valor", step=0.1)

        do_insert = st.button("Inserir Serviço")

        if do_insert:
            try:
                View.append_service(description, value)
                st.success("Serviço Inserido com Sucesso!", icon="✔")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}", icon="🚨")
            sleep(2)
            st.rerun()

    @staticmethod
    def update_service() -> None:
        services = View.get_service_list()

        if len(services) <= 0:
            st.write("Nenhum Serviço Registrado.")
        else:
            service_selected = st.selectbox(
                "Selecione um Serviço para Atualizar",
                services
            )
            description = st.text_input("Insira a Descrição", service_selected.description)
            value = st.number_input("Insira o Valor", value=service_selected.value, step=0.1)
            do_update = st.button("Atualizar Cliente")

            if do_update:
                try:
                    View.update_service(service_selected.id, description, value)
                    st.success("Serviço Atualizado com Sucesso!", icon="✔")
                except Exception as e:
                    st.error(f"Um Erro Ocorreu: {e}", icon="🚨")
                sleep(2)
                st.rerun()

    @staticmethod
    def remove_service() -> None:
        services = View.get_service_list()

        if len(services) <= 0:
            st.write("Nenhum Serviço Registrado.")
        else:
            service_selected = st.selectbox(
                "Selecione um Serviço para Deletar",
                services
            )
            do_removal = st.button("Deletar Serviço", type="primary")

            if do_removal:
                try:
                    View.remove_service(service_selected.id)
                    st.success("Serviço Deletado com Sucesso!", icon="✔")
                except Exception as e:
                    st.error(f"Um Erro Ocorreu: {e}", icon="🚨")
                sleep(2)
                st.rerun()
