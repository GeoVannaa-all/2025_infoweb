import json
from models.profissional import Profissional

class ProfissionalDAO:
    profissionais = []

    @staticmethod
    def abrir():
        try:
            with open("profissionais.json", "r", encoding="utf-8") as f:
                dados = json.load(f)
                ProfissionalDAO.profissionais = [Profissional.from_json(d) for d in dados]
        except (FileNotFoundError, json.JSONDecodeError):
            ProfissionalDAO.profissionais = []

    @staticmethod
    def salvar():
        with open("profissionais.json", "w", encoding="utf-8") as f:
            dados = [p.to_json() for p in ProfissionalDAO.profissionais]
            json.dump(dados, f, indent=4, ensure_ascii=False)

    @staticmethod
    def inserir(profissional):
        ProfissionalDAO.abrir()
        if len(ProfissionalDAO.profissionais) == 0:
            profissional.id = 1
        else:
            profissional.id = ProfissionalDAO.profissionais[-1].id + 1
        ProfissionalDAO.profissionais.append(profissional)
        ProfissionalDAO.salvar()

    @staticmethod
    def listar():
        ProfissionalDAO.abrir()
        return ProfissionalDAO.profissionais

    @staticmethod
    def atualizar(profissional):
        ProfissionalDAO.abrir()
        for i, p in enumerate(ProfissionalDAO.profissionais):
            if p.id == profissional.id:
                ProfissionalDAO.profissionais[i] = profissional
                ProfissionalDAO.salvar()
                return

    @staticmethod
    def excluir(id):
        ProfissionalDAO.abrir()
        ProfissionalDAO.profissionais = [p for p in ProfissionalDAO.profissionais if p.id != id]
        ProfissionalDAO.salvar()

    @staticmethod
    def autenticar(email, senha):
        ProfissionalDAO.abrir()
        for p in ProfissionalDAO.profissionais:
            if p.email == email and p.senha == senha:
                return p
        return None