import streamlit as st
import numpy as np

#configuracion de la Home
st.set_page_config(
    page_title="Champagne o Abogado",
    page_icon= ":crystal_ball:",
    layout="centered",
    initial_sidebar_state="expanded")

#titulo
st.title('Champagne :champagne: o abogado :female-judge:')
st.header(':blue[Predictor de fidelidad marital]')
#st.sidebar.success("Select a page above.")

#texto descriptivo
with st.container():
   st.write("En esta web, vamos a utilizar un conjunto de datos obtenidos mediante encuestas a mujeres para predecir si una mujer va a ser infiel o no en su matrimonio.")
with st.container():
   st.write("¿Cómo lo haremos sin nuestra :crystal_ball:?") 
with st.container():
   st.write("Pues utilizando modelos de Machine Learning, que son como los cerebritos de un ordenador, para analizar la información que tenemos sobre el matrimonio, la edad, el tiempo de casados, el número de hijos, la religiosidad, el nivel de educación y la ocupación tanto de la mujer como del marido.")
with st.container():
   st.write(":grey_exclamation: también se tiene en cuenta la cantidad de tiempo que la mujer dedica a relaciones extramatrimoniales.")

#from PIL import Image
#image = Image.open('balanza.png')
#st.image(image, width=500,caption='Imagen con Canva IA by ASuarez')
