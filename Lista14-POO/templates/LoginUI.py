import streamlit as st
from agenda import View

class LoginUI:
    @staticmethod
    def main():
        st.title("Login no Sistema")

        # Se já estiver logado
        if "usuario" in st.session_state:
            usuario = st.session_state["usuario"]
            st.success(f"Você já está logado como: {usuario['nome']}")
            if st.button("Sair"):
                del st.session_state["usuario"]
                st.info("Sessão encerrada com sucesso.")
                st.rerun()
            return

        tipo = st.radio("Entrar como:", ["Profissional", "Cliente"])
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")

        if st.button("Entrar"):

            # Campos vazios
            if email.strip() == "" or senha.strip() == "":
                st.error("Preencha e-mail e senha.")
                return

            # Autenticar profissional
            if tipo == "Profissional":
                profissional = View.autenticar_profissional(email, senha)
                
                # Se não existir professional com esse email
                lista = View.profissional_listar()
                existe_email = any(p.email == email for p in lista)

                if not existe_email:
                    st.error("Nenhum profissional cadastrado com esse e-mail.")
                    return

                if profissional:
                    st.session_state["usuario"] = {
                        "id": profissional.id,
                        "nome": profissional.nome,
                        "email": profissional.email,
                        "tipo": "Profissional"
                    }
                    st.success("Login realizado com sucesso!")
                    st.rerun()
                else:
                    st.error("Senha incorreta. Tente novamente.")
                return

            # Autenticar cliente
            if tipo == "Cliente":
                from models.clienteDAO import ClienteDAO
                clientes = ClienteDAO.listar()
                cliente = next((c for c in clientes if c.email == email and c.senha == senha), None)
                existe_email = any(c.email == email for c in clientes)

                if not existe_email:
                    st.error("Nenhum cliente cadastrado com esse e-mail.")
                    return

                if cliente:
                    st.session_state["usuario"] = {
                        "id": cliente.id,
                        "nome": cliente.nome,
                        "email": cliente.email,
                        "tipo": "Cliente"
                    }
                    st.success("Login realizado com sucesso!")
                    st.rerun()
                else:
                    st.error("Senha incorreta. Tente novamente.")