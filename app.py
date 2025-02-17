import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Datos de Anuncios de Ventas de Vehículos')
hist_button = st.button('Construir histograma')
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir gráfica de Dispersión')
if disp_button:
        st.write('Creación de gráfico de Dispersión para el conjunto de datos de anuncios de venta de coches')
        fig = px.scatter(car_data, x="odometer", y="price")
        st.plotly_chart(fig, use_container_width=True)               