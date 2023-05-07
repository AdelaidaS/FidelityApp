import streamlit as st 

#titulo de la pagina
st.subheader ("Exploratory Data Analysis")

#explicaion operativa destacable
with st.container(): st.write("Se ha incluido una nueva feature a partir de affairs, que es binaria True/False, y es el target del modelo.")

#presentacion en columnas de las graficas importantes
col1, col2 = st.columns(2)
with col1:
   st.subheader("Correlation matrix")
   st.image("matrix_corr.png")

with col2:
   st.subheader("Outliers")
   st.image("boxplot.png")

col3, col4 = st.columns(2)
with col3:
   st.subheader("Correlacion features")
   st.image("matriz.png")

with col4:
   st.subheader("Relaciones")
   st.image("pairplot.png")