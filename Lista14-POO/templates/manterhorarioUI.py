import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime

class ManterHorarioUI:
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterHorarioUI.listar()
        with tab2: ManterHorarioUI.inserir()
        with tab3: ManterHorarioUI.atualizar()
        with tab4: ManterHorarioUI.excluir()

    def listar():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            dic = []
            for obj in horarios:
                cliente = View.cliente_listar_id(obj.get_id_cliente())
                servico = View.servico_listar_id(obj.get_id_servico())
                profissional = View.profissional_listar_id(obj.get_id_profissional())
                cliente_nome = cliente.get_nome() if cliente else None
                profissional_nome = profissional.get_nome() if profissional else None
                servico_desc = servico.get_descricao() if servico else None
                dic.append({
                    "id" : obj.get_id(),
                    "data" : obj.get_data(),
                    "confirmado" : obj.get_confirmado(),
                    "cliente" : cliente_nome,
                    "serviço" : servico_desc,
                    "profissional" : profissional_nome
                })
            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index=True)

    def inserir():
        clientes = View.cliente_listar()
        servicos = View.servico_listar()
        profissionais = View.profissional_listar()
        data = st.text_input("Informe a data e horário do serviço", datetime.now().strftime("%d/%m/%Y %H:%M"))
        confirmado = st.checkbox("Confirmado")
        cliente = st.selectbox("Informe o cliente", clientes, index = None, format_func=lambda c: f"{c.get_id()} - {c.get_nome()}" if c else "")
        profissional = st.selectbox("Informe o profissional", profissionais, index = None, format_func=lambda p: f"{p.get_id()} - {p.get_nome()}" if p else "")
        servico = st.selectbox("Informe o serviço", servicos, index = None, format_func=lambda s: f"{s.get_id()} - {s.get_descricao()}" if s else "")
        if st.button("Inserir"):
            id_cliente = cliente.get_id() if cliente else None
            id_profissional = profissional.get_id() if profissional else None
            id_servico = servico.get_id() if servico else None
            View.horario_inserir(datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico, id_profissional)
            st.success("Horário inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
            return
        clientes = View.cliente_listar()
        profissionais = View.profissional_listar()
        servicos = View.servico_listar()
        op = st.selectbox("Atualização de Horários", horarios, format_func=lambda h: f"{h.get_id()} - {h.get_data().strftime('%d/%m/%Y %H:%M')}")
        data = st.text_input("Informe a nova data e horário do serviço", op.get_data().strftime("%d/%m/%Y %H:%M"))
        confirmado = st.checkbox("Nova confirmação", op.get_confirmado())

        id_cliente = None if op.get_id_cliente() in [0, None] else op.get_id_cliente()
        id_profissional = None if op.get_id_profissional() in [0, None] else op.get_id_profissional()
        id_servico = None if op.get_id_servico() in [0, None] else op.get_id_servico()

        cliente = st.selectbox("Informe o novo cliente", clientes, index= next((i for i, c in enumerate(clientes) if c.get_id() == id_cliente), None), format_func=lambda c: f"{c.get_id()} - {c.get_nome()}" if c else "")
        profissional = st.selectbox("Informe o novo profissional", profissionais, index= next((i for i, p in enumerate(profissionais) if p.get_id() == id_profissional), None), format_func=lambda p: f"{p.get_id()} - {p.get_nome()}" if p else "")
        servico = st.selectbox("Informe o novo serviço", servicos, index= next((i for i, s in enumerate(servicos) if s.get_id() == id_servico), None), format_func=lambda s: f"{s.get_id()} - {s.get_descricao()}" if s else "")

        if st.button("Atualizar"):
            id_cliente = cliente.get_id() if cliente else None
            id_profissional = profissional.get_id() if profissional else None
            id_servico = servico.get_id() if servico else None
            View.horario_atualizar(op.get_id(), datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico, id_profissional)
            st.success("Horário atualizado com sucesso")

    def excluir():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
            return
        op = st.selectbox("Exclusão de Horários", horarios, format_func=lambda h: f"{h.get_id()} - {h.get_data().strftime('%d/%m/%Y %H:%M')}")
        if st.button("Excluir"):
            View.horario_excluir(op.get_id())
            st.success("Horário excluído com sucesso")
            time.sleep(2)
            st.rerun()