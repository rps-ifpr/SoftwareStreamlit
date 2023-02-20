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
    