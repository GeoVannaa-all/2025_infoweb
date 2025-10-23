import streamlit as st
from views import View
import pandas as pd

class VisualizarAgendaUI:
    def main():
        st.header("Meus Serviços")

        if "usuario_id" not in st.session_state:
            st.error("Nenhum profissional logado.")
            return

        id_profissional = st.session_state["usuario_id"]

        horarios = View.horario_filtrar_profissional(id_profissional)

        if len(horarios) == 0:
            st.info("Nenhum serviço agendado ainda.")
        else:
            dados = []
            for h in horarios:
                cliente = View.cliente_listar_id(h.get_id_cliente())
                servico = View.servico_listar_id(h.get_id_servico())

                dados.append({
                    "ID": h.get_id(),
                    "Data": h.get_data().strftime("%d/%m/%Y %H:%M") if h.get_data() else "",
                    "Confirmado": True if h.get_confirmado() else False,
                    "Cliente": cliente.get_nome() if cliente else None,
                    "Serviço": servico.get_descricao() if servico else None
                })

            df = pd.DataFrame(dados)
            st.dataframe(df, use_container_width=True)