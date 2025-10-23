from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterprofissionalUI import ManterProfissionalUI
from templates.abrircontaUI import AbrirContaUI
from templates.agendarUI import AgendarServicoUI
from templates.loginUI import LoginUI
from templates.perfilUI import PerfilClienteUI
from templates.perfilproUI import PerfilProfissionalUI
from templates.abriragendaUI import AbrirAgendaUI
from templates.visualizaragendaUI import VisualizarAgendaUI
from templates.visualizarservicoUI import VisualizarServicosUI
from templates.confirmarUI import ConfirmarServicoUI
from templates.alterarsenhaUI import AlterarSenhaUI
from views import View
import streamlit as st

class IndexUI:
    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            admin = st.session_state["usuario_nome"] == "admin"
            tipo = st.session_state.get("tipo_usuario", "")


            if admin:
                IndexUI.menu_admin()
            elif tipo == "profissional":
                IndexUI.menu_profissional()
            else:
                IndexUI.menu_cliente()

            IndexUI.sair_do_sistema()

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Agendar Serviço", "Visualizar Serviços"])
        if op == "Meus Dados": PerfilClienteUI.main()
        if op == "Agendar Serviço": AgendarServicoUI.main()
        if op == "Visualizar Serviços": VisualizarServicosUI.main()
            
    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Abrir Minha Agenda", "Visualizar Agenda", "Confirmar Serviço"])
        if op == "Meus Dados": PerfilProfissionalUI.main()
        if op == "Abrir Minha Agenda": AbrirAgendaUI.main()
        if op == "Visualizar Agenda": VisualizarAgendaUI.main()
        if op == "Confirmar Serviço": ConfirmarServicoUI.main()

    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais", "Alterar Senha"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        if op == "Alterar Senha": AlterarSenhaUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()

    def main():
        # verifica a existe o usuário admin
        View.cliente_criar_admin()
        # monta o sidebar
        IndexUI.sidebar()

IndexUI.main()