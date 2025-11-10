from .abc_dao import AbstractDAO
from typing import Any

class Service:
    def __init__(self, service_id: int, description: str, value: float) -> None:
        self.id = service_id
        self.description = description
        self.value = value
    
    @property
    def id(self) -> int: return self.__id

    @id.setter
    def id(self, service_id: int) -> None:
        if not isinstance(service_id, int): raise TypeError("ID needs to be an INT.")
        if service_id < 0: raise ValueError("ID can't be negative.")

        self.__id = service_id

    @property
    def description(self) -> str: return self.__description

    @description.setter
    def description(self, description: str) -> None:
        description = description.strip()
        if description == "": raise ValueError("Description can't be empty.")

        self.__description = description

    @property
    def value(self) -> float: return self.__value

    @value.setter
    def value(self, value: float) -> None:
        if not isinstance(value, (int, float)): raise TypeError("Value needs to be a Number.")

        self.__value = value

    def __str__(self) -> str:
        return f"Serviço {self.id}: '{self.description}' - {self.value}"

    def to_json(self) -> dict[str, Any]:
        """Converte os dados do Objeto para JSON."""
        return {
            "id": self.id,
            "description": self.description,
            "value": self.value
        }

    @staticmethod
    def from_json(data: dict[str, Any]) -> "Service":
        """Ler dados JSON e converte para um Objeto dessa Classe."""
        return Service(data["id"], data["description"], data["value"])

class ServiceDAO(AbstractDAO):
    _objects: list[Service] = []
    _json_file_path_str: str = "../data/services.json"
    _from_json_method = Service.from_json
