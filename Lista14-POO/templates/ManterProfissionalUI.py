import streamlit as st
import pandas as pd
import time
from agenda import View

class ManterProfissionalUI:
    @staticmethod
    def main():
        st.header("Cadastro de Profissionais")
        aba1, aba2, aba3, aba4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with aba1:
            ManterProfissionalUI.listar()
        with aba2:
            ManterProfissionalUI.inserir()
        with aba3:
            ManterProfissionalUI.atualizar()
        with aba4:
            ManterProfissionalUI.excluir()

    @staticmethod
    def listar():
        profissionais = View.profissional_listar()
        if not profissionais:
            st.info("Nenhum profissional cadastrado.")
            return
        tabela = [p.to_json() for p in profissionais]
        df = pd.DataFrame(tabela)
        st.dataframe(df)

    @staticmethod
    def inserir():
        st.subheader("Inserir novo profissional")
        nome = st.text_input("Nome")
        especialidade = st.text_input("Especialidade")
        fone = st.text_input("Telefone")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        if st.button("Inserir Profissional"):
            try:
                View.profissional_inserir(nome, especialidade, fone, email, senha)
                st.success("Profissional cadastrado com sucesso!")
                time.sleep(1)
                try:
                    st.experimental_rerun()
                except Exception:
                    pass
            except Exception as e:
                st.error(f"Erro ao cadastrar: {e}")

    @staticmethod
    def atualizar():
        st.subheader("Atualizar profissional")
        profissionais = View.profissional_listar()
        if not profissionais:
            st.info("Nenhum profissional cadastrado.")
            return
        op = st.selectbox(
            "Escolha um profissional",
            profissionais,
            format_func=lambda p: getattr(p, "nome", p.get_nome() if hasattr(p, "get_nome") else str(p))
        )

        nome_val = getattr(op, "nome", op.get_nome() if hasattr(op, "get_nome") else "")
        esp_val = getattr(op, "especialidade", op.get_especialidade() if hasattr(op, "get_especialidade") else "")
        fone_val = getattr(op, "fone", op.get_fone() if hasattr(op, "get_fone") else "")
        email_val = getattr(op, "email", op.get_email() if hasattr(op, "get_email") else "")
        senha_val = getattr(op, "senha", op.get_senha() if hasattr(op, "get_senha") else "")

        nome = st.text_input("Novo nome", nome_val)
        especialidade = st.text_input("Nova especialidade", esp_val)
        fone = st.text_input("Novo telefone", fone_val)
        email = st.text_input("Novo e-mail", email_val)
        senha = st.text_input("Nova senha", senha_val, type="password")

        if st.button("Atualizar Profissional"):
            try:
                id_val = getattr(op, "id", op.get_id() if hasattr(op, "get_id") else None)
                View.profissional_atualizar(id_val, nome, especialidade, fone, email, senha)
                st.success("Profissional atualizado com sucesso!")
                time.sleep(1)
                try:
                    st.experimental_rerun()
                except Exception:
                    pass
            except Exception as e:
                st.error(f"Erro ao atualizar: {e}")

    @staticmethod
    def excluir():
        st.subheader("Excluir profissional")
        profissionais = View.profissional_listar()
        if not profissionais:
            st.info("Nenhum profissional cadastrado.")
            return
        op = st.selectbox(
            "Escolha um profissional para excluir",
            profissionais,
            format_func=lambda p: getattr(p, "nome", p.get_nome() if hasattr(p, "get_nome") else str(p))
        )
        if st.button("Excluir Profissional"):
            try:
                id_val = getattr(op, "id", op.get_id() if hasattr(op, "get_id") else None)
                View.profissional_excluir(id_val)
                st.success("Profissional excluído com sucesso!")
                time.sleep(1)
                try:
                    st.experimental_rerun()
                except Exception:
                    pass
            except Exception as e:
                st.error(f"Erro ao excluir: {e}")