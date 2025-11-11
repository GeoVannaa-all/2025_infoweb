
import streamlit as st
from agenda import View

class AbrirContaUI:
    @staticmethod
    def main():
        st.title("Abrir Conta")

        if "usuario" in st.session_state:
            st.info(f"Você já está logado como {st.session_state['usuario']['nome']}.")
            if st.button("Sair"):
                del st.session_state["usuario"]
                st.success("Sessão encerrada.")
                try:
                    st.experimental_rerun()
                except Exception:
                    pass
            return

        st.subheader("Crie sua conta de Cliente")
        nome = st.text_input("Nome completo")
        email = st.text_input("E-mail")
        fone = st.text_input("Telefone (opcional)")
        senha = st.text_input("Senha", type="password")
        if st.button("Criar Conta"):
            try:
                View.cliente_inserir(nome, email, fone, senha)

                clientes = View.cliente_listar()
                criado = next((c for c in clientes if c.get_email().lower() == email.lower()), None)

                if criado:
                    st.session_state["usuario"] = {
                        "id": criado.get_id(),
                        "nome": criado.get_nome(),
                        "email": criado.get_email(),
                        "tipo": "Cliente"
                    }
                    st.success("Conta criada com sucesso! Você já está logado.")
                    try:
                        st.experimental_rerun()
                    except Exception:
                        pass
                else:
                    st.error("Conta criada, mas não foi possível localizar o usuário. Atualize a página.")
            except Exception as e:
                st.error(f"Erro ao criar conta: {e}")