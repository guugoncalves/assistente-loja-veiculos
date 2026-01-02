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
# CABEÇALHO
# =========================
st.title("🚗 Assistente Virtual da Loja")
st.write(
    "Olá! 👋\n\n"
    "Vou te ajudar a escolher um veículo e **simular as condições de compra** "
    "de forma rápida, antes de um vendedor entrar em contato."
)

st.divider()

# =========================
# CATÁLOGO
# =========================
st.subheader("📋 Ver veículos disponíveis")

st.markdown(
    """
    👉 **[Clique aqui para ver o catálogo no WhatsApp](https://wa.me/c/5511947352770)**  
    Veja fotos, modelos e valores disponíveis.
    """,
    unsafe_allow_html=True
)

st.divider()

# =========================
# SIMULAÇÃO DE COMPRA
# =========================
st.subheader("💰 Simulação de compra")

st.write(
    "Preencha os dados abaixo para iniciarmos a simulação. "
    "Essas informações serão analisadas e um vendedor entrará em contato."
)

# Dados do cliente
nome = st.text_input("Nome completo *")
cpf = st.text_input("CPF *")
data_nascimento = st.date_input("Data de nascimento *")
telefone = st.text_input("Telefone / WhatsApp *")
cep = st.text_input("CEP *")

st.divider()

# Dados financeiros
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

st.divider()

# =========================
# ENVIO DA SIMULAÇÃO
# =========================
if st.button("📨 Enviar simulação"):
    if nome and cpf and telefone and cep and renda > 0:
        st.success("✅ Simulação enviada com sucesso!")

        st.write(
            """
            Recebemos seus dados e vamos encaminhar para análise.  

            Assim que o banco retornar com as condições,  
            **um vendedor da loja entrará em contato pelo WhatsApp informado**.

            Obrigado pelo contato! 🙂
            """
        )
    else:
        st.warning("⚠️ Preencha todos os campos obrigatórios marcados com *.")

# =========================
# RODAPÉ
# =========================
st.divider()
st.caption(
    "🔒 Seus dados são utilizados apenas para simulação de compra "
    "e contato comercial."
)
