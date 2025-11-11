class Horario:
    def __init__(self, id, data, hora, id_profissional):
        ano = int(str(data)[:4])
        if ano < 2025:
            raise ValueError("A data deve ser igual ou posterior a 2025.")
        self.__id = id
        self.__data = data
        self.__hora = hora
        self.__id_profissional = id_profissional

    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_hora(self):
        return self.__hora

    def get_id_profissional(self):
        return self.__id_profissional

    def set_data(self, data):
        ano = int(str(data)[:4])
        if ano < 2025:
            raise ValueError("A data deve ser igual ou posterior a 2025.")
        self.__data = data

    def set_hora(self, hora):
        self.__hora = hora

    def set_id_profissional(self, id_profissional):
        self.__id_profissional = id_profissional

    def __str__(self):
        return f"{self.__id} - {self.__data} {self.__hora} - Profissional {self.__id_profissional}"

    def to_json(self):
        return {
            "id": self.__id,
            "data": self.__data,
            "hora": self.__hora,
            "id_profissional": self.__id_profissional
        }

    @staticmethod
    def from_json(dic):
        return Horario(dic.get("id"), dic.get("data"), dic.get("hora"), dic.get("id_profissional"))