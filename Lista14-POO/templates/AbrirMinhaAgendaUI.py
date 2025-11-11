from agenda import View
from datetime import datetime, timedelta
from models.agendamento import Agendamento
import streamlit as st

class AbrirMinhaAgendaUI:
    @staticmethod
    def main():
        st.title("Abrir Minha Agenda")
        if "usuario" not in st.session_state or st.session_state["usuario"]["tipo"] != "Profissional":
            st.warning("Apenas profissionais podem abrir a agenda.")
            return

        data = st.date_input("Data do atendimento")
        hora_inicial = st.time_input("Hora inicial")
        hora_final = st.time_input("Hora final")
        intervalo = st.number_input("Intervalo (minutos)", min_value=15, max_value=120, value=30, step=15)

        if st.button("Gerar horários disponíveis"):
            horarios = []
            hora_atual = datetime.combine(data, hora_inicial)
            fim = datetime.combine(data, hora_final)
            while hora_atual < fim:
                horarios.append(hora_atual.strftime("%H:%M"))
                hora_atual += timedelta(minutes=intervalo)

            for h in horarios:
                View.agendamento_inserir(data.isoformat(), h, st.session_state["usuario"]["id"])

            st.success(f"{len(horarios)} horários adicionados à sua agenda.")