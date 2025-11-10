from views import View

class UI:
    """Programa de Terminal que realiza o CRUD do 'Admin'."""
    @staticmethod
    def menu() -> int:
        print("1 - Adicionar Admin\n2 - Listar Admins\n3 - Listar Admin por ID\n4 - Atualizar Admins\n5 - Deletar Admins\n6 - Sair do Programa")
        return int(input("- Selecione uma Opção acima: "))

    @staticmethod
    def main() -> None:
        while True:
            opt = UI.menu()

            match opt:
                case 1: UI.add_admin()
                case 2: UI.list_admins()
                case 3: UI.get_admin()
                case 4: UI.update_admin()
                case 5: UI.delete_admin()
                case 6:
                    print("Saindo...")
                    break
                case _: print("Opção Inválida!")
    
    @staticmethod
    def add_admin() -> None:
        name = input("- Nome do Admin: ")
        email = input("- E-mail do Admin: ")
        password = input("- Senha do Admin: ")
        
        View.append_admin(name, email, password)

        print("Admin adicionado com Sucesso!")
    
    @staticmethod
    def update_admin() -> None:
        admin_id = int(input("- ID do Admin: "))
        name = input("- Novo Nome do Admin: ")
        email = input("- Novo E-mail do Admin: ")
        password = input("- Nova Senha do Admin: ")
        
        View.update_admin(admin_id, name, email, password)

        print("Admin atualizado com Sucesso!")
    
    @staticmethod
    def list_admins() -> None:
        admins = View.get_admin_list()

        for admin in admins:
            print(admin)
        
    @staticmethod
    def get_admin() -> None:
        admin_id = int(input("- ID do Admin: "))
        admin = View.get_admin(admin_id)

        if admin:
            print(admin)
        else:
            print("ID Desconhecido!")
        
    @staticmethod
    def delete_admin() -> None:
        admin_id = int(input("- ID do Admin: "))
        View.remove_admin(admin_id)

        print("Admin deletado com Sucesso!")

if __name__ == "__main__":
    UI.main()
