
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from joblib import dump

df = pd.read_csv('../data/tickets.csv')
X = df[['priority', 'created_hours']]
X['priority'] = X['priority'].map({'Low': 0, 'Medium': 1, 'High': 2})
y = df['sla_breach'].map({'No': 0, 'Yes': 1})
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
dump(clf, 'sla_model.joblib')
