from templates import (
    LoginUI, SigninUI, ClientProfileUI, ScheduleClientUI,
    SetServiceClientUI, ProfessionalProfileUI, ScheduleProfessionalUI,
    SetScheduleProfessionalUI, ConfirmScheduleProfessionalUI,
    ClienteUI, KeepServiceUI, KeepScheduleUI, KeepProfessionalUI,
    AdminProfileUI)
    
from views import View
import streamlit as st

class IndexUI:
    @staticmethod
    def menu_visitor() -> None:
        st.sidebar.header("Menu de Visitante")

        op = st.sidebar.selectbox("Menu", ["Entrar no Site", "Criar Conta"])

        if op == "Entrar no Site": LoginUI.main()
        elif op == "Criar Conta": SigninUI.main()
    
    @staticmethod
    def menu_client() -> None:
        st.sidebar.header("Menu de Cliente")

        op = st.sidebar.selectbox("Menu", ["Visualizar Perfil", "Visualizar Horários", "Agendar Horário"])

        if op == "Visualizar Perfil": ClientProfileUI.main()
        elif op == "Visualizar Horários": ScheduleClientUI.main()
        elif op == "Agendar Horário": SetServiceClientUI.main()
    
    @staticmethod
    def menu_professional() -> None:
        st.sidebar.header("Menu de Profissional")

        op = st.sidebar.selectbox("Menu", ["Visualizar Perfil", "Visualizar Horários", "Abrir Agenda", "Confirmar Serviço"])

        if op == "Visualizar Perfil": ProfessionalProfileUI.main()
        elif op == "Visualizar Horários": ScheduleProfessionalUI.main()
        elif op == "Abrir Agenda": SetScheduleProfessionalUI.main()
        elif op == "Confirmar Serviço": ConfirmScheduleProfessionalUI.main()
    
    @staticmethod
    def menu_admin() -> None:
        st.sidebar.header("Menu de Admin")

        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais", "Visualizar Perfil"])
        
        if op == "Cadastro de Clientes": ClienteUI.main()
        elif op == "Cadastro de Serviços": KeepServiceUI.main()
        elif op == "Cadastro de Horários": KeepScheduleUI.main()
        elif op == "Cadastro de Profissionais": KeepProfessionalUI.main()
        elif op == "Visualizar Perfil": AdminProfileUI.main()

    @staticmethod
    def log_out_sidebar() -> None:
        """Coloca o botão de 'sair da conta' no Sidebar."""
        if st.sidebar.button("Sair", type="primary"):
           st.session_state.pop("user_id", None)
           st.session_state.pop("user_type", None)
        st.rerun()

    @staticmethod
    def sidebar() -> None:
        """Mostra o sidebar."""
        users_type = View.get_users_type()
        
        if "user_id" not in st.session_state:
            IndexUI.menu_visitor()
        else:
            match st.session_state["user_type"]:
                case users_type.CLIENT: IndexUI.menu_client()
                case users_type.PROFESSIONAL: IndexUI.menu_professional()
                case users_type.ADMIN: IndexUI.menu_admin()
            
            IndexUI.log_out_sidebar()

    @staticmethod
    def main() -> None:
        IndexUI.sidebar()

if __name__ == "__main__":
    IndexUI.main()
