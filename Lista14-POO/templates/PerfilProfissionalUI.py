import streamlit as st
from agenda import View

class PerfilProfissionalUI:
    @staticmethod
    def perfil_profissional(usuario):
        profissionais = View.profissional_listar()
        profissional = next((p for p in profissionais if p.get_email() == usuario["email"]), None)
        if profissional is None:
            st.error("Profissional não encontrado.")
            return

        nome = st.text_input("Nome:", profissional.get_nome())
        especialidade = st.text_input("Especialidade:", profissional.get_especialidade())
        fone = st.text_input("Telefone:", profissional.get_fone())
        email = st.text_input("E-mail:", profissional.get_email())
        senha = st.text_input("Senha:", profissional.get_senha(), type="password")

        if st.button("Salvar"):
            try:
                View.profissional_atualizar(profissional.get_id(), nome, especialidade, fone, email, senha)
                st.session_state["usuario"]["nome"] = nome
                st.session_state["usuario"]["email"] = email
                st.success("Perfil atualizado com sucesso!")
            except Exception as e:
                st.error(f"Erro: {e}")