import streamlit as st
from agenda import View

class PerfilUI:
    @staticmethod
    def perfil_cliente(usuario):
        clientes = View.cliente_listar()
        cliente = next((c for c in clientes if c.get_email() == usuario["email"]), None)
        if cliente is None:
            st.error("Cliente não encontrado.")
            return

        nome = st.text_input("Nome:", cliente.get_nome())
        email = st.text_input("E-mail:", cliente.get_email())
        fone = st.text_input("Telefone:", cliente.get_fone())
        senha = st.text_input("Senha:", cliente.get_senha(), type="password")

        if st.button("Salvar"):
            try:
                View.cliente_atualizar(cliente.get_id(), nome, email, fone, senha)
                st.session_state["usuario"]["nome"] = nome
                st.session_state["usuario"]["email"] = email
                st.success("Perfil atualizado com sucesso!")
            except Exception as e:
                st.error(f"Erro: {e}")