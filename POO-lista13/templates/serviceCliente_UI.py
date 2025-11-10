import streamlit as st
from views import View
from time import sleep

class SetServiceClientUI:
    """Página do Cliente de Agendar um Serviço."""
    @staticmethod
    def main() -> None:
        st.set_page_config(
            page_title="Agendar Serviço",
            page_icon="📅"
        )
        
        st.header("📅 Agendar Serviço")

        user_id: int = st.session_state["user_id"]
        client_data = View.get_client(user_id)

        profs_list = View.get_professional_list()
        services_list = View.get_service_list()

        if len(profs_list) <= 0:
            st.write("Nenhum Profissional Cadastrado. Volte mais Tarde.")
            return
        elif len(services_list) <= 0:
            st.write("Nenhum Serviço Cadastrado. Volte mais Tarde.")
            return

        prof = st.selectbox("Informe o Profissional", profs_list)
        schedule = st.selectbox("Informe o Horário", View.get_schedules_to_setting(prof.id))
        service = st.selectbox("Informe o Serviço", services_list)
        
        if len(View.get_schedules_to_setting(prof.id)) <= 0:
            st.write("Nenhum Horário Disponível para esse Profissional.")
            return
        
        set_schedule = st.button("Agendar")

        if set_schedule:
            try:
                View.update_schedule(schedule.id, schedule.date, schedule.confirmed, client_data, service, prof)
                st.success("Horário Agendado com Sucesso!", icon="✔")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}", icon="🚨")
            sleep(1)
            st.rerun()
