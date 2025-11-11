import json
from models.dao import DAO

class Profissional:
    def __init__(self, id, nome, especialidade, conselho, email, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_especialidade(especialidade)
        self.set_conselho(conselho)
        self.set_email(email)
        self.set_senha(senha)

    def get_id(self): return self.id
    def get_nome(self): return self.nome
    def get_especialidade(self): return self.especialidade
    def get_conselho(self): return self.conselho
    def get_email(self): return self.email
    def get_senha(self): return self.senha

    def set_id(self, id): self.id = id
    def set_nome(self, nome): self.nome = nome
    def set_especialidade(self, especialidade): self.especialidade = especialidade
    def set_conselho(self, conselho): self.conselho = conselho
    def set_email(self, email): self.email = email
    def set_senha(self, senha): self.senha = senha

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "especialidade": self.especialidade,
            "conselho": self.conselho,
            "email": self.email,
            "senha": self.senha
        }

    @staticmethod
    def from_json(dic):
        return Profissional(dic["id"], dic["nome"], dic["especialidade"], dic["conselho"], dic["email"], dic["senha"])

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.especialidade} - {self.conselho} - {self.email}"


class ProfissionalDAO(DAO):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("profissionais.json", "r") as f:
                lista = json.load(f)
                for dic in lista:
                    cls.objetos.append(Profissional.from_json(dic))
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("profissionais.json", "w") as f:
            json.dump(cls.objetos, f, default=Profissional.to_json)