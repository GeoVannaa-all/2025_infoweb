import streamlit as st
import pandas as pd
from agenda import View

class VisualizarMeusServicosUI:
    @staticmethod
    def main():
        st.title("Visualizar Meus Serviços")
        if "usuario" not in st.session_state or st.session_state["usuario"]["tipo"] != "Cliente":
            st.warning("Apenas clientes podem acessar esta tela.")
            return

        cli_id = st.session_state["usuario"]["id"]
        agendamentos = [a for a in View.agendamento_listar() if a.id_cliente == cli_id]
        if not agendamentos:
            st.info("Você não possui agendamentos.")
            return

        df = pd.DataFrame([a.to_json() for a in agendamentos])
        df["confirmado"] = df["confirmado"].map({True: "Confirmado", False: "Aguardando"})
        df = df.sort_values(["data", "hora"])
        st.dataframe(df)

        