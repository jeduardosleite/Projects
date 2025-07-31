import streamlit as st

st.set_page_config(page_title="Calculadora de m²", layout="centered")

st.title("Calculadora de Valor por Metro Quadrado (em cm)")

# Entrada do valor por metro quadrado
preco_m2 = st.number_input("Valor do metro quadrado (R$):", min_value=0.0, format="%.2f")

# Entrada das medidas em centímetros
largura_cm = st.number_input("Largura (em centímetros):", min_value=0.0, format="%.2f")
comprimento_cm = st.number_input("Comprimento (em centímetros):", min_value=0.0, format="%.2f")

#Entrada da quantidade
quantidade = st.number_input("Quantidade:", min_value=0.0, format="%.2f")


# Cálculo e exibição do resultado
if st.button("Calcular"):
    largura_m = largura_cm / 100
    comprimento_m = comprimento_cm / 100
    area = largura_m * comprimento_m * quantidade
    valor_total = area * preco_m2

    st.success(f"Área total: {area:.2f} m²")
    st.success(f"Valor total: R$ {valor_total:,.2f}")
