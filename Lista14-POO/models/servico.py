import json
from models.dao import DAO

class Servico:
    def __init__(self, id, descricao, valor):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_valor(valor)

    def get_id(self): return self.id
    def get_descricao(self): return self.descricao
    def get_valor(self): return self.valor

    def set_id(self, id): self.id = id
    def set_descricao(self, descricao): self.descricao = descricao
    def set_valor(self, valor): self.valor = valor

    def to_json(self):
        return {"id": self.id, "descricao": self.descricao, "valor": self.valor}

    @staticmethod
    def from_json(dic):
        return Servico(dic["id"], dic["descricao"], dic["valor"])

    def __str__(self):
        return f"{self.id} - {self.descricao} - R$ {self.valor:.2f}"


class ServicoDAO(DAO):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("servicos.json", "r") as f:
                lista = json.load(f)
                for dic in lista:
                    cls.objetos.append(Servico.from_json(dic))
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("servicos.json", "w") as f:
            json.dump(cls.objetos, f, default=Servico.to_json)