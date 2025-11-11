import json
from models.servico import Servico

class ServicoDAO:
    servicos = []

    @staticmethod
    def inserir(servico):
        ServicoDAO.abrir()
        if len(ServicoDAO.servicos) == 0:
            servico.id = 1
        else:
            servico.id = ServicoDAO.servicos[-1].id + 1
        ServicoDAO.servicos.append(servico)
        ServicoDAO.salvar()

    @staticmethod
    def listar():
        ServicoDAO.abrir()
        return ServicoDAO.servicos

    @staticmethod
    def atualizar(servico):
        ServicoDAO.abrir()
        for i, s in enumerate(ServicoDAO.servicos):
            if s.id == servico.id:
                ServicoDAO.servicos[i] = servico
                ServicoDAO.salvar()
                return

    @staticmethod
    def excluir(id):
        ServicoDAO.abrir()
        ServicoDAO.servicos = [s for s in ServicoDAO.servicos if s.id != id]
        ServicoDAO.salvar()

    @staticmethod
    def abrir():
        ServicoDAO.servicos = []
        try:
            with open("servicos.json", "r") as f:
                dados = json.load(f)
                for dic in dados:
                    ServicoDAO.servicos.append(Servico.from_json(dic))
        except FileNotFoundError:
            pass

    @staticmethod
    def salvar():
        with open("servicos.json", "w") as f:
            dados = [s.to_json() for s in ServicoDAO.servicos]
            json.dump(dados, f)