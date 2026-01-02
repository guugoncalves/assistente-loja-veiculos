import streamlit as st

st.set_page_config(
    page_title="Assistente Virtual da Loja",
    layout="centered"
)

st.title("🤖 Assistente Virtual da Loja")

st.write(
    "Olá! 👋\n\n"
    "Vou te fazer algumas perguntas rápidas para agilizar seu atendimento "
    "e te ajudar a simular as condições de compra."
)

st.divider()

# Catálogo
st.subheader("📋 Ver veículos disponíveis")
st.markdown(
    "[👉 Clique aqui para ver o catálogo no WhatsApp](https://wa.me/c/5511947352770)",
    unsafe_allow_html=True
)

st.divider()

# Simulação
st.subheader("💰 Simulação de compra")

nome = st.text_input("Nome completo")
telefone = st.text_input("Telefone / WhatsApp")
entrada = st.number_input("Valor de entrada (R$)", min_value=0, step=500)
renda = st.number_input("Renda mensal (R$)", min_value=0, step=500)

parcelamento = st.selectbox(
    "Forma de pagamento",
    [
        "Financiamento bancário (até 48x)",
        "Cartão de crédito (até 21x)"
    ]
)

if st.button("Enviar simulação"):
    if nome and telefone and renda > 0:
        st.success("✅ Simulação enviada com sucesso!")
        st.write(
            "Recebemos seus dados e vamos encaminhar para análise.\n\n"
            "Assim que o banco retornar com as condições, "
            "um vendedor entrará em contato pelo WhatsApp informado."
        )
    else:
        st.warning("⚠️ Preencha todos os campos obrigatórios.")
