
from models.servico import Servico, ServicoDAO
from models.cliente import Cliente, ClienteDAO
from models.horario import Horario, HorarioDAO
from models.profissional import Profissional, ProfissionalDAO
from datetime import datetime

class View:

    # ---------- CLIENTE ----------
    def cliente_inserir(nome, email, fone, senha):
        cliente = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente)

    def cliente_listar():
        return ClienteDAO.listar()

    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)

    def cliente_atualizar(id, nome, email, fone, senha):
        cliente = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente)

    def cliente_excluir(id):
        cliente = Cliente(id, "", "", "", "")
        ClienteDAO.excluir(cliente)

    def cliente_criar_admin():
        """Cria o usuário admin caso não exista."""
        for c in View.cliente_listar():
            if c.get_email() == "admin":
                return
        View.cliente_inserir("Administrador", "admin", "0000-0000", "1234")

    def cliente_autenticar(email, senha):
        """Autentica clientes e também o admin."""
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None

    # ---------- PROFISSIONAL ----------
    def profissional_inserir(nome, especialidade, conselho, email, senha):
        profissional = Profissional(0, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.inserir(profissional)

    def profissional_listar():
        return ProfissionalDAO.listar()

    def profissional_listar_id(id):
        return ProfissionalDAO.listar_id(id)

    def profissional_atualizar(id, nome, especialidade, conselho, email, senha):
        profissional = Profissional(id, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.atualizar(profissional)

    def profissional_excluir(id):
        profissional = Profissional(id, "", "", "", "", "")
        ProfissionalDAO.excluir(profissional)

    def profissional_autenticar(email, senha):
        for p in View.profissional_listar():
            if p.get_email() == email and p.get_senha() == senha:
                return {"id": p.get_id(), "nome": p.get_nome()}
        return None

    # ---------- SERVIÇO ----------
    def servico_inserir(descricao, valor):
        servico = Servico(0, descricao, valor)
        ServicoDAO.inserir(servico)

    def servico_listar():
        return ServicoDAO.listar()

    def servico_listar_id(id):
        return ServicoDAO.listar_id(id)

    def servico_atualizar(id, descricao, valor):
        servico = Servico(id, descricao, valor)
        ServicoDAO.atualizar(servico)

    def servico_excluir(id):
        servico = Servico(id, "", 0.0)
        ServicoDAO.excluir(servico)

    # ---------- HORÁRIO ----------
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        h = Horario(0, data)
        h.set_confirmado(confirmado)
        h.set_id_cliente(id_cliente)
        h.set_id_servico(id_servico)
        h.set_id_profissional(id_profissional)
        HorarioDAO.inserir(h)

    def horario_listar():
        return HorarioDAO.listar()

    def horario_listar_id(id):
        return HorarioDAO.listar_id(id)

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        h = Horario(id, data)
        h.set_confirmado(confirmado)
        h.set_id_cliente(id_cliente)
        h.set_id_servico(id_servico)
        h.set_id_profissional(id_profissional)
        HorarioDAO.atualizar(h)

    def horario_excluir(id):
        h = Horario(id, datetime.now())
        HorarioDAO.excluir(h)

    def horario_avaliar(id, avaliacao, comentario):
        """Adiciona avaliação de um cliente a um horário."""
        h = View.horario_listar_id(id)
        if h is None: return
        h.set_avaliacao(avaliacao)
        h.set_comentario(comentario)
        HorarioDAO.atualizar(h)


    def horario_agendar_horario(id_profissional):
        """Retorna apenas horários disponíveis do profissional."""
        agora = datetime.now()
        disponiveis = []
        for h in View.horario_listar():
            if (h.get_data() >= agora and not h.get_confirmado() 
                and (h.get_id_cliente() == 0 or h.get_id_cliente() is None)
                and h.get_id_profissional() == id_profissional):
                disponiveis.append(h)
        disponiveis.sort(key=lambda x: x.get_data())
        return disponiveis
