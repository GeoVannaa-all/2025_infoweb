import json

class Profissional:
    def __init__(self, id, nome, especialidade, conselho, email, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_especialidade(especialidade)
        self.set_conselho(conselho)
        self.set_email(email)
        self.set_senha(senha)

    def get_id(self): return self.__id
    def set_id(self, id): self.__id = id

    def get_nome(self): return self.__nome
    def set_nome(self, nome): self.__nome = nome

    def get_especialidade(self): return self.__especialidade
    def set_especialidade(self, especialidade): self.__especialidade = especialidade

    def get_conselho(self): return self.__conselho
    def set_conselho(self, conselho): self.__conselho = conselho

    def get_email(self): return self.__email
    def set_email(self, email): self.__email = email

    def get_senha(self): return self.__senha
    def set_senha(self, senha): self.__senha = senha

    def __str__(self):
        return f"{self.__id} - {self.__nome} ({self.__especialidade})"

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "especialidade": self.__especialidade,
            "conselho": self.__conselho,
            "email": self.__email,
            "senha": self.__senha
        }

    @staticmethod
    def from_json(dic):
        return Profissional(dic["id"], dic["nome"], dic["especialidade"], dic["conselho"], dic["email"], dic["senha"])

class ProfissionalDAO:
    @classmethod
    def inserir(cls, profissional):
        dados = cls.listar()
        max_id = max([p.get_id() for p in dados], default=0)
        profissional.set_id(max_id + 1)
        dados.append(profissional)
        cls.__salvar(dados)

    @classmethod
    def atualizar(cls, profissional):
        dados = cls.listar()
        for i, p in enumerate(dados):
            if p.get_id() == profissional.get_id():
                dados[i] = profissional
                break
        cls.__salvar(dados)

    @classmethod
    def excluir(cls, profissional):
        dados = cls.listar()
        dados = [p for p in dados if p.get_id() != profissional.get_id()]
        cls.__salvar(dados)

    @classmethod
    def listar(cls):
        try:
            with open("profissionais.json", mode="r") as f:
                lista_dic = json.load(f)
        except FileNotFoundError:
            lista_dic = []
        return [Profissional.from_json(dic) for dic in lista_dic]

    @classmethod
    def listar_id(cls, id):
        dados = cls.listar()
        for p in dados:
            if p.get_id() == id:
                return p
        return None

    @classmethod
    def __salvar(cls, dados):
        with open("profissionais.json", mode="w") as f:
            json.dump([p.to_json() for p in dados], f, indent=4)