from .abc_dao import AbstractDAO
from datetime import datetime
from typing import Any

class Schedule:
    def __init__(self, schedule_id: int, date: datetime, confirmed: bool = False, client_id: int = 0, service_id: int = 0, professional_id: int = 0) -> None:
        self.id = schedule_id
        self.date = date
        self.confirmed = confirmed
        self.client_id = client_id
        self.service_id = service_id
        self.professional_id = professional_id

    @property
    def id(self) -> int: return self.__id

    @id.setter
    def id(self, new_id: int) -> None:
        if not isinstance(new_id, int): raise TypeError("ID needs to be an Integer.")
        if new_id < 0: raise ValueError("ID needs to be greater than Zero.")

        self.__id = new_id

    @property
    def date(self) -> datetime: return self.__date

    @date.setter
    def date(self, new_date: datetime) -> None:
        if not isinstance(new_date, datetime): raise TypeError("Date needs to be a Datetime.")
        if new_date < datetime(2025, 1, 1): raise ValueError("Date too long ago.")

        self.__date = new_date

    @property
    def confirmed(self) -> bool: return self.__confirmed

    @confirmed.setter
    def confirmed(self, new_confirmed: bool) -> None:
        if not isinstance(new_confirmed, bool): raise TypeError("Confirmed needs to be a Boolean.")

        self.__confirmed = new_confirmed

    @property
    def client_id(self) -> int: return self.__client_id

    @client_id.setter
    def client_id(self, new_client_id: int) -> None:
        if not isinstance(new_client_id, int): raise TypeError("Client's ID needs to be an Integer.")
        if new_client_id < 0: raise ValueError("Client's ID needs to be greater than Zero.")

        self.__client_id = new_client_id

    @property
    def service_id(self) -> int: return self.__service_id

    @service_id.setter
    def service_id(self, new_service_id: int) -> None:
        if not isinstance(new_service_id, int): raise TypeError("Service's ID needs to be an Integer.")
        if new_service_id < 0: raise ValueError("Service's ID needs to be greater than Zero.")

        self.__service_id = new_service_id

    @property
    def professional_id(self) -> int: return self.__professional_id

    @professional_id.setter
    def professional_id(self, new_professional_id: int) -> None:
        if not isinstance(new_professional_id, int): raise TypeError("Professional's ID needs to be an Integer.")
        if new_professional_id < 0: raise ValueError("Professional's ID needs to be greater than Zero.")

        self.__professional_id = new_professional_id

    def get_formatted_date(self) -> str: 
        """Retorna a data do Horário, mas formatada especificamente para texto."""
        return self.date.strftime("%d/%m/%Y %H:%M:%S")

    def to_json(self) -> dict[str, Any]:
        """Converte os dados do Objeto para JSON."""
        return {
            "id": self.id,
            "date": self.date.strftime("%d/%m/%Y %H:%M:%S"),
            "confirmed": self.confirmed,
            "client_id": self.client_id,
            "service_id": self.service_id,
            "professional_id": self.professional_id
        }
    
    @staticmethod
    def from_json(data: dict[str, Any]) -> "Schedule":
        """Ler dados JSON e converte para um Objeto dessa Classe."""
        return Schedule(data["id"], datetime.strptime(data["date"], "%d/%m/%Y %H:%M:%S"), data["confirmed"], data["client_id"], data["service_id"], data["professional_id"])

    def __str__(self) -> str:
        available = "Confirmado" if self.confirmed else "Não Confirmado"
        return f"Horário {self.id}: {self.date.strftime("%d/%m/%Y %H:%M:%S")} - {available}"

class ScheduleDAO(AbstractDAO):
    _objects: list[Schedule] = []
    _json_file_path_str: str = "../data/schedules.json"
    _from_json_method = Schedule.from_json
