import streamlit as st
from views import View
import time

class PerfilProfissionalUI:
    def main():
        st.header("Meus Dados (Profissional)")
        op = View.profissional_listar_id(st.session_state["usuario_id"])

        nome = st.text_input("Nome", op.get_nome())
        especialidade = st.text_input("Especialidade", op.get_especialidade())
        conselho = st.text_input("Conselho", op.get_conselho())
        email = st.text_input("E-mail", op.get_email())
        senha = st.text_input("Senha", op.get_senha(), type="password")

        if st.button("Atualizar"):
            View.profissional_atualizar(op.get_id(), nome, especialidade, conselho, email, senha)
            st.success("Dados atualizados com sucesso!")
            time.sleep(2)
            st.rerun()