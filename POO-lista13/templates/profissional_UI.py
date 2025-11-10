import pandas as pd
import streamlit as st
from time import sleep
from views import View

class KeepProfessionalUI:
    """Página do Admin para o Gerenciamento dos Profissionais."""
    @staticmethod
    def main() -> None:
        st.set_page_config(
            page_title="Cadastro de Profissionais",
            page_icon="👨‍✈️"
        )
        
        st.header("👨‍✈️ Cadastro de Profissionais")

        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Deletar"])

        with tab1: KeepProfessionalUI.list_professionals()
        with tab2: KeepProfessionalUI.insert_professional()
        with tab3: KeepProfessionalUI.update_professional()
        with tab4: KeepProfessionalUI.remove_professional()
    
    @staticmethod
    def list_professionals() -> None:
        professionals = View.get_professional_list()
        professionals_data = [ [ prof.id, prof.name, prof.email, prof.speciality, prof.council, prof.password ] for prof in professionals ]
        
        data = pd.DataFrame(
            professionals_data,
            columns=["ID", "Nome", "E-mail", "Especialidade", "Conselho", "Senha"]
        )

        st.table(data)

    @staticmethod
    def insert_professional() -> None:
        name = st.text_input("Insira o Nome")
        email = st.text_input("Insira o E-mail")
        speciality = st.text_input("Insira a Especialidade")
        council = st.text_input("Insira o Conselho")
        password = st.text_input("Insira a Senha", type="password")

        do_insert = st.button("Inserir Profissional")

        if do_insert:
            try:
                View.append_professional(name, email, speciality, council, password)
                st.success("Profissional Inserido com Sucesso!", icon="✔")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}", icon="🚨")
            sleep(2)
            st.rerun()

    @staticmethod
    def update_professional() -> None:
        professionals = View.get_professional_list()

        if len(professionals) <= 0:
            st.write("Nenhum Profissional Registrado.")
        else:
            professional_selected = st.selectbox(
                "Selecione um Profissional para Atualizar",
                professionals
            )
            new_name = st.text_input("Insira o Novo Nome", professional_selected.name)
            new_email = st.text_input("Insira o Novo E-mail", professional_selected.email)
            new_speciality = st.text_input("Insira a Nova Especialidade", professional_selected.speciality)
            new_council = st.text_input("Insira o Novo Conselho", professional_selected.council)
            new_password = st.text_input("Insira a Nova Senha", professional_selected.password, type="password")
            do_update = st.button("Atualizar Profissional")

            if do_update:
                try:
                    View.update_professional(professional_selected.id, new_name, new_email, new_speciality, new_council, new_password)
                    st.success("Profissional Atualizado com Sucesso!", icon="✔")
                except Exception as e:
                    st.error(f"Um Erro Ocorreu: {e}", icon="🚨")
                sleep(2)
                st.rerun()

    @staticmethod
    def remove_professional() -> None:
        professionals = View.get_professional_list()

        if len(professionals) <= 0:
            st.write("Nenhum Profissional Registrado.")
        else:
            professional_selected = st.selectbox(
                "Selecione um Profissional para Deletar",
                professionals
            )
            do_removal = st.button("Deletar Profissional", type="primary")

            if do_removal:
                try:
                    View.remove_professional(professional_selected.id)
                    st.success("Profissional Deletado com Sucesso!", icon="✔")
                except Exception as e:
                    st.error(f"Um Erro Ocorreu: {e}", icon="🚨")
                sleep(2)
                st.rerun()
