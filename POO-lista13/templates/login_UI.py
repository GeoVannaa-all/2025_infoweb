import streamlit as st
from views import View
from time import sleep


class LoginUI:
    """Página de Log In do Visitante."""

    @staticmethod
    def main() -> None:
        # OBS: st.set_page_config() deve ser chamado apenas uma vez no app principal,
        # então não precisa ficar aqui se já foi configurado em outro arquivo.
        st.header("👤 Entrar no Sistema")

        # Campos de entrada
        email = st.text_input("Informe o E-mail")
        password = st.text_input("Informe a Senha", type="password")

        # Botão de login
        if st.button("Entrar"):
            user_auth = View.auth_user(email, password)

            if user_auth:
                # Salva os dados na sessão
                st.session_state["user_id"] = user_auth[0]
                st.session_state["user_type"] = user_auth[1]

                # Mensagem de sucesso
                st.success("Log In realizado com sucesso!", icon="✔")

                # Pequeno delay só pra mostrar o feedback
                sleep(1)

                # Recarrega a página para atualizar a interface
                st.experimental_rerun()

            else:
                # Mensagem de erro
                st.warning("E-mail ou senha inválidos!", icon="⚠")
