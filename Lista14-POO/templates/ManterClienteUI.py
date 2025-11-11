import streamlit as st
import pandas as pd
from agenda.view import View
import time

class ManterClienteUI:
    @staticmethod
    def main():
        st.title("Cadastro de Clientes")
        op = st.radio("Escolha uma opção:", ["Listar", "Inserir", "Atualizar", "Excluir"])
        if op == "Listar":
            ManterClienteUI.listar()
        elif op == "Inserir":
            ManterClienteUI.inserir()
        elif op == "Atualizar":
            ManterClienteUI.atualizar()
        elif op == "Excluir":
            ManterClienteUI.excluir()

    @staticmethod
    def listar():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.info("Nenhum cliente cadastrado.")
        else:
            tabela = [c.to_json() for c in clientes]
            st.dataframe(pd.DataFrame(tabela))

    @staticmethod
    def inserir():
        st.subheader("Inserir novo cliente")
        nome = st.text_input("Nome:")
        email = st.text_input("E-mail:")
        fone = st.text_input("Telefone:")
        senha = st.text_input("Senha:", type="password")
        if st.button("Salvar"):
            try:
                View.cliente_inserir(nome, email, fone, senha)
                st.success("Cliente cadastrado com sucesso!")
                time.sleep(1)
                try:
                    st.experimental_rerun()
                except Exception:
                    pass
            except Exception as e:
                st.error(f"Erro: {e}")

    @staticmethod
    def atualizar():
        st.subheader("Atualizar cliente")
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.info("Nenhum cliente cadastrado.")
            return
        op = st.selectbox("Escolha o cliente:", clientes, format_func=lambda c: c.get_nome())
        nome = st.text_input("Novo nome:", op.get_nome())
        email = st.text_input("Novo e-mail:", op.get_email())
        fone = st.text_input("Novo telefone:", op.get_fone())
        senha = st.text_input("Nova senha:", op.get_senha(), type="password")
        if st.button("Atualizar"):
            try:
                View.cliente_atualizar(op.get_id(), nome, email, fone, senha)
                st.success("Cliente atualizado com sucesso!")
                time.sleep(1)
                try:
                    st.experimental_rerun()
                except Exception:
                    pass
            except Exception as e:
                st.error(f"Erro: {e}")

    @staticmethod
    def excluir():
        st.subheader("Excluir cliente")
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.info("Nenhum cliente cadastrado.")
            return
        op = st.selectbox("Escolha o cliente para excluir:", clientes, format_func=lambda c: c.get_nome())
        if st.button("Excluir"):
            try:
                View.cliente_excluir(op.get_id())
                st.success("Cliente excluído com sucesso!")
                time.sleep(1)
                try:
                    st.experimental_rerun()
                except Exception:
                    pass
            except Exception as e:
                st.error(f"Erro: {e}")