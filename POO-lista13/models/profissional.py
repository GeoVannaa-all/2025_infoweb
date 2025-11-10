from .abc_dao import AbstractDAO
from typing import Any

class Professional:
    def __init__(self, prof_id: int, name: str, email: str, speciality: str, council: str, password: str) -> None:
        self.id = prof_id
        self.name = name
        self.email = email
        self.speciality = speciality
        self.council = council
        self.password = password
    
    @property
    def id(self) -> int: return self.__id

    @id.setter
    def id(self, prof_id: int) -> None:
        if not isinstance(prof_id, int): raise TypeError("ID needs to be an INT.")
        if prof_id < 0: raise ValueError("ID can't be negative.")

        self.__id = prof_id

    @property
    def name(self) -> str: return self.__name

    @name.setter
    def name(self, name: str) -> None:
        name = name.strip()
        if name == "": raise ValueError("Name can't be empty.")

        self.__name = name

    @property
    def email(self) -> str: return self.__email

    @email.setter
    def email(self, email: str) -> None:
        email = email.strip()
        if email == "": raise ValueError("Email can't be empty.")

        self.__email = email

    @property
    def speciality(self) -> str: return self.__speciality

    @speciality.setter
    def speciality(self, speciality: str) -> None:
        speciality = speciality.strip()
        if speciality == "": raise ValueError("Speciality can't be empty.")

        self.__speciality = speciality

    @property
    def council(self) -> str: return self.__council

    @council.setter
    def council(self, council: str) -> None:
        council = council.strip()
        if council == "": raise ValueError("Council can't be empty.")

        self.__council = council

    @property
    def password(self) -> str:
        return self.__password
    
    @password.setter
    def password(self, new_password: str) -> None:
        new_password = new_password.strip()
        if new_password == "": raise ValueError("Password can't be empty.")
        
        self.__password = new_password

    def __str__(self) -> str:
        return f"Profissional {self.id} : {self.name} - {self.speciality} e {self.council}"

    def to_json(self) -> dict[str, Any]:
        """Converte os dados do Objeto para JSON."""
        return {
            "prof_id": self.id,
            "name": self.name,
            "email": self.email,
            "speciality": self.speciality,
            "council": self.council,
            "password": self.password
        }

    @staticmethod
    def from_json(data: dict[str, Any]) -> "Professional":
        """Ler dados JSON e converte para um Objeto dessa Classe."""
        return Professional(data["prof_id"], data["name"], data["email"], data["speciality"], data["council"], data["password"])

class ProfessionalDAO(AbstractDAO):
    _objects: list[Professional] = []
    _json_file_path_str: str = "../data/professionals.json"
    _from_json_method = Professional.from_json
