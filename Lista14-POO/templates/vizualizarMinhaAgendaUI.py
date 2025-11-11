import streamlit as st
import pandas as pd
from agenda import View

class VisualizarMinhaAgendaUI:
    @staticmethod
    def main():
        st.title("Visualizar Minha Agenda")
        if "usuario" not in st.session_state or st.session_state["usuario"]["tipo"] != "Profissional":
            st.warning("Apenas profissionais podem visualizar esta agenda.")
            return

        prof_id = st.session_state["usuario"]["id"]
        agendamentos = [a for a in View.agendamento_listar() if a.id_profissional == prof_id]
        if not agendamentos:
            st.info("Nenhum horário disponível.")
            return

        df = pd.DataFrame([a.to_json() for a in agendamentos])
        df["confirmado"] = df["confirmado"].map({True: "Confirmado", False: "Pendente"})
        df = df.sort_values(["data", "hora"])
        st.dataframe(df)