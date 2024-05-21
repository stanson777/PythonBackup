from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix


iris=datasets.load_iris()

x=iris.data
y=iris.target


X_train, X_test,y_train, y_test= train_test_split(x,y,test_size=0.2,random_state=42)


model=KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)

predictions=model.predict(X_test)


accuracy = accuracy_score(y_test, predictions)
print(f'Dokładność modelu: {accuracy * 100:.2f}%')


conf_matrix = confusion_matrix(y_test, predictions)
print('Macierz pomyłek:')
print(conf_matrix)

class_report = classification_report(y_test, predictions, target_names=iris.target_names)
print('Raport klasyfikacji:')
print(class_report)