import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')
st.title('Pagina para visualizar los datos en histograma o diagrama de dispersión')
st.text('Por favor selecciona que deseas visualizar')
# Crear botones
hist_button = st.button('Construir histograma')
scatter_button = st.button('Construir gráfico de dispersión')

# Histograma
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión
if scatter_button:
    st.write('Creación de un gráfico de dispersión (kilometraje vs precio)')
    fig = px.scatter(car_data, x="odometer", y="price", title="Relación entre kilometraje y precio")
    st.plotly_chart(fig, use_container_width=True)
