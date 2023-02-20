import streamlit as st
import pandas as pd
import numpy as np
#streamlit run app2.py
st.header('Minha dashboard')
st.sidebar.header('Escolha')
st.markdown('# Meu Titulo')
st.caption('Minha legenda')

pessoas = [{'Nome': 'Caio', 'Idade':22},
           {'Nome': 'Marcos', 'Idade':33}]
st.write('Pessoa', pessoas)
#Exibindo Dados com pandas
df = pd.DataFrame(
    np.random.rand(10,4),#linhas e colunas
    columns=['Preço', 'Taxa de Ocupação', 'Taxa de Inadimplência', 'Pessoas por Casa']
)
st.table(df)
st.line_chart(df)
st.bar_chart(df)

if st.sidebar.button('Exibir Grafico'):
    df = pd.DataFrame (
        np.random.rand (10, 4),  # linhas e colunas
        columns=['Preço', 'Taxa de Ocupação', 'Taxa de Inadimplência', 'Pessoas por Casa'])
    st.bar_chart(df)

check = st.sidebar.checkbox('Aceitos')
if check:
     st.write('Marcado')

opcao = st.sidebar.radio( #ou selectbox ou multiselect ou slider
    'Selecione uma opcao',
    ('Preço', 'Taxa de Ocupação')
)
if opcao == 'Preço':
    df = pd.DataFrame (
        np.random.rand (10, 1),  # linhas e colunas
        columns=['Preço'])
    st.bar_chart (df)

if opcao == 'Taxa de Ocupação':
    df = pd.DataFrame (
        np.random.rand (10, 1),  # linhas e colunas
        columns=['Taxa de Ocupação'])
    st.bar_chart (df)