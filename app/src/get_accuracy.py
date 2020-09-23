import pandas as pd
from sklearn.model_selection import train_test_split

from app.src.metric import compute_accuracy
from app.src.titanic_model import TitanicModel


def return_accuracy():
    titanic = pd.read_csv('data/titanic.csv')
    titanic_y = titanic['Survived']
    titanic_X = titanic.drop(columns=["Survived"])
    titanic_X = titanic_X[['Sex','Pclass','Name','Age','Siblings/Spouses Aboard','Parents/Children Aboard','Fare']]
    X_train, X_test, y_train, y_test = train_test_split(titanic_X, titanic_y, test_size=0.2)

    model = TitanicModel()
    model.fit(X_train, y_train)
    #print(f'women survival proba : {model.woman_survival_probability_}')
    #print(f'men survival proba : {model.men_survival_probability_}')
    predicted = model.predict(X=X_test)
    accuracy = compute_accuracy(actual=y_test, predicted=predicted)
    return accuracy
