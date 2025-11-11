import streamlit as st
from agenda import View
from models.agendamento import Agendamento

class ConfirmarServicoUI:
    @staticmethod
    def main():
        st.title("Confirmar Serviço")
        if "usuario" not in st.session_state or st.session_state["usuario"]["tipo"] != "Profissional":
            st.warning("Apenas profissionais podem confirmar serviços.")
            return

        prof_id = st.session_state["usuario"]["id"]
        agendamentos = [a for a in View.agendamento_listar() if a.id_profissional == prof_id and not a.confirmado]
        if not agendamentos:
            st.info("Nenhum serviço pendente de confirmação.")
            return

        op = st.selectbox("Selecione um agendamento", agendamentos, format_func=lambda a: f"{a.data} {a.hora}")
        if st.button("Confirmar Serviço"):
            op.confirmado = True
            View.agendamento_atualizar(op.id, op.data, op.hora, op.id_profissional, op.id_cliente, op.id_servico, True)
            st.success("Serviço confirmado.")