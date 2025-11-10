import streamlit as st
from views import View
from time import sleep

class SigninUI:
    """Página de Sign In do Visitante."""
    @staticmethod
    def main() -> None:
        st.set_page_config(
            page_title="Abrir Conta no Sistema",
            page_icon="👤"
        )
        
        st.header("👤 Abrir Conta no Sistema")

        name = st.text_input("Informe o Nome")
        email = st.text_input("Informe o E-mail")
        phone = st.text_input("Informe o Telefone")
        password = st.text_input("Informe a Senha", type="password")
        do_signin = st.button("Criar")

        if do_signin:
            try:
                View.append_client(name, email, phone, password)
                st.success("Conta Cliente criada com Sucesso!", icon="✔")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}", icon="🚨")
            sleep(2)
            st.rerun()
