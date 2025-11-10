from abc import ABC
import json
import os
from typing import Any, Callable, Optional

def get_file_path(file: str) -> str:
    """Retorna o caminho absoluto de um arquivo."""
    base_dir: str = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_dir, file)

class AbstractDAO(ABC):
    """Classe Abstrata que padroniza todos os DAOs do programa."""
    _objects: list[Any] = []
    _json_file_path_str: str = "../data/file.json" # Uma String mais ou menos assim, indicando o caminho do arquivo JSON do DAO em relação ao arquivo.
    _json_file_path: str = "" # Caminho após passar pelo método "get_file_path". É inicializado quando a Subclasse for inicializada.
    _from_json_method: Callable[[dict[str, Any]], Any] = lambda obj: object # Método que transforma o JSON em um objeto do DAO.

    @classmethod
    def __init_subclass__(cls) -> None:
        """Ao iniciar uma Classe que Herda algo dessa Classe, ela terá seu atributo de classe 'json_file_path' alterado conforme o seu 'json_file_path_str'."""
        cls._json_file_path = get_file_path(cls._json_file_path_str)
        super().__init_subclass__()

    @classmethod
    def add(cls, obj: Any) -> None:
        cls._open_file()
        
        new_id: int = 1
        while cls.get_id(new_id) is not None:
            new_id += 1
        
        obj.id = new_id
        cls._objects.append(obj)

        cls._save_file()
    
    @classmethod
    def get_all(cls) -> list[Any]: 
        cls._open_file()
        return cls._objects

    @classmethod
    def get_id(cls, searched_id: int) -> Optional[Any]:
        cls._open_file()

        for obj in cls._objects:
            if obj.id == searched_id:
                return obj

    @classmethod
    def update(cls, obj: Any) -> None:
        cls._open_file()

        cur_obj = cls.get_id(obj.id)
        if cur_obj is None: raise ValueError("Passed Object doesn't exist on database.")

        cls._objects.remove(cur_obj)
        cls._objects.append(obj)

        cls._save_file()

    @classmethod
    def delete(cls, obj: Any) -> None:
        cls._open_file()
        
        cur_obj = cls.get_id(obj.id)
        if cur_obj is None: raise ValueError("Passed Object doesn't exist on database.")

        cls._objects.remove(cur_obj)

        cls._save_file()

    @classmethod
    def _open_file(cls) -> None:
        cls._objects = []

        if os.path.exists(cls._json_file_path):
            with open(cls._json_file_path, mode="r") as file:
                data: list[dict[str, Any]] = json.load(file)

                for obj in data:
                    new_obj = cls._from_json_method(obj)
                    cls._objects.append(new_obj)

    @classmethod
    def _save_file(cls) -> None:
        with open(cls._json_file_path, mode="w") as file:
            json_objects = [ obj.to_json() for obj in cls._objects ]
            json.dump(json_objects, file, indent=4)
