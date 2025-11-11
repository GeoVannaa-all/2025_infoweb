import json
from models.dao import DAO

class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)

    def get_id(self): return self.id
    def get_nome(self): return self.nome
    def get_email(self): return self.email
    def get_fone(self): return self.fone
    def get_senha(self): return self.senha

    def set_id(self, id): self.id = id
    def set_nome(self, nome): self.nome = nome
    def set_email(self, email): self.email = email
    def set_fone(self, fone): self.fone = fone
    def set_senha(self, senha): self.senha = senha

    def to_json(self):
        return {"id": self.id, "nome": self.nome, "email": self.email, "fone": self.fone, "senha": self.senha}

    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["senha"])

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"


class ClienteDAO(DAO):
    objetos = []

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("clientes.json", "r") as f:
                dados = json.load(f)
                for dic in dados:
                    cls.objetos.append(Cliente.from_json(dic))
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("clientes.json", "w") as f:
            json.dump(cls.objetos, f, default=Cliente.to_json)