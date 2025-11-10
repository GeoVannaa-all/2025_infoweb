import streamlit as st
from views import View
from time import sleep

class ConfirmScheduleProfessionalUI:
    """Página do Profissional de Confirmar um Serviço."""
    @staticmethod
    def main() -> None:
        st.set_page_config(
            page_title="Confirmar Serviço",
            page_icon="🖊️"
        )
        
        st.header("🖊️ Confirmar Serviço")

        user_id: int = st.session_state["user_id"]
        prof_data = View.get_professional(user_id)

        schedules = View.get_schedules_by_professional(prof_data.id)
        schedule = st.selectbox("Informe o Horário", schedules)
        schedule_client = View.get_client(schedule.client_id)
        client = st.text_input("Cliente", schedule_client, disabled=True)
        if not schedule_client: return

        do_confirmation = st.button("Confirmar" if not schedule.confirmed else "Desmarcar")

        if do_confirmation:
            try:
                View.update_schedule(schedule.id, schedule.date, not schedule.confirmed, schedule_client, View.get_service(schedule.service_id), prof_data)
                st.success(f"Horário {'Confirmado' if not schedule.confirmed else 'Desmarcado'} com Sucesso!", icon="✔")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}", icon="🚨")
            sleep(2)
            st.rerun()
