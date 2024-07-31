# db_train.py
import joblib
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

import pandas as pd
import psycopg2


# 1. get data
db_connect = psycopg2.connect(
    host="localhost", database="mydatabase", user="myuser", password="mypassword"
)
df = pd.read_sql("SELECT * FROM iris_data ORDER BY id DESC LIMIT 100", db_connect)

# X, y = load_iris(return_X_y=True, as_frame=True)
X = df.drop(["id", "timestamp", "target"], axis="columns")
y = df["target"]

X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, train_size=0.8, random_state=2022
)

# 2. model development and train
scaler = StandardScaler()
classifier = SVC()

scaled_X_train = scaler.fit_transform(X_train)
scaled_X_valid = scaler.transform(X_valid)
classifier.fit(scaled_X_train, y_train)

train_pred = classifier.predict(scaled_X_train)
valid_pred = classifier.predict(scaled_X_valid)

train_acc = accuracy_score(y_true=y_train, y_pred=train_pred)
valid_acc = accuracy_score(y_true=y_valid, y_pred=valid_pred)

print("Train Accuracy :", train_acc)
print("Valid Accuracy :", valid_acc)

# 3. save model
joblib.dump(model_pipeline, "db_pipeline.joblib")

# 4. save data
df.to_csv("data.csv", index=False)
