import streamlit as st 

#titulo del apartado
st.subheader("Selección Modelo de Machine Learning")

#texto explicativo
with st.container(): st.write("Una vez realizado el análisis exploratorio de datos (EDA) de nuestro dataset y establecido nuestro target, que en este caso es la clasificación binaria de infidelidad True/False, podemos proceder a seleccionar un modelo de aprendizaje automático :blue[supervisado de clasificación].")
with st.container(): st.write("Como abordaje inical se ha empleado la biblioteca LazyPredict, de la que hemos obtenido graficamente estos resultados")

#incluir imagen
from PIL import Image
image = Image.open('lazy.png')
st.image(image)

#texto explicativo
with st.container(): st.write("Se han testado los siguientes modelos:")
with st.container(): st.write("-AdaBoostClassifier")
with st.container(): st.write("-KNeighborsClassifier")
with st.container(): st.write("-MLPClassifier")