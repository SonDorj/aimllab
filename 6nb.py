#6
import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv('p-tennis.csv')

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

le= LabelEncoder()
X.Outlook = le.fit_transform(X.Outlook)
X.Temperature = le.fit_transform(X.Temperature)
X.Humidity = le.fit_transform(X.Humidity)
X.Windy = le.fit_transform(X.Windy)
y = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.30)

classifier = GaussianNB()
classifier.fit(X_train, y_train)
print("Accuracy is:", accuracy_score(classifier.predict(X_test), y_test))
