import streamlit as st

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="Assistente Virtual da Loja",
    page_icon="🚗",
    layout="centered"
)

# =========================
# ESTADO DA APLICAÇÃO
# =========================
if "etapa" not in st.session_state:
    st.session_state.etapa = 1

# =========================
# CABEÇALHO
# =========================
st.title("🚗 Assistente Virtual da Loja")
st.write(
    "Olá! 👋\n\n"
    "Vou te ajudar a escolher um veículo e simular as condições de compra "
    "de forma rápida, antes de um vendedor entrar em contato."
)

st.divider()

# =========================
# ETAPA 1 — CATÁLOGO
# =========================
if st.session_state.etapa == 1:
    st.subheader("📋 Ver veículos disponíveis")

    st.markdown(
        """
        👉 **[Clique aqui para ver o catálogo no WhatsApp](https://wa.me/c/5511947352770)**  
        Veja fotos, modelos e valores disponíveis.
        """,
        unsafe_allow_html=True
    )

    st.write("Quando encontrar um veículo de interesse, clique abaixo para simular a compra.")

    if st.button("➡️ Quero simular a compra"):
        st.session_state.etapa = 2
        st.rerun()

# =========================
# ETAPA 2 — CONTATO BÁSICO
# =========================
if st.session_state.etapa == 2:
    st.subheader("📞 Dados para contato")

    st.write(
        "Para continuarmos, informe seus dados básicos. "
        "Isso nos ajuda a agilizar o atendimento."
    )

    nome = st.text_input("Nome completo *")
    telefone = st.text_input("Telefone / WhatsApp *")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅️ Voltar"):
            st.session_state.etapa = 1
            st.rerun()

    with col2:
        if st.button("➡️ Continuar"):
            if nome and telefone:
                st.session_state.nome = nome
                st.session_state.telefone = telefone
                st.session_state.etapa = 3
                st.rerun()
            else:
                st.warning("⚠️ Preencha nome e telefone.")

# =========================
# ETAPA 3 — SIMULAÇÃO COMPLETA
# =========================
if st.session_state.etapa == 3:
    st.subheader("💰 Simulação de compra")

    st.write(
        "Agora vamos coletar as informações para simular as condições de pagamento."
    )

    cpf = st.text_input("CPF *")
    data_nascimento = st.date_input("Data de nascimento *")
    cep = st.text_input("CEP *")

    entrada = st.number_input(
        "Valor de entrada (R$)",
        min_value=0,
        step=500
    )

    renda = st.number_input(
        "Renda mensal (R$) *",
        min_value=0,
        step=500
    )

    parcelamento = st.selectbox(
        "Forma de pagamento",
        [
            "Financiamento bancário (até 48x)",
            "Cartão de crédito (até 21x)"
        ]
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅️ Voltar"):
            st.session_state.etapa = 2
            st.rerun()

    with col2:
        if st.button("📨 Enviar simulação"):
            if cpf and cep and renda > 0:
                st.success("✅ Simulação enviada com sucesso!")

                st.write(
                    f"""
                    Obrigado, **{st.session_state.nome}**!  

                    Recebemos seus dados e vamos encaminhar a simulação.  
                    Assim que o banco retornar com as condições,  
                    **um vendedor entrará em contato pelo WhatsApp {st.session_state.telefone}.**

                    🙂
                    """
                )

                st.session_state.etapa = 4
            else:
                st.warning("⚠️ Preencha todos os campos obrigatórios.")

# =========================
# ETAPA 4 — FINALIZAÇÃO
# =========================
if st.session_state.etapa == 4:
    st.subheader("✅ Atendimento finalizado")

    st.write(
        "Sua solicitação já está em análise.\n\n"
        "Se quiser, você pode continuar navegando pelo catálogo "
        "ou aguardar o contato do vendedor."
    )

    if st.button("🔁 Ver catálogo novamente"):
        st.session_state.etapa = 1
        st.rerun()

# =========================
# RODAPÉ
# =========================
st.divider()
st.caption(
    "🔒 Seus dados são utilizados apenas para simulação de compra "
    "e contato comercial."
)
