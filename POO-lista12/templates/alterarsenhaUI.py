import streamlit as st
from views import View

class AlterarSenhaUI:
    def main():
        st.header("Alterar Senha")
        id_cliente = st.session_state["usuario_id"]
        cliente = View.cliente_listar_id(id_cliente)

        id = cliente.get_id()
        nome = cliente.get_nome()
        email = cliente.get_email()
        fone = cliente.get_fone()
        
        senha = st.text_input("Digite a nova senha")

        if st.button("Atualizar senha"):
            View.cliente_atualizar(id, nome, email, fone, senha)
            st.success("Cliente atualizado com sucesso")