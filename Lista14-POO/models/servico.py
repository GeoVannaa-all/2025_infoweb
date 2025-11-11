class Servico:
    def __init__(self, id, descricao, valor):
        self.id = id
        self.descricao = descricao
        self.valor = valor

    def __str__(self):
        return f"{self.id} - {self.descricao} - R$ {self.valor:.2f}"

    def to_json(self):
        return {"id": self.id, "descricao": self.descricao, "valor": self.valor}

    @staticmethod
    def from_json(dic):
        return Servico(dic["id"], dic["descricao"], dic["valor"])