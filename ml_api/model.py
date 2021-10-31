import os
import pickle
import shutil

import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

MODEL_PATH = os.environ["MODEL_PATH"]
LOGIT_GAMES_V1_PATH = os.environ["LOGIT_GAMES_V1_PATH"]

df = pd.read_csv(
    "https://github.com/bgweber/Twitch/raw/master/Recommendations/games-expand.csv"
)


X = df.drop(["label"], axis=1)
y = df["label"]

print("################ X ################")
print(X.head())

print("################ y ################")
print(y.head())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print(f"train score: {train_score}")
print(f"test score: {test_score}")


pickle.dump(model, open(MODEL_PATH, "wb"))

model = pickle.load(open(MODEL_PATH, "rb"))

shutil.rmtree(LOGIT_GAMES_V1_PATH)
mlflow.sklearn.save_model(model, LOGIT_GAMES_V1_PATH)

loaded = mlflow.sklearn.load_model(LOGIT_GAMES_V1_PATH)
