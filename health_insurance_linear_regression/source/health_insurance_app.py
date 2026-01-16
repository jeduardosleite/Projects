import streamlit as st
import requests
from PIL import Image

API_URL_DEFAULT = "http://127.0.0.1:8000"

# Dicionários de mapeamento
SMOKER_MAP = {"Sim": "yes", "Não": "no"}
SEX_MAP = {"Masculino": "male", "Feminino": "female"}
REGION_MAP = {"Sudeste": "southeast", "Sul": "southwest", "Noroeste": "northwest", "Nordeste": "northeast"}

def compute_bmi(weight_kg: float, height_m: float) -> float:
    if height_m <= 0:
        raise ValueError("A altura deve ser maior que zero para calcular o IMC.")
    return weight_kg / (height_m ** 2)

def call_prediction_api(api_url: str, payload: dict) -> float:
    response = requests.post(f"{api_url}/predict", json=payload, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data.get("predicted_charges")


def main():
    st.set_page_config(page_title="Estimativa de Custos Médicos", page_icon="💡", layout="wide")

    # Título
    st.markdown("<h2 style='text-align: center; color: #4B8BBE;'> Estimativa de Custos Médicos</h2>", unsafe_allow_html=True)

    # Imagem abaixo do título

    # Cria layout com três colunas horizontais
    col1, col2, col3 = st.columns([1, 2, 1]) # 1,2,1 define a largura de cada coluna

    # Tudo que vier dentro desse bloco deve ser renderizado dentro da coluna central
    with col2: 
        img = Image.open(r"C:\Users\Meu Computador\anaconda3\EBAC\Projetos\Em andamento\Health Insurance (trabalho em equipe)\titulo.png")
        st.image(img, width=1500) # largura de 1500 pixels

    # Explicação do projeto
    st.markdown(
        """
        Bem-vindo ao **Estimador de Custos Médicos**!

        Este aplicativo permite estimar o valor do seguro de saúde de um paciente com base em dados como idade, peso, altura, sexo, histórico de tabagismo, região e número de filhos.

        **Como usar o formulário:**
        - Preencha cada campo na barra lateral.  
        - Valores como "Sexo", "Fumante?" e "Região" estão em português, mas internamente serão convertidos para os valores esperados pelo modelo.
        - Clique em **Calcular custo** para enviar os dados para a API e obter o custo previsto do seguro.
        """
    )

    # Sidebar com dados do paciente

    st.sidebar.image(r"C:\Users\Meu Computador\Desktop\Dudu\Perfil.png", width=150)
    st.sidebar.header("Sobre o autor")
    st.sidebar.markdown(
        """
        Chamo-me José Eduardo, sou estudante de Ciência de Dados pela Uninter, com experiência em projetos de Machine Learning, análise de dados e desenvolvimento de aplicações com Python, FastAPI e Streamlit. 
        
        Este projeto tem a supervisão do Breno Andrade, cientista de dados da Unimed.

        **Contatos:**  
        [LinkedIn](https://www.linkedin.com/in/jeduardosleite/) | [GitHub](https://github.com/jeduardosleite)
        """)

    st.sidebar.header("Parâmetros do Paciente")
    api_url = st.sidebar.text_input("URL da API", value=API_URL_DEFAULT)

    age = st.sidebar.number_input("Idade", min_value=18, max_value=64, value=30, help="Informe a idade do paciente, entre 18 e 64 anos.")
    weight_kg = st.sidebar.number_input("Peso (kg)", min_value=0.0, max_value=400.0, value=75.0, step=0.1, help="Informe o peso do paciente em quilogramas.")
    height_m = st.sidebar.number_input("Altura (m)", min_value=0.5, max_value=2.5, value=1.7, step=0.01, help="Informe a altura do paciente em metros.")
    children = st.sidebar.selectbox(
    "Número de filhos",
    options=["0", "1-2", "3+"],
    help="Selecione a faixa de quantidade de filhos. 0 (sem filhos), 1-2 (um ou dois), 3+(três ou mais)"
    )

    sex_pt = st.sidebar.selectbox("Sexo", options=list(SEX_MAP.keys()), help="Selecione o sexo do paciente.")
    smoker_pt = st.sidebar.selectbox("Fumante?", options=list(SMOKER_MAP.keys()), help="Informe se o paciente fuma.")
    region_pt = st.sidebar.selectbox("Região", options=list(REGION_MAP.keys()), help="Selecione a região de residência do paciente.")

    # Mapear para valores do dataset
    sex = SEX_MAP[sex_pt]
    smoker = SMOKER_MAP[smoker_pt]
    region = REGION_MAP[region_pt]

    # Calcular IMC
    try:
        bmi = compute_bmi(weight_kg, height_m)
        st.expander("Ver IMC do paciente").info(f"IMC calculado: **{bmi:.2f}**")
    except ValueError as exc:
        st.error(str(exc))

# Botão de cálculo
if st.button("Prever custo"):
    try:
        bmi = float(weight_kg) / (float(height_m) ** 2)

        payload = {
            "age": int(age),
            "bmi": float(bmi),
            "children": children,
            "sex": sex,
            "smoker": smoker
        }

        predicted = call_prediction_api(api_url, payload)
        st.success(f"💰 Custo previsto: **${predicted:.2f}**")

    except requests.exceptions.RequestException as exc:
        st.error(f"🚨 Erro ao chamar a API: {exc}")

    except Exception as exc:
        st.error(f"🚨 Falha ao processar a previsão: {exc}")


if __name__ == "__main__":
    main()