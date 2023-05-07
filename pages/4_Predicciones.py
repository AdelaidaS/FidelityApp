import streamlit as st 
import pandas as pd

from infiel_web import AdaBoostClassifier, KNeighborsClassifier, MLPClassifier, classify

def main():
    #titulo
    st.subheader("Predicciones :female-detective:")
    #titulo de la barra
    st.sidebar.header("Datos para la prediccion")

    #funcion para poner los parametros en el sidebar
    def user_input_parameters():
        rate_marriage = st.sidebar.slider("Califica tu matrimonio: 1=horror, 2=pobre, 3 = vaya, 4 = bueno, 5 = de lujo", 1, 5, 3)
        age = st.sidebar.slider("Edad",0,65,18)
        religious = st.sidebar.slider("Religión: 1 = no, 2 = moderadamente, 3 = bastante, 4 = fuertemente", 1,5,3)
        yrs_married = st.sidebar.slider("Años casada:", 1,60,1)
        children = st.sidebar.slider("Numero de hijos:", 0,10,1)
        occupation = st.sidebar.slider("Profesión: 1-estudiante, 2-semicualificado, 3-administrativo, 4-trabajo cualificado, 5-comercial,administrativo,6-directivo", 1,6,3)
        occupation_husb = st.sidebar.slider("Profesion marido: 1-estudiante, 2-semicualificado, 3-administrativo, 4-trabajo cualificado, 5-comercial,administrativo,6-directivo", 1,6,3)
        educ = st.sidebar.slider("Nivel de educación: 9=primaria, 12=secundaria, 14=form profesional, 16=universitario,17=posgrado, 20=master", 9,20,16)
        
             
        #creo un dataset para incluir los datos del usuario
        data={"Calidad matrimonio":rate_marriage,
            "Edad":age,
             "Religion": religious,
            "Años matrimonio:": yrs_married,
            "Numero hijos:": children,
            "Profesion propia": occupation,
            "Profesion marido":occupation_husb,
            "Nivel educativo": educ  
            }
        features = pd.DataFrame(data, index=[0]) 
        return features

    df = user_input_parameters()

    #elegir el modelo a aplicar
    option = ["AdaBoostClassifier" , "KNeighborsClassifier", "MLPClassifier"]
    model = st.sidebar.selectbox("Elige un modelo para tu prediccion", option)
    
    with st.container(): st.write("Parametros seleccionados por el usuario:")
    st.table(df)
    with st.container(): st.write("Modelo seleccionado por el usuario:") 
    with st.container(): st.write(model)
    
    if st.button("RUN"):
        if model == "AdaBoostClassifier":
            st.success(classify(AdaBoostClassifier.predict(df)))
        elif model == "MLPClassifier":
            st.success(classify(MLPClassifier.predict(df))) 
        elif model == "KNeighborsClassifier":
            st.success(classify(KNeighborsClassifier.predict(df)))


if __name__ == "__main__":
    main()
