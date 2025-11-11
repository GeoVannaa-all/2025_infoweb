import streamlit as st
import pandas as pd
import time
from agenda import View

class ManterHorarioUI:
    @staticmethod
    def main():
        st.header("Gerenciamento de Horários")
        aba1, aba2, aba3, aba4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with aba1:
            ManterHorarioUI.listar()
        with aba2:
            ManterHorarioUI.inserir()
        with aba3:
            ManterHorarioUI.atualizar()
        with aba4:
            ManterHorarioUI.excluir()

    @staticmethod
    def listar():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.info("Nenhum horário cadastrado.")
            return
        tabela = [h.to_json() for h in horarios]
        df = pd.DataFrame(tabela)
        st.dataframe(df)

    @staticmethod
    def inserir():
        data = st.text_input("Data (AAAA-MM-DD)")
        hora = st.text_input("Hora (HH:MM)")
        id_prof = st.number_input("ID do profissional", min_value=1, step=1)
        if st.button("Inserir Horário"):
            try:
                View.horario_inserir(data, hora, id_prof)
                st.success("Horário inserido com sucesso!")
                time.sleep(1)
                try:
                    st.experimental_rerun()
                except Exception:
                    pass
            except Exception as e:
                st.error(f"Erro: {e}")

    @staticmethod
    def atualizar():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.info("Nenhum horário cadastrado.")
            return

        def fmt(h):
            d = h.get_data() if hasattr(h, "get_data") else getattr(h, "data", "")
            ho = h.get_hora() if hasattr(h, "get_hora") else getattr(h, "hora", "")
            return f"{d} {ho}"

        op = st.selectbox("Escolha um horário", horarios, format_func=fmt)

        data_default = op.get_data() if hasattr(op, "get_data") else getattr(op, "data", "")
        hora_default = op.get_hora() if hasattr(op, "get_hora") else getattr(op, "hora", "")
        id_prof_default = op.get_id_profissional() if hasattr(op, "get_id_profissional") else getattr(op, "id_profissional", 1)

        data = st.text_input("Nova data (AAAA-MM-DD)", data_default)
        hora = st.text_input("Nova hora (HH:MM)", hora_default)
        id_prof = st.number_input("ID do profissional", value=id_prof_default, min_value=1, step=1)

        if st.button("Atualizar Horário"):
            try:
                op_id = op.get_id() if hasattr(op, "get_id") else getattr(op, "id", None)
                View.horario_atualizar(op_id, data, hora, id_prof)
                st.success("Horário atualizado com sucesso!")
                time.sleep(1)
                try:
                    st.experimental_rerun()
                except Exception:
                    pass
            except Exception as e:
                st.error(f"Erro: {e}")

    @staticmethod
    def excluir():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.info("Nenhum horário cadastrado.")
            return

        def fmt(h):
            d = h.get_data() if hasattr(h, "get_data") else getattr(h, "data", "")
            ho = h.get_hora() if hasattr(h, "get_hora") else getattr(h, "hora", "")
            return f"{d} {ho}"

        op = st.selectbox("Escolha um horário para excluir", horarios, format_func=fmt)
        if st.button("Excluir Horário"):
            try:
                op_id = op.get_id() if hasattr(op, "get_id") else getattr(op, "id", None)
                View.horario_excluir(op_id)
                st.success("Horário excluído com sucesso!")
                time.sleep(1)
                try:
                    st.experimental_rerun()
                except Exception:
                    pass
            except Exception as e:
                st.error(f"Erro: {e}")