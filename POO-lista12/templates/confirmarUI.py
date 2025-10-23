import streamlit as st
from views import View

class ConfirmarServicoUI:
    def main():
        st.header("Confirmar Serviço")

        if "usuario_id" not in st.session_state:
            st.error("Nenhum profissional logado.")
            return

        id_profissional = st.session_state["usuario_id"]

        horarios = View.horario_filtrar_profissional(id_profissional)
        if len(horarios) == 0:
            st.info("Nenhum horário disponível para confirmação.")
            return

        opcoes_horarios = []
        for h in horarios:
            cliente = View.cliente_listar_id(h.get_id_cliente())
            cliente_nome = cliente.get_nome() if cliente else "Sem cliente"
            opcoes_horarios.append(f"{h.get_id()} - {h.get_data()} - Confirmado: {h.get_confirmado()}")

        opcao_horario = st.selectbox("Informe o horário para confirmar", opcoes_horarios)
        id_horario = int(opcao_horario.split(" - ")[0])
        horario = View.horario_listar_id(id_horario)

        clientes = View.cliente_listar()
        opcoes_clientes = []
        for c in clientes:
            opcoes_clientes.append(f"{c.get_id()} - {c.get_nome()} - {c.get_email()} - {c.get_fone()}")

        cliente_escolhido = st.selectbox("Cliente", opcoes_clientes, index=0 if len(opcoes_clientes) > 0 else None)

        if st.button("Confirmar"):
            if horario is None:
                st.error("Horário inválido.")
                return

            horario.set_confirmado(True)
            View.horario_atualizar(horario)
            st.success("Serviço confirmado com sucesso!")

            st.rerun()