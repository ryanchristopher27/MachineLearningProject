from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
from minRiskClassifier import *

# Load the dataset
# data = pd.read_csv("dataNums.csv")

# # Preprocess the data
# X = data.drop("class", axis=1)
# y = data["class"]
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# # Train the model
# # clf = DecisionTreeClassifier(random_state=0).fit(X_train, y_train)
# clf = DecisionTreeClassifier(random_state=0).fit(X, y)
# # clf.fit(X_train, y_train)

# # Evaluate the model
# y_pred = clf.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print("Accuracy:", accuracy)

# # Make predictions on new data
# state = [-1, 1, 1, -1, -1, 0, 0, 1, 0]

# stateLabels = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# stateCombined = dict()
# for index, val in enumerate(stateLabels):
#     stateCombined[val] = state[index]
# stateDF = pd.DataFrame(stateCombined, index=[0])

# prediction = clf.predict_proba(stateDF)
# print("Prediction:", prediction)


def decisionTreeClassifier(state, player):
    # Load the dataset
    data = pd.read_csv("dataNums.csv")  

    X = data.drop("class", axis=1)
    y = data["class"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Train the model
    # clf = DecisionTreeClassifier(random_state=0).fit(X_train, y_train)
    clf = DecisionTreeClassifier(random_state=0).fit(X, y)

    # Evaluate the model
    # y_pred = clf.predict(X_test)
    # accuracy = accuracy_score(y_test, y_pred)
    # print("Accuracy:", accuracy)

    stateLabels = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    stateCombined = dict()
    for index, val in enumerate(stateLabels):
        stateCombined[val] = state[index]
    stateDF = pd.DataFrame(stateCombined, index=[0])
    prediction = clf.predict(stateDF)
    # print(prediction)
    if prediction[0] == 'positive':
        return 'X'

    return 'O'

# currentPrediction = decisionTreeClassifier([1,1,-1,0,-1,0,1,0,0], 1)
# print(currentPrediction)