import streamlit as st
from views import View
from time import sleep

class ProfessionalProfileUI:
    """Página de Perfil do Profissional que permite ele ver e alterar seus dados."""
    @staticmethod
    def main() -> None:
        st.set_page_config(
            page_title="Meu Perfil",
            page_icon="🪪"
        )
        
        st.header("🪪 Meus Dados")

        user_id: int = st.session_state["user_id"]
        prof_data = View.get_professional(user_id)

        new_name = st.text_input("Informe o Novo Nome", prof_data.name)
        new_email = st.text_input("Informe o Novo E-mail", prof_data.email)
        new_speciality = st.text_input("Informe a Nova Especialidade", prof_data.speciality)
        new_council = st.text_input("Informe o Novo Conselho", prof_data.council)
        new_password = st.text_input("Informe a Nova Senha", prof_data.password, type="password")
        do_update = st.button("Atualizar")

        if do_update:
            try:
                View.update_professional(prof_data.id, new_name, new_email, new_speciality, new_council, new_password)
                st.success("Seus Dados foram Atualizados com Sucesso!", icon="✔")
            except Exception as e:
                st.error(f"Um Erro Ocorreu: {e}", icon="🚨")
            sleep(2)
            st.rerun()
