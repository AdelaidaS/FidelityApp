import streamlit as st 
import pandas as pd 

#titulo
st.subheader("Información del Dataset:")

#carga del dataset
df = pd.read_csv("infiel.csv")

#explicacion del contenido del dataset
with st.container(): st.write(":information_source: Number of observations: 6366.  Number of variables: 9. Variable name definitions:")
with st.container(): st.write("-Rate marriage: 1=horror, 2=pobre, 3 = vaya, 4 = bueno, 5 = de lujo")
with st.container(): st.write("-Age: edad")
with st.container(): st.write("-Religious: 1 = no, 2 = moderadamente, 3 = bastante, 4 = fuertemente")
with st.container(): st.write("-yrs_married: Años de matrimonio")
with st.container(): st.write("-children: Numero de hijos")
with st.container(): st.write("-occupation: 1 = estudiante, 2 = semicualificada, 3 = administrativo, 4 = cualificado, 5 = administrativo, comercial, 6 = directivo")
with st.container(): st.write("-occupation_husb: profesion del marido")
with st.container(): st.write("-educ:9=primaria, 12=secundaria, 14 = form profesional, 16=universitario, 17=posgrado, 20=master")
with st.container(): st.write ("-affairs: tiempo dedicado a aventuras extramaritales")

#boton download del dataset
@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')
csv = convert_df(df)

#boton descarga
st.download_button(
   label=":orange[Press to Download Dataset]",
   data=csv,
   file_name="file.csv",
   mime= "text/csv",
   key='download-csv'
)
#visualizacion del dataset
st.dataframe(df) 