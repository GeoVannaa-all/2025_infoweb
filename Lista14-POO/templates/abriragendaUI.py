import streamlit as st
from views import View
from datetime import datetime, timedelta

class AbrirAgendaUI:
    def main():
        st.header("Abrir Minha Agenda")
        st.write("Preencha os campos para inserir horários de atendimento na sua agenda.")
        profissional_id = st.session_state.get("usuario_id")
        if not profissional_id:
            st.warning("Você precisa estar logado como profissional para abrir a agenda.")
            return

        data = st.date_input("Dia do atendimento", datetime.now().date())
        hora_inicial = st.time_input("Hora inicial", value=datetime.now().time())
        hora_final = st.time_input("Hora final", value=(datetime.now() + timedelta(hours=1)).time())
        intervalo = st.number_input("Intervalo entre horários (minutos)", min_value=5, max_value=120, value=30, step=5)
        servicos = View.servico_listar()
        servico = st.selectbox("Serviço oferecido", servicos, format_func=lambda s: s.get_descricao() if s else "")

        if st.button("Inserir horários na agenda"):
            if servico is None:
                st.error("Selecione um serviço.")
                return
            dt_inicial = datetime.combine(data, hora_inicial)
            dt_final = datetime.combine(data, hora_final)
            horarios_criados = 0
            while dt_inicial < dt_final:
                View.horario_inserir(dt_inicial, False, None, servico.get_id(), profissional_id)
                horarios_criados == 1
                dt_inicial += timedelta(minutes=intervalo)
            st.success(f"{horarios_criados} horários inseridos na agenda!")
            st.rerun()