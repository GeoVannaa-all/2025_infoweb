import json
from models.horario import Horario

class HorarioDAO:
    horarios = []

    @staticmethod
    def abrir():
        try:
            with open("horarios.json", "r", encoding="utf-8") as f:
                dados = json.load(f)
                HorarioDAO.horarios = [Horario.from_json(d) for d in dados]
        except (FileNotFoundError, json.JSONDecodeError):
            HorarioDAO.horarios = []

    @staticmethod
    def salvar():
        with open("horarios.json", "w", encoding="utf-8") as f:
            dados = [h.to_json() for h in HorarioDAO.horarios]
            json.dump(dados, f, indent=4, ensure_ascii=False)

    @staticmethod
    def inserir(horario):
        HorarioDAO.abrir()
        if not HorarioDAO.horarios:
            new_id = 1
        else:
            last = HorarioDAO.horarios[-1]
            last_id = last.get_id() if hasattr(last, "get_id") else getattr(last, "id", 0)
            new_id = (last_id or 0) + 1

        # atualiza o id interno do objeto Horario
        try:
            setattr(horario, "_Horario__id", new_id)
        except Exception:
            setattr(horario, "id", new_id)

        HorarioDAO.horarios.append(horario)
        HorarioDAO.salvar()

    @staticmethod
    def listar():
        HorarioDAO.abrir()
        return HorarioDAO.horarios

    @staticmethod
    def atualizar(horario):
        HorarioDAO.abrir()
        target_id = horario.get_id() if hasattr(horario, "get_id") else getattr(horario, "id", None)
        for i, h in enumerate(HorarioDAO.horarios):
            h_id = h.get_id() if hasattr(h, "get_id") else getattr(h, "id", None)
            if h_id == target_id:
                HorarioDAO.horarios[i] = horario
                HorarioDAO.salvar()
                return

    @staticmethod
    def excluir(id):
        HorarioDAO.abrir()
        HorarioDAO.horarios = [h for h in HorarioDAO.horarios
                               if (h.get_id() if hasattr(h, "get_id") else getattr(h, "id", None)) != id]
        HorarioDAO.salvar()