import streamlit as st
import pandas as pd
import time
from agenda.view import View

class ManterServicoUI:
    @staticmethod
    def main():
        st.header("Cadastro de Serviços")
        aba1, aba2, aba3, aba4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with aba1:
            ManterServicoUI.listar()
        with aba2:
            ManterServicoUI.inserir()
        with aba3:
            ManterServicoUI.atualizar()
        with aba4:
            ManterServicoUI.excluir()

    @staticmethod
    def listar():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum serviço cadastrado")
        else:
            tabela = [s.to_json() for s in servicos]
            df = pd.DataFrame(tabela)
            st.dataframe(df)

    @staticmethod
    def inserir():
        descricao = st.text_input("Descrição do serviço")
        valor = st.number_input("Valor do serviço", min_value=0.0, step=0.01, format="%.2f")
        if st.button("Inserir Serviço"):
            View.servico_inserir(descricao, float(valor))
            st.success("Serviço cadastrado!")
            time.sleep(1)
            try:
                st.experimental_rerun()
            except Exception:
                pass

    @staticmethod
    def atualizar():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Escolha um serviço", servicos, format_func=lambda s: getattr(s, "descricao", str(s)))
            descricao = st.text_input("Nova descrição", getattr(op, "descricao", ""))
            valor = st.number_input("Novo valor", value=float(getattr(op, "valor", 0.0)), min_value=0.0, step=0.01, format="%.2f")
            if st.button("Atualizar Serviço"):
                View.servico_atualizar(op.id, descricao, float(valor))
                st.success("Serviço atualizado!")

    @staticmethod
    def excluir():
        servicos = View.servico_listar()
        if len(servicos) == 0:
            st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Escolha um serviço para excluir", servicos, format_func=lambda s: getattr(s, "descricao", str(s)))
            if st.button("Excluir Serviço"):
                View.servico_excluir(op.id)
                st.success("Serviço excluído")