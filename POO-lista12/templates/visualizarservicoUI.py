import streamlit as st
from views import View
import pandas as pd

class VisualizarServicosUI:
    def main():
        st.header("Meus Serviços")

        if "usuario_id" not in st.session_state:
            st.error("Nenhum cliente logado.")
            return

        id_cliente = st.session_state["usuario_id"]

        horarios = View.horario_filtrar_cliente(id_cliente)

        if len(horarios) == 0:
            st.info("Nenhum serviço agendado ainda.")
        else:
            dados = []
            for h in horarios:
                profissional = View.profissional_listar_id(h.get_id_profissional())
                servico = View.servico_listar_id(h.get_id_servico())

                dados.append({
                    "ID": h.get_id(),
                    "Data": h.get_data().strftime("%d/%m/%Y %H:%M") if h.get_data() else "",
                    "Confirmado": True if h.get_confirmado() else False,
                    "Profissional": profissional.get_nome() if profissional else None,
                    "Serviço": servico.get_descricao() if servico else None
                })

            df = pd.DataFrame(dados)
            st.dataframe(df, use_container_width=True)