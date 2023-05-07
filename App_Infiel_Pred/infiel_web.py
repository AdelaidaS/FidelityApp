#importar librerias
import streamlit as st
import pickle
import pandas as pd

#extraer los archivos pickle
with open ("AdaBoostClassifier.pkl", "rb") as ad:
    AdaBoostClassifier = pickle.load(ad)

with open ("GradientBoostingClassifier.pkl", "rb") as bo:
    GradientBoostingClassifier = pickle.load(bo)

with open ("KNeighborsClassifier.pkl", "rb") as kn:
    KNeighborsClassifier = pickle.load(kn)

with open ("MLPClassifier.pkl", "rb") as ml:
    MLPClassifier = pickle.load(ml)

with open ("RandomForestClassifier.pkl", "rb") as rf:
    KRandomForestClassifier = pickle.load(rf)


#funcion para clasificar el resultado
def classify(num):
    if num ==0:
        return "A buscar un buen abogado matrimonialista"
    else: 
        return "A cenar para celebrarlo"

def main(): 
    st.title("Cena o Abogado por Adelaida Suarez") 
    
if __name__ == '__main__':
    main() 