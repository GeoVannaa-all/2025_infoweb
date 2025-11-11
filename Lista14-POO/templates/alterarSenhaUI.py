import streamlit as st
from agenda import View

class AlterarSenhaUI:
    @staticmethod
    def main():
        st.title("Alterar Senha do Admin")

        if "usuario" not in st.session_state or st.session_state["usuario"]["email"] != "admin@admin.com":
            st.warning("Somente o Admin pode alterar a senha.")
            return

        nova_senha = st.text_input("Nova senha", type="password")
        if st.button("Salvar nova senha"):
            profissionais = View.profissional_listar()
            for p in profissionais:
                if p.email == "admin@admin.com":
                    p.senha = nova_senha
                    View.profissional_atualizar(p.id, p.nome, p.especialidade, p.fone, p.email, p.senha)
                    st.success("Senha alterada com sucesso.")
                    return
            st.error("Admin não encontrado.")