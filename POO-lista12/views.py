from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
from models.horario import Horario, HorarioDAO
from models.profissional import Profissional, ProfissionalDAO
from datetime import datetime

class View:

#cliente
    def cliente_listar():
        r = ClienteDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)
    def cliente_inserir(nome, email, fone, senha):
        cliente = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente)
    def cliente_atualizar(id, nome, email, fone, senha):
        cliente = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente)
    def cliente_excluir(id):
        cliente = Cliente(id, "", "", "", "")
        ClienteDAO.excluir(cliente)
    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": return
        View.cliente_inserir("admin", "admin", "fone", "1234")
    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id":c.get_id(), "nome":
            c.get_nome()}
        return None

#serviço
    def servico_listar():
        r = ServicoDAO.listar()
        r.sort(key = lambda obj : obj.get_descricao())
        return r
    def servico_listar_id(id):
        return ServicoDAO.listar_id(id)
    def servico_inserir(id, descricao, valor):
        servico = Servico(id, descricao, valor)
        ServicoDAO.inserir(servico)
    def servico_atualizar(id, descricao, valor):
        servico = Servico(id, descricao, valor)
        ServicoDAO.atualizar(servico)
    def servico_excluir(id):
        servico = Servico(id, "", 0)
        ServicoDAO.excluir(servico)

#horário
    def horario_agendar_horario(id_profissional):
        r = []
        agora = datetime.now()
        for h in View.horario_listar():
            if h.get_data() >= agora and h.get_confirmado() == False and h.get_id_cliente() == None and h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort(key= lambda h : h.get_data())
        return r        
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO.inserir(c)
    def horario_listar():
        r = HorarioDAO.listar()
        r.sort(key = lambda obj : obj.get_data())
        return r
    @staticmethod
    def horario_listar_id(id):
        horarios = View.horario_listar()
        for h in horarios:
            if h.get_id() == id:
                return h
        return None

    def horario_filtrar_profissional(id_profissional):
        r = []
        for h in View.horario_listar():
            if h.get_id_profissional() == id_profissional:
                r.append(h)
        return r
    def horario_filtrar_cliente(id_cliente):
        r = []
        for h in View.horario_listar():
            if h.get_id_profissional() == id_cliente:
                r.append(h)
        return r
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO.atualizar(c)
    def horario_excluir(id):
        c = Horario(id, None)
        HorarioDAO.excluir(c)

#profissional
    def profissional_inserir(nome, especialidade, conselho, email, senha):
        p = Profissional(0, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.inserir(p)
    def profissional_atualizar(id, nome, especialidade, conselho, email, senha):
        p = Profissional(id, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.atualizar(p)
    def profissional_excluir(id):
        p = Profissional(id, "", "", "", "", "")
        ProfissionalDAO.excluir(p)
    def profissional_listar():
        r = ProfissionalDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r
    def profissional_listar_id(id):
        return ProfissionalDAO.listar_id(id)
    def profissional_autenticar(email, senha):
        for p in ProfissionalDAO.listar():
            if p.get_email() == email and p.get_senha() == senha:
                return {"id": p.get_id(), "nome": p.get_nome()}
        return None