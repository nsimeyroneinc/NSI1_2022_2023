from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Chargement et séparation des données en ensembles d'entraînement et de test
X, y = load_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Création du modèle KNN
knn = KNeighborsClassifier(n_neighbors=5)

# Entraînement du modèle
knn.fit(X_train, y_train)

# Prédiction des classes pour les exemples de test
predictions = knn.predict(X_test)

# Evaluation de la précision du modèle
accuracy = knn.score(X_test, y_test)
print("Précision du modèle : {:.2f}".format(accuracy))
