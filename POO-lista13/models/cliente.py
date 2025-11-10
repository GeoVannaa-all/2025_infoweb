from .abc_dao import AbstractDAO
from typing import Any

class Client:
    def __init__(self, client_id: int, name: str, email: str, phone: str, password: str) -> None:
        self.id = client_id
        self.name = name
        self.email = email
        self.phone = phone
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
    def phone(self) -> str: return self.__phone

    @phone.setter
    def phone(self, phone: str) -> None:
        phone = phone.strip()
        if phone == "": raise ValueError("Phone can't be empty.")

        self.__phone = phone

    @property
    def password(self) -> str:
        return self.__password
    
    @password.setter
    def password(self, new_password: str) -> None:
        new_password = new_password.strip()
        if new_password == "": raise ValueError("Password can't be empty.")
        
        self.__password = new_password

    def __str__(self) -> str:
        return f"Cliente {self.id} : {self.name} -> {self.email} | {self.phone}"

    def to_json(self) -> dict[str, Any]:
        """Converte os dados do Objeto para JSON."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "password": self.password
        }

    @staticmethod
    def from_json(data: dict[str, Any]) -> "Client":
        """Ler dados JSON e converte para um Objeto dessa Classe."""
        return Client(data["id"], data["name"], data["email"], data["phone"], data["password"])

class ClientDAO(AbstractDAO):
    _objects: list[Client] = []
    _json_file_path_str: str = "../data/clients.json"
    _from_json_method = Client.from_json
