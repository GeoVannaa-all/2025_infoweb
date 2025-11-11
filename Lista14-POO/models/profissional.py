class Profissional:
    def __init__(self, id, nome, especialidade, fone, email, senha):
        if nome.strip() == "":
            raise ValueError("O nome não pode ficar vazio.")
        if email.strip() == "":
            raise ValueError("O e-mail não pode ficar vazio.")
        if senha.strip() == "":
            raise ValueError("A senha não pode ficar vazia.")

        self.__id = id
        self.__nome = nome
        self.__especialidade = especialidade
        self.__fone = fone
        self.__email = email
        self.__senha = senha

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_especialidade(self):
        return self.__especialidade

    def get_fone(self):
        return self.__fone

    def get_email(self):
        return self.__email

    def get_senha(self):
        return self.__senha

    def set_nome(self, nome):
        if nome.strip() == "":
            raise ValueError("O nome não pode ficar vazio.")
        self.__nome = nome

    def set_especialidade(self, esp):
        self.__especialidade = esp

    def set_fone(self, fone):
        self.__fone = fone

    def set_email(self, email):
        if email.strip() == "":
            raise ValueError("O e-mail não pode ficar vazio.")
        self.__email = email

    def set_senha(self, senha):
        if senha.strip() == "":
            raise ValueError("A senha não pode ficar vazia.")
        self.__senha = senha

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "especialidade": self.__especialidade,
            "fone": self.__fone,
            "email": self.__email,
            "senha": self.__senha
        }

    @staticmethod
    def from_json(dic):
        return Profissional(
            dic["id"],
            dic["nome"],
            dic["especialidade"],
            dic["fone"],
            dic["email"],
            dic["senha"]
        )

    def __str__(self):
        return f"{self.__id} - {self.__nome} ({self.__especialidade})"