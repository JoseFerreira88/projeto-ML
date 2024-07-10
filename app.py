import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression


# carregar dados
df = pd.read_csv("pizzas.csv")

# treinar o Modelo
modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x, y)

st.title("Prever o preço pizza")
st.divider()

diametro = st.number_input("Digite o Tamaho do diametro da pizza: ")

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(
        f"O valor da pizza com o diâmetro de {diametro:.2f} é de {preco_previsto:.2f} €."
    )
