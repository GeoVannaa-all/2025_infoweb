import json
from datetime import datetime

class Horario:
    def __init__(self, id, data):
        self.__id = id
        self.__data = data
        self.__confirmado = False
        self.__id_cliente = None
        self.__id_servico = None
        self.__id_profissional = None

    # getters
    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_confirmado(self): return self.__confirmado
    def get_id_cliente(self): return self.__id_cliente
    def get_id_servico(self): return self.__id_servico
    def get_id_profissional(self): return self.__id_profissional

    # setters
    def set_confirmado(self, confirmado): self.__confirmado = confirmado
    def set_id_cliente(self, id_cliente): self.__id_cliente = id_cliente
    def set_id_servico(self, id_servico): self.__id_servico = id_servico
    def set_id_profissional(self, id_profissional): self.__id_profissional = id_profissional

    def to_dict(self):
        """Converte o objeto em dicionário serializável"""
        data_str = None
        if isinstance(self.__data, datetime):
            data_str = self.__data.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(self.__data, str):
            data_str = self.__data
        else:
            data_str = str(self.__data)
        return {
            "id": self.__id,
            "data": data_str,
            "confirmado": self.__confirmado,
            "id_cliente": self.__id_cliente,
            "id_servico": self.__id_servico,
            "id_profissional": self.__id_profissional
        }

    @staticmethod
    def from_dict(d):
        """Reconstrói um objeto Horario a partir de um dicionário"""
        data = d.get("data")
        # converte para datetime se possível
        if isinstance(data, str):
            for fmt in ("%Y-%m-%d %H:%M:%S", "%d/%m/%Y %H:%M", "%Y-%m-%dT%H:%M:%S"):
                try:
                    data = datetime.strptime(data, fmt)
                    break
                except:
                    pass
        h = Horario(d.get("id"), data)
        h.set_confirmado(d.get("confirmado", False))
        h.set_id_cliente(d.get("id_cliente"))
        h.set_id_servico(d.get("id_servico"))
        h.set_id_profissional(d.get("id_profissional"))
        return h


class HorarioDAO:
    arquivo = "horarios.json"

    @staticmethod
    def salvar(lista):
        with open(HorarioDAO.arquivo, "w", encoding="utf-8") as f:
            json.dump([obj.to_dict() for obj in lista], f, indent=4, ensure_ascii=False)

    @staticmethod
    def abrir():
        try:
            with open(HorarioDAO.arquivo, "r", encoding="utf-8") as f:
                lista = json.load(f)
                return [Horario.from_dict(obj) for obj in lista]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    @staticmethod
    def listar():
        return HorarioDAO.abrir()

    @staticmethod
    def inserir(horario):
        lista = HorarioDAO.abrir()
        novo_id = max([obj.get_id() for obj in lista], default=0) + 1
        horario._Horario__id = novo_id
        lista.append(horario)
        HorarioDAO.salvar(lista)

    @staticmethod
    def atualizar(horario):
        lista = HorarioDAO.abrir()
        for i, obj in enumerate(lista):
            if obj.get_id() == horario.get_id():
                lista[i] = horario
        HorarioDAO.salvar(lista)

    @staticmethod
    def excluir(horario):
        lista = HorarioDAO.abrir()
        lista = [obj for obj in lista if obj.get_id() != horario.get_id()]
        HorarioDAO.salvar(lista)