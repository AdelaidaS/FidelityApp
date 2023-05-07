import pickle
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier


def get_best_model(X_train, y_train, X_test, y_test):
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
        grid_search = GridSearchCV(model, param_grid=params, cv=5)
        grid_search.fit(X_train, y_train)

        y_pred = grid_search.predict(X_test)
        score = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)

        # guardar modelo y puntaje en la lista
        best_models.append((grid_search.best_estimator_, score))

        with open(f"{model.__class__.__name__}.pkl", "wb") as f:
            pickle.dump(grid_search.best_estimator_, f)

    # ordenar la lista por puntaje (en orden descendente) y seleccionar los tres mejores modelos
    best_models = sorted(best_models, key=lambda x: x[1], reverse=True)[:3]
    best_model_1, best_score_1 = best_models[0]
    best_model_2, best_score_2 = best_models[1]
    best_model_3, best_score_3 = best_models[2]

    with open("best_model_1.pkl", "wb") as f:
        pickle.dump(best_model_1, f)

    with open("best_model_2.pkl", "wb") as f:
        pickle.dump(best_model_2, f)

    with open("best_model_3.pkl", "wb") as f:
        pickle.dump(best_model_3, f)

    return best_model_1, best_model_2, best_model_3

# Carga tus datos aquí
infiel = pd.read_csv(r'C:\Users\Ade\Documents\ML\infiel.csv')
X = infiel.drop(["affairs","fidelidad"], axis=1)
y = infiel.fidelidad 

# Divide tus datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Llama a la función get_best_model
best_model_1, best_model_2, best_model_3 = get_best_model(X_train, y_train, X_test, y_test)


with open("best_model_1.pkl", "rb") as f:
    best_model_1 = pickle.load(f)

with open("best_model_2.pkl", "rb") as f:
    best_model_2 = pickle.load(f)

with open("best_model_3.pkl", "rb") as f:
    best_model_3 = pickle.load(f)

# Hacer predicciones sobre nuevos datos
nuevos_datos = pd.read_csv("nuevos_datos.csv")
predicciones_1 = best_model_1.predict(nuevos_datos)
predicciones_2 = best_model_2.predict(nuevos_datos)
predicciones_3 = best_model_3.predict(nuevos_datos)
