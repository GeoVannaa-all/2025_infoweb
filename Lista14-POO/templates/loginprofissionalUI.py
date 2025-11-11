import streamlit as st
from views import View

class LoginProfissionalUI:
    def main():
        st.header("Entrar no Sistema (Profissional)")
        email = st.text_input("Informe o e-mail (profissional)")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            p = View.profissional_autenticar(email, senha)
            if p is None:
                st.write("E-mail ou senha inválidos")
            else:
                st.session_state["usuario_id"] = p["id"]
                st.session_state["usuario_nome"] = p["nome"]
                st.rerun()