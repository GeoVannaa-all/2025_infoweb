from datetime import datetime, timedelta
from typing import Any, Type, Optional
from models import *

class View:
    @staticmethod
    def get_all(dao_class: Type[AbstractDAO]) -> list[Any]: return dao_class.get_all()

    @staticmethod
    def get_id(dao_class: Type[AbstractDAO], obj_id: int) -> Optional[Any]: return dao_class.get_id(obj_id)
    
    @staticmethod
    def add(dao_class: Type[AbstractDAO], obj: Any) -> None:
        dao_class.add(obj)
    
    @staticmethod
    def update(dao_class: Type[AbstractDAO], obj: Any) -> None:
        dao_class.update(obj)
    
    @staticmethod
    def delete(dao_class: Type[AbstractDAO], obj: Any) -> None:
        dao_class.delete(obj)
    
    # Métodos - Cliente.
    @staticmethod
    def get_client_list() -> list[Client]:
        items: list[Client] = View.get_all(ClientDAO)
        items.sort(key=lambda i: i.id)
        return items

    @staticmethod
    def get_client(client_id: int) -> Optional[Client]: return View.get_id(ClientDAO, client_id)

    @staticmethod
    def append_client(name: str, email: str, phone: str, password: str) -> None:
        if View.check_email(email):
            raise ValueError("E-mail is already being used")
        
        View.add(ClientDAO, Client(0, name, email, phone, password))
    
    @staticmethod
    def update_client(client_id: int, name: str, email: str, phone: str, password: str) -> None:
        old_client = View.get_client(client_id)
        users_type = View.get_users_type()
        verif_excep = {} if old_client is None else { users_type.CLIENT : [ old_client.email ] }

        if View.check_email(email, verif_excep):
            raise ValueError("E-mail is already being used")
        
        View.update(ClientDAO, Client(client_id, name, email, phone, password))
    
    @staticmethod
    def remove_client(client_id: int) -> None:
        if len(View.get_schedules_by_client(client_id)) > 0:
            raise ValueError("Client has scheduled appointments")
        
        View.delete(ClientDAO, Client(client_id, "_", "_", "_", "_"))
    
    # Métodos - Serviço.
    @staticmethod
    def get_service_list() -> list[Service]: 
        items: list[Service] = View.get_all(ServiceDAO)
        items.sort(key=lambda i: i.id)
        return items

    @staticmethod
    def get_service(service_id: int) -> Optional[Service]: return View.get_id(ServiceDAO, service_id)

    @staticmethod
    def append_service(description: str, value: float) -> None:
        if View.check_service_description(description):
            raise ValueError("This description is already being used")
        
        View.add(ServiceDAO, Service(0, description, value))

    @staticmethod
    def update_service(service_id: int, description: str, value: float) -> None:
        if View.check_service_description(description):
            raise ValueError("This description is already being used")
        
        View.update(ServiceDAO, Service(service_id, description, value))

    @staticmethod
    def remove_service(service_id: int) -> None:
        if View.check_service_schedules(service_id):
            raise ValueError("This service is being used in some schedules")
        
        View.delete(ServiceDAO, Service(service_id, "_", 0))
    
    # Métodos - Horário.
    @staticmethod
    def get_schedule_list() -> list[Schedule]: 
        items: list[Schedule] = View.get_all(ScheduleDAO)
        items.sort(key=lambda i: i.date)
        return items

    @staticmethod
    def get_schedule(schedule_id: int) -> Optional[Schedule]: return View.get_id(ScheduleDAO, schedule_id)

    @staticmethod
    def append_schedule(date: datetime, confirmed: bool, client: Optional[Client], service: Optional[Service], professional: Optional[Professional]) -> None:
        client_id = client.id if isinstance(client, Client) else 0
        service_id = service.id if isinstance(service, Service) else 0
        professional_id = professional.id if isinstance(professional, Professional) else 0
        schedule = Schedule(0, date, confirmed, client_id, service_id, professional_id)
        if View.check_schedule(schedule):
            raise ValueError("There is already a schedule for the same professional at the same time")
        
        View.add(ScheduleDAO, schedule)

    @staticmethod
    def update_schedule(schedule_id: int, date: datetime, confirmed: bool, client: Optional[Client], service: Optional[Service], professional: Optional[Professional]) -> None:
        client_id = client.id if isinstance(client, Client) else 0
        service_id = service.id if isinstance(service, Service) else 0
        professional_id = professional.id if isinstance(professional, Professional) else 0
        schedule = Schedule(schedule_id, date, confirmed, client_id, service_id, professional_id)
        if View.check_schedule(schedule):
            raise ValueError("There is already a schedule for the same professional at the same time")
        
        View.update(ScheduleDAO, schedule)

    @staticmethod
    def remove_schedule(schedule_id: int) -> None:
        if View.get_schedule(schedule_id).client_id != 0:
            raise ValueError("Schedule has already been scheduled")
        
        View.delete(ScheduleDAO, Schedule(schedule_id, datetime(2025, 1, 2)))
    
    @staticmethod
    def append_multiple_schedules(date_beginning: datetime, date_ending: datetime, interval_minutes: int, professional: Professional) -> None:
        while date_beginning <= date_ending:
            View.append_schedule(date_beginning, False, None, None, professional)
            date_beginning += timedelta(minutes=interval_minutes)
    
    # Métodos - Profissional.
    @staticmethod
    def get_professional_list() -> list[Professional]: 
        items: list[Professional] = View.get_all(ProfessionalDAO)
        items.sort(key=lambda i: i.id)
        return items

    @staticmethod
    def get_professional(prof_id: int) -> Optional[Professional]: return View.get_id(ProfessionalDAO, prof_id)

    @staticmethod
    def append_professional(name: str, email: str, speciality: str, council: str, password: str) -> None:
        if View.check_email(email):
            raise ValueError("E-mail is already being used")
        
        View.add(ProfessionalDAO, Professional(0, name, email, speciality, council, password))

    @staticmethod
    def update_professional(prof_id: int, name: str, email: str, speciality: str, council: str, password: str) -> None:
        old_prof = View.get_professional(prof_id)
        users_type = View.get_users_type()
        verif_excep = {} if old_prof is None else { users_type.PROFESSIONAL : [ old_prof.email ] }

        if View.check_email(email, verif_excep):
            raise ValueError("E-mail is already being used")
        
        View.update(ProfessionalDAO, Professional(prof_id, name, email, speciality, council, password))

    @staticmethod
    def remove_professional(prof_id: int) -> None:
        if len(View.get_schedules_by_professional(prof_id)) > 0:
            raise ValueError("Professional has scheduled appointments")
        
        View.delete(ProfessionalDAO, Professional(prof_id, "_", "_", "_", "_", "_"))

    # Métodos - Admin.
    @staticmethod
    def get_admin_list() -> list[Admin]: 
        items: list[Admin] = View.get_all(AdminDAO)
        items.sort(key=lambda i: i.id)
        return items

    @staticmethod
    def get_admin(admin_id: int) -> Optional[Admin]: return View.get_id(AdminDAO, admin_id)

    @staticmethod
    def append_admin(name: str, email: str, password: str) -> None:
        if View.check_email(email):
            raise ValueError("E-mail is already being used")
        
        View.add(AdminDAO, Admin(0, name, email, password))
    
    @staticmethod
    def update_admin(admin_id: int, name: str, email: str, password: str) -> None:
        old_admin = View.get_admin(admin_id)
        users_type = View.get_users_type()
        verif_excep = {} if old_admin is None else { users_type.ADMIN : [ old_admin.email ] }

        if View.check_email(email, verif_excep):
            raise ValueError("E-mail is already being used")
        
        View.update(AdminDAO, Admin(admin_id, name, email, password))
    
    @staticmethod
    def remove_admin(admin_id: int) -> None:
        View.delete(AdminDAO, Admin(admin_id, "_", "_", "_"))

    # Filtração.
    @staticmethod
    def get_schedules_to_setting(prof_id: int) -> list[Schedule]:
        """Retorna os horários permitidos para serem agendados."""
        schedules: list[Schedule] = []
        today_time = datetime.now()
        
        for schedule in View.get_schedule_list():
            if (schedule.professional_id == prof_id
                    and schedule.date >= today_time
                    and schedule.client_id == 0
                    and schedule.confirmed == False):
                schedules.append(schedule)

        return schedules

    @staticmethod
    def get_schedules_by_client(client_id: int) -> list[Schedule]:
        """Retornar os Horários de um Cliente específico."""
        wanted_schedules: list[Schedule] = []
        schedules = View.get_schedule_list()

        for schedule in schedules:
            if schedule.client_id == client_id:
                wanted_schedules.append(schedule)

        return wanted_schedules

    @staticmethod
    def get_schedules_by_professional(prof_id: int) -> list[Schedule]:
        """Retornar os Horários de um Profissional específico."""
        wanted_schedules: list[Schedule] = []
        schedules = View.get_schedule_list()

        for schedule in schedules:
            if schedule.professional_id == prof_id:
                wanted_schedules.append(schedule)

        return wanted_schedules

    @staticmethod
    def check_schedule(schedule: Schedule) -> bool:
        """Retornar se um horário igual já existe para o profissional do horário"""
        if schedule.professional_id == 0: return False

        prof_schedules = View.get_schedules_by_professional(schedule.professional_id)

        for sch in prof_schedules:
            if sch.date == schedule.date and sch.id != schedule.id:
                return True
        
        return False
        
    @staticmethod
    def check_email(email: str, exceptions: dict[UsersTypeIDs, list[str]] = {}) -> bool:
        """Retorna se o email já está sendo utilizado."""
        clients = View.get_client_list()
        professionals = View.get_professional_list()
        admins = View.get_admin_list()
        users_types = View.get_users_type()

        for client in clients:
            if client.email == email and client.email not in exceptions.get(users_types.CLIENT, []): 
                return True

        for professional in professionals:
            if professional.email == email and professional.email not in exceptions.get(users_types.PROFESSIONAL, []): 
                return True

        for admin in admins:
            if admin.email == email and admin.email not in exceptions.get(users_types.ADMIN, []): 
                return True
        
        return False

    @staticmethod
    def check_service_description(description: str) -> bool:
        """Retorna se um serviço com a mesma descrição já existe."""
        services = View.get_service_list()

        for service in services:
            if service.description == description:
                return True
        
        return False

    @staticmethod
    def check_service_schedules(service_id: int) -> bool:
        """Retorna se o serviço está sendo utilizado em algum horário."""
        schedules = View.get_schedule_list()

        for schedule in schedules:
            if schedule.service_id == service_id:
                return True
            
        return False

    # Autenticação.
    @staticmethod
    def auth_user(email: str, password: str) -> Optional[tuple[int, int]]:
        """Retorna o ID e Tipo do Usuário."""
        clients = View.get_client_list()
        professionals = View.get_professional_list()
        admins = View.get_admin_list()
        users_type = View.get_users_type()
        
        for client in clients:
            if client.email == email and client.password == password:
                return (client.id, users_type.CLIENT)
        
        for prof in professionals:
            if prof.email == email and prof.password == password:
                return (prof.id, users_type.PROFESSIONAL)

        for admin in admins:
            if admin.email == email and admin.password == password:
                return (admin.id, users_type.ADMIN)
        
    @staticmethod
    def get_users_type() -> Type[UsersTypeIDs]:
        """Retorna os tipos de Usuários (Enum)."""
        return UsersTypeIDs
