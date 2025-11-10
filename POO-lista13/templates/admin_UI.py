from enum import IntEnum, auto

class UsersTypeIDs(IntEnum):
    """Enum para identificar o tipo do Usuário no 'session_state'."""
    ADMIN = auto()
    CLIENT = auto()
    PROFESSIONAL = auto()
