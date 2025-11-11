import streamlit as st
from agenda import View
import time

class AbrirAgendaUI:
    @staticmethod
    def main():
        st.header("Abrir Agenda de Horários")
        data = st.text_input("Data (AAAA-MM-DD)")
        hora = st.text_input("Hora (HH:MM)")
        id_prof = st.number_input("ID do profissional", min_value=1, step=1)

        if st.button("Abrir Horário"):
            try:
                View.horario_inserir(data, hora, id_prof)
                st.success("Horário adicionado à agenda com sucesso!")
                time.sleep(1)
                try:
                    st.experimental_rerun()
                except Exception:
                    pass
            except Exception as e:
                st.error(f"Erro: {e}")