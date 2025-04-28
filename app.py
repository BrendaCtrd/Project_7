import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Car Sales', divider=True)
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
      

#Creación de botón para gráfico de dispersión
scatterpl_button = st.button('Build scatter plot') # crear un botón

if scatterpl_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Scatter plot of condition of cars for sale vs. price')
    
    fig2 = px.scatter(car_data, x='condition', y='price', color='condition', labels={'condition': 'Car condition', 'price': 'Price $USD'})
    st.plotly_chart(fig2, use_container_width=True)

build_histogram = st.checkbox('Build cars on sale histogram')

if build_histogram:
    st.write('Type of cars on sale histogram')
            
    # crear un histograma
    fig = px.histogram(car_data, x="type", color="type", labels={'type': 'Car type'})
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Cars available per price")

# Slider de rango de precios
slider_range = st.slider("Price filter", 0, 375000, (0, 375000))  

# Filtrar el DataFrame por el rango seleccionado
filtered_data = car_data[(car_data['price'] >= slider_range[0]) & (car_data['price'] <= slider_range[1])]

# Mostrar los modelos disponibles en ese rango
st.write("The available cars are:")
st.write(filtered_data['model'].unique())

