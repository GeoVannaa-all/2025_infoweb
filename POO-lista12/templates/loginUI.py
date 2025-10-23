import streamlit as st
from views import View

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            c = View.cliente_autenticar(email, senha)
            p = View.profissional_autenticar(email, senha)

            if c != None:
                st.session_state["usuario_id"] = c["id"]
                st.session_state["usuario_nome"] = c["nome"]
                st.session_state["tipo_usuario"] = "cliente"
                st.rerun()
            elif p != None:
                st.session_state["usuario_id"] = p["id"]
                st.session_state["usuario_nome"] = p["nome"]
                st.session_state["tipo_usuario"] = "profissional"
                st.rerun()
            else:
                st.error("E-mail ou senha inválidos")