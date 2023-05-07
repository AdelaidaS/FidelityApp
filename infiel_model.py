#importar las librerias necesarias
import pickle
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier

#cargar los datos del dataset
# Carga tus datos aquí
infiel = pd.read_csv(r'C:\Users\Ade\Documents\ML\infiel.csv')

#separo el dataset 
X = infiel.drop(["affairs","fidelidad"], axis=1)
y = infiel.fidelidad 

# Divide tus datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Llama a la función best_model
best_model, best_report = get_best_model(X_train, y_train, X_test, y_test)

def find_best_params(model, params, X_train, y_train):
    grid_search = GridSearchCV(model, param_grid=params, cv=5)
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_

def get_best_models(X_train, y_train, X_test, y_test):
    classifiers_clasif = [
        (RandomForestClassifier(), {"n_estimators": [10, 100], "max_features": [1, 2, 3]}),
        (KNeighborsClassifier(), {"n_neighbors": [3, 5, 7, 9], "weights": ["uniform", "distance"]}),
        (GradientBoostingClassifier(), {"n_estimators": [50, 100, 200], "learning_rate": [0.1, 0.5, 1],
                                        "max_depth": [3, 4, 5]}),
        (MLPClassifier(), {"hidden_layer_sizes": [(10,), (20,), (30,)], "solver": ["lbfgs", "adam", "sgd"]}),
        (AdaBoostClassifier(), {"n_estimators": [50, 100, 200], "learning_rate": [0.1, 0.5, 1]}),
    ]

    best_models = [] # lista para guardar los tres mejores modelos

    for model, params in classifiers_clasif:
        best_model = find_best_params(model, params, X_train, y_train)

        y_pred = best_model.predict(X_test)
        score = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)

        # guardar modelo y puntaje en la lista
        best_models.append((best_model, score))

        with open(f"{model.__class__.__name__}.pkl", "wb") as file:
            # guardar el modelo en un archivo pickle
            pickle.dump(best_model, file)

        # imprimir el reporte de clasificación del modelo
        print(f"{model.__class__.__name__}:\n{report}\n")

    # ordenar los modelos por su puntaje y guardar los tres mejores
    best_models = sorted(best_models, key=lambda x: x[1], reverse=True)[:3]

    # imprimir los mejores modelos y sus puntajes
    for i, (model, score) in enumerate(best_models):
        print(f"{i+1}. {model.__class__.__name__}: {score}")
        print(f"{model.__class__.__name__}:\n{report}\n")

    return best_models