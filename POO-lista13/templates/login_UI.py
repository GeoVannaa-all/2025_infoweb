import streamlit as st
from views import View
from time import sleep

class LoginUI:
    """Página de Log In do Visitante."""
    @staticmethod
    def main() -> None:
        st.set_page_config(
            page_title="Entrar no Sistema",
            page_icon="👤"
        )
        
        st.header("👤 Entrar no Sistema")

        email = st.text_input("Informe o E-mail")
        password = st.text_input("Informe a Senha", type="password")
        do_login = st.button("Entrar")

        if do_login:
            user_auth = View.auth_user(email, password)

            if user_auth:
                st.session_state["user_id"] = user_auth[0] # "session_state" salva a variável na "sessão" do browser para ser usada em outras páginas do site.
                st.session_state["user_type"] = user_auth[1] # "Tipo do Usuário" indica se ele é um: Cliente, Admin, Profissional, etc.
                st.success("Log In realizado com Sucesso!", icon="✔")
            else:
                st.warning("E-mail ou Senha Inválidos!", icon="⚠")
            
            sleep(2)
            st.rerun()
