import streamlit as st
from views import View
from datetime import datetime, timedelta

class AbrirAgendaUI:
    def main():
        st.header("Abrir Minha Agenda")

        data_inicio = st.text_input("Informe a data em formato dd/mm/aaaa", datetime.now().strftime("%d/%m/%Y"))
        horario_inicio = st.text_input("Informe o horário inicial no formato HH:MM", "09:00")
        horario_final = st.text_input("Informe o horário final no formato HH:MM", "12:00")
        intervalo = st.text_input("Informe o intervalo entre os horários (min)", "30")

        if st.button("Abrir Agenda"):
            try:
                data = datetime.strptime(data_inicio, "%d/%m/%Y").date()
                hora_ini = datetime.strptime(horario_inicio, "%H:%M").time()
                hora_fim = datetime.strptime(horario_final, "%H:%M").time()
                intervalo_min = int(intervalo)

                inicio = datetime.combine(data, hora_ini)
                fim = datetime.combine(data, hora_fim)
                delta = timedelta(minutes=intervalo_min)

                id_profissional = st.session_state["usuario_id"]

                while inicio < fim:
                    View.horario_inserir(
                        inicio,   # agora vai como datetime
                        False,    # confirmado
                        None,     # cliente
                        None,     # serviço
                        id_profissional
                    )
                    inicio += delta

                st.success("Agenda aberta com sucesso!")
            except Exception as e:
                st.error(f"Erro ao abrir agenda: {e}")