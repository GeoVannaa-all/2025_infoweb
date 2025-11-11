import streamlit as st
from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterprofissionalUI import ManterProfissionalUI
from templates.alterarsenhaUI import AlterarSenhaUI
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.loginprofissionalUI import LoginProfissionalUI
from templates.perfilclienteUI import PerfilClienteUI
from templates.perfilprofissionalUI import PerfilProfissionalUI
from templates.agendarservicoUI import AgendarServicoUI
from templates.visualizaragendaUI import VisualizarAgendaUI
from templates.visualizarservicoUI import VisualizarServicoUI
from templates.confirmarservicoUI import ConfirmarServicoUI


from views import View

if "usuario_id" not in st.session_state:
    st.session_state["usuario_id"] = None
if "usuario_nome" not in st.session_state:
    st.session_state["usuario_nome"] = None

class IndexUI:
    @staticmethod
    def main():
        View.cliente_criar_admin()
        IndexUI.sidebar()

    @staticmethod
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar como Cliente", "Entrar como Profissional", "Abrir Conta"])
        if op == "Entrar como Cliente":
            LoginUI.main()
        elif op == "Entrar como Profissional":
            LoginProfissionalUI.main()
        elif op == "Abrir Conta":
            AbrirContaUI.main()

    @staticmethod
    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Agendar Serviço", "Meus Serviços"])
        if op == "Meus Dados":
            PerfilClienteUI.main()
        elif op == "Agendar Serviço":
            AgendarServicoUI.main()
        elif op == "Meus Serviços":
            VisualizarServicoUI.main()


    @staticmethod
    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Gerenciar Agenda", "Confirmar Serviço"])
        if op == "Meus Dados":
            PerfilProfissionalUI.main()
        elif op == "Gerenciar Agenda":
            VisualizarAgendaUI.main()
        elif op == "Confirmar Serviço":
            ConfirmarServicoUI.main()

    @staticmethod
    def menu_admin():
        op = st.sidebar.selectbox(
            "Menu do Administrador",
            ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais", "Alterar Senha"]
        )
        if op == "Cadastro de Clientes":
            ManterClienteUI.main()
        elif op == "Cadastro de Serviços":
            ManterServicoUI.main()
        elif op == "Cadastro de Horários":
            ManterHorarioUI.main()
        elif op == "Cadastro de Profissionais":
            ManterProfissionalUI.main()
        elif op == "Alterar Senha":
            AlterarSenhaUI.main()

    @staticmethod
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            st.session_state["usuario_id"] = None
            st.session_state["usuario_nome"] = None
            st.rerun()

    @staticmethod
    def sidebar():
        if not st.session_state.get("usuario_id"):
            IndexUI.menu_visitante()
        else:
            admin = st.session_state.get("usuario_nome") == "Administrador"
            profissional = not admin and View.profissional_listar_id(st.session_state.get("usuario_id")) is not None
            st.sidebar.write(f"Bem-vindo(a), {st.session_state.get('usuario_nome')}!")

            if admin:
                IndexUI.menu_admin()
            elif profissional:
                IndexUI.menu_profissional()
            else:
                IndexUI.menu_cliente()

            IndexUI.sair_do_sistema()

if __name__ == "__main__":
    IndexUI.main()