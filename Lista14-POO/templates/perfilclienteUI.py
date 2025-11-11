import streamlit as st
from views import View
import time

class PerfilClienteUI:
    def main():
        st.header("Meus Dados")

        usuario_id = st.session_state.get("usuario_id")
        if not usuario_id:
            st.warning("Você precisa estar logado para acessar esta página.")
            return

        op = View.cliente_listar_id(usuario_id)
        if op is None:
            st.error("Usuário não encontrado.")
            return

        nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        fone = st.text_input("Informe o novo fone", op.get_fone())
        senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
        if st.button("Atualizar"):
            id = op.get_id()
            View.cliente_atualizar(id, nome, email, fone, senha)
            st.success("Cliente atualizado com sucesso")
            time.sleep(2)
            st.rerun()