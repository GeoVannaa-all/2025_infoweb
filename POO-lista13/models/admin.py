from .abc_dao import AbstractDAO
from typing import Any

class Admin:
    def __init__(self, admin_id: int, name: str, email: str, password: str) -> None:
        self.id = admin_id
        self.name = name
        self.email = email
        self.password = password
    
    @property
    def id(self) -> int: return self.__id

    @id.setter
    def id(self, client_id: int) -> None:
        if not isinstance(client_id, int): raise TypeError("ID needs to be an INT.")
        if client_id < 0: raise ValueError("ID can't be negative.")

        self.__id = client_id

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
    def password(self) -> str:
        return self.__password
    
    @password.setter
    def password(self, new_password: str) -> None:
        new_password = new_password.strip()
        if new_password == "": raise ValueError("Password can't be empty.")
        
        self.__password = new_password

    def __str__(self) -> str:
        return f"Admin {self.id} : {self.name} -> {self.email}"

    def to_json(self) -> dict[str, Any]:
        """Converte os dados do Objeto para JSON."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password
        }

    @staticmethod
    def from_json(data: dict[str, Any]) -> "Admin":
        """Ler dados JSON e converte para um Objeto dessa Classe."""
        return Admin(data["id"], data["name"], data["email"], data["password"])

class AdminDAO(AbstractDAO):
    _objects: list[Admin] = []
    _json_file_path_str: str = "../data/admins.json"
    _from_json_method = Admin.from_json
