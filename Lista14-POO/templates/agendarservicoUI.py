import streamlit as st
from views import View
import time

class AgendarServicoUI:
    def main():
        st.header("Agendar Serviço")

        usuario_id = st.session_state.get("usuario_id")
        if not usuario_id:
            st.warning("Você precisa estar logado para agendar um serviço.")
            return

        profs = View.profissional_listar()
        if len(profs) == 0:
            st.write("Nenhum profissional cadastrado")
            return

        profissional = st.selectbox("Informe o profissional", profs, format_func=lambda p: f"{p.get_id()} - {p.get_nome()}")
        horarios = View.horario_agendar_horario(profissional.get_id())
        if len(horarios) == 0:
            st.write("Nenhum horário disponível")
            return

        horario = st.selectbox("Informe o horário", horarios, format_func=lambda h: f"{h.get_id()} - {h.get_data().strftime('%d/%m/%Y %H:%M')}")
        servicos = View.servico_listar()
        servico = st.selectbox("Informe o serviço", servicos, format_func=lambda s: f"{s.get_id()} - {s.get_descricao()}")

        if st.button("Agendar"):
            View.horario_atualizar(horario.get_id(), horario.get_data(), False, st.session_state.get("usuario_id"), servico.get_id(), profissional.get_id())
            st.success("Horário agendado com sucesso")
            time.sleep(2)
            st.rerun()