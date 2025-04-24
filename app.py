import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Mi primera app en Render ✨")
st.write("¡Hola, mundo!")

# Ejemplo de tabla
data = pd.DataFrame({
    "Categoría": ["A", "B", "C"],
    "Valor": [10, 20, 30]
})

st.write("Tabla de ejemplo:")
st.dataframe(data)

# Ejemplo de gráfico
fig = px.bar(data, x="Categoría", y="Valor", title="Gráfico de barras")
st.plotly_chart(fig)