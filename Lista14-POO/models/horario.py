import json
from datetime import datetime
from models.dao import DAO
from datetime import datetime
from datetime import datetime
import json

class Horario:
    def __init__(self, id, data):
        self.__id = id
        self.__data = data
        self.__confirmado = False
        self.__id_cliente = None
        self.__id_servico = None
        self.__id_profissional = None
        self.__comentario = ""

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_confirmado(self): return self.__confirmado
    def get_id_cliente(self): return self.__id_cliente
    def get_id_servico(self): return self.__id_servico
    def get_id_profissional(self): return self.__id_profissional
    def get_comentario(self): return self.__comentario

    def set_id(self, id): self.__id = id
    def set_confirmado(self, confirmado): self.__confirmado = confirmado
    def set_id_cliente(self, id_cliente): self.__id_cliente = id_cliente
    def set_id_servico(self, id_servico): self.__id_servico = id_servico
    def set_id_profissional(self, id_profissional): self.__id_profissional = id_profissional
    def set_comentario(self, comentario): self.__comentario = comentario

    def __str__(self):
        return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - Confirmado: {self.__confirmado}"

    def to_json(self):
        return {
            "id": self.__id,
            "data": self.__data.strftime("%d/%m/%Y %H:%M"),
            "confirmado": self.__confirmado,
            "id_cliente": self.__id_cliente,
            "id_servico": self.__id_servico,
            "id_profissional": self.__id_profissional,
            "comentario": self.__comentario
        }

    @classmethod
    def from_json(cls, dic):
        raw = dic.get("data")
        formats = [
            "%d/%m/%Y %H:%M",
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%dT%H:%M:%S",
            "%Y-%m-%d %H:%M",
            "%d/%m/%Y %H:%M:%S"
        ]

        data = None
        if raw is None:
            data = datetime.now()
        else:
            if isinstance(raw, datetime):
                data = raw
            else:
                for fmt in formats:
                    try:
                        data = datetime.strptime(raw, fmt)
                        break
                    except Exception:
                        continue
                if data is None:
                    try:
                        data = datetime.fromisoformat(raw)
                    except Exception:
                        data = datetime.now()

        h = Horario(dic.get("id", 0), data)
        h.set_confirmado(dic.get("confirmado", False))
        h.set_id_cliente(dic.get("id_cliente"))
        h.set_id_servico(dic.get("id_servico"))
        h.set_id_profissional(dic.get("id_profissional"))
        h.set_comentario(dic.get("comentario", ""))
        return h



    @classmethod
    def from_json(cls, dic):
        raw = dic.get("data")
        formats = [
            "%d/%m/%Y %H:%M",       
            "%Y-%m-%d %H:%M:%S",   
            "%Y-%m-%dT%H:%M:%S",    
            "%Y-%m-%d %H:%M",      
            "%d/%m/%Y %H:%M:%S"    
        ]
        data = None
        if raw is None:
            data = datetime.now()
        else:
            if isinstance(raw, datetime):
                data = raw
            else:
                for fmt in formats:
                    try:
                        data = datetime.strptime(raw, fmt)
                        break
                    except Exception:
                        continue
                if data is None:
                    try:
                        data = datetime.fromisoformat(raw)
                    except Exception:
                        data = datetime.now()

        h = Horario(dic.get("id", 0), data)
        h.set_confirmado(dic.get("confirmado", False))
        h.set_id_cliente(dic.get("id_cliente"))
        h.set_id_servico(dic.get("id_servico"))
        h.set_id_profissional(dic.get("id_profissional"))
        h.set_comentario(dic.get("comentario", ""))
        return h




class HorarioDAO(DAO):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("horarios.json", "r") as f:
                lista = json.load(f)
                for dic in lista:
                    cls.objetos.append(Horario.from_json(dic))
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("horarios.json", "w") as f:
            json.dump(cls.objetos, f, default=Horario.to_json)