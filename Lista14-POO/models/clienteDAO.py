import json
from models.cliente import Cliente

class ClienteDAO:
    clientes = []

    @staticmethod
    def inserir(cliente):
        ClienteDAO.abrir()
        if len(ClienteDAO.clientes) == 0:
            cliente.id = 1
        else:
            cliente.id = ClienteDAO.clientes[-1].id + 1
        ClienteDAO.clientes.append(cliente)
        ClienteDAO.salvar()

    @staticmethod
    def listar():
        ClienteDAO.abrir()
        return ClienteDAO.clientes

    @staticmethod
    def atualizar(cliente):
        ClienteDAO.abrir()
        for i, c in enumerate(ClienteDAO.clientes):
            if c.id == cliente.id:
                ClienteDAO.clientes[i] = cliente
                ClienteDAO.salvar()
                return

    @staticmethod
    def excluir(id):
        ClienteDAO.abrir()
        ClienteDAO.clientes = [c for c in ClienteDAO.clientes if c.id != id]
        ClienteDAO.salvar()

    @staticmethod
    def abrir():
        ClienteDAO.clientes = []
        try:
            with open("clientes.json", "r") as f:
                dados = json.load(f)
                for dic in dados:
                    ClienteDAO.clientes.append(Cliente.from_json(dic))
        except FileNotFoundError:
            pass

    @staticmethod
    def salvar():
        with open("clientes.json", "w") as f:
            dados = [c.to_json() for c in ClienteDAO.clientes]
            json.dump(dados, f, indent=2)