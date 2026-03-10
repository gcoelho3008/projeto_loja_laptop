import streamlit as st
import pandas as pd

# Carregar os dados e colocar no Cache do streamlit
@st.cache_data
def carregar_dados():
    return pd.read_csv('./dataset/dados_notebook_clusterizado.csv')

df = carregar_dados()

# sidebar para filtro
st.sidebar.header('Filtros')

# selecionar modelos
model = st.sidebar.selectbox('Selecione o modelo', df['model'].unique())

# Filtrar o modelo
df_laptops_modelo = df[df['model'] == model]

# Filtrar por cluster do modelo escolhido 
df_laptops_final = df[df['cluster'] == df_laptops_modelo.iloc[0]['cluster']]

# Visualizar os modelos
st.write("Recomendações de notebooks ")
st.table(df_laptops_final)