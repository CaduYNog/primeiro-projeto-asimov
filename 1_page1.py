import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df_reviews = pd.read_csv('/Users/T-GAMER/OneDrive/Documentos/GitHub/primeiro-projeto-asimov/dataset/customer reviews.csv')
df_top100_books = pd.read_csv('/Users/T-GAMER/OneDrive/Documentos/GitHub/primeiro-projeto-asimov/dataset/Top-100 Trending Books.csv')

price_max = df_top100_books['book price'].max()
#variável que pega o maior valor da coluna 'book price'

price_min = df_top100_books['book price'].min()
#variável que pega o menor valor da coluna 'book price'

max_price = st.sidebar.slider('Price Range', price_min, price_max, price_max)
#slider para filtrar livros por preço
#ele seleciona livros em um intervalo de preço 'Price Range', que vai do menor valor ao maior começando pelo maior
df_books = df_top100_books[df_top100_books['book price'] <= max_price] 
df_books

fig = px.bar(df_top100_books['year of publication'].value_counts())
fig2 = px.histogram(df_books['book price'])

col1, col2 = st.columns(2)
col1.plotly_chart(fig)
#cria um gráfico de barras mostrando quais livros mais venderam de acordo com o ano de sua publicação
col2.plotly_chart(fig2)



