import json
from models.agendamento import Agendamento

class AgendamentoDAO:
    agendamentos = []

    @staticmethod
    def abrir():
        try:
            with open("agendamentos.json", "r", encoding="utf-8") as f:
                dados = json.load(f)
                AgendamentoDAO.agendamentos = [Agendamento.from_json(d) for d in dados]
        except (FileNotFoundError, json.JSONDecodeError):
            AgendamentoDAO.agendamentos = []

    @staticmethod
    def salvar():
        with open("agendamentos.json", "w", encoding="utf-8") as f:
            dados = [a.to_json() for a in AgendamentoDAO.agendamentos]
            json.dump(dados, f, indent=4, ensure_ascii=False)

    @staticmethod
    def inserir(agendamento):
        AgendamentoDAO.abrir()
        if not AgendamentoDAO.agendamentos:
            agendamento.id = 1
        else:
            agendamento.id = AgendamentoDAO.agendamentos[-1].id + 1
        AgendamentoDAO.agendamentos.append(agendamento)
        AgendamentoDAO.salvar()

    @staticmethod
    def listar():
        AgendamentoDAO.abrir()
        return AgendamentoDAO.agendamentos

    @staticmethod
    def atualizar(agendamento):
        AgendamentoDAO.abrir()
        for i, a in enumerate(AgendamentoDAO.agendamentos):
            if a.id == agendamento.id:
                AgendamentoDAO.agendamentos[i] = agendamento
                AgendamentoDAO.salvar()
                return