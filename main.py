import streamlit as st

st.set_page_config(page_title="Assistente Virtual", layout="centered")

st.title("🤖 Assistente Virtual da Loja")

st.write(
    "Olá! 👋\n\n"
    "Sou o assistente virtual da loja.\n\n"
    "Vou te ajudar a encontrar o veículo ideal e "
    "simular as condições de pagamento."
)

if st.button("📋 Ver catálogo no WhatsApp"):
    st.markdown(
        "[Clique aqui para ver o catálogo](https://wa.me/c/5511947352770)",
        unsafe_allow_html=True
    )

st.divider()

st.subheader("💰 Simulação de compra")

nome = st.text_input("Nome completo")
entrada = st.number_input("Valor de entrada (R$)", min_value=0)
renda = st.number_input("Renda mensal (R$)", min_value=0)

if st.button("Enviar simulação"):
    if nome and renda > 0:
        st.success("✅ Simulação enviada com sucesso!")
        st.write("Um vendedor entrará em contato em breve.")
    else:
        st.warning("⚠️ Preencha os campos obrigatórios.")
