import os
import pickle
import shutil

import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

MODEL_PATH = os.environ["MODEL_PATH"]
LOGIT_GAMES_V1_PATH = os.environ["LOGIT_GAMES_V1_PATH"]


def print_data(df: pd.DataFrame, df_name: str) -> None:
    """
    df: pandas data frame
    df_name: data frame name
    """

    print(f"################### {df_name} ###################")
    print(df.head())
    print("#########################################")


df = pd.read_csv(
    "https://github.com/bgweber/Twitch/raw/master/Recommendations/games-expand.csv"
)


X = df.drop(["label"], axis=1)
y = df["label"]

print_data(X, "X")
print_data(y, "y")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print(f"train accuracy: {train_score}")
print(f"test accuracy: {test_score}")

test_roc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])

print(f"test roc: {test_roc}")


pickle.dump(model, open(MODEL_PATH, "wb"))

model = pickle.load(open(MODEL_PATH, "rb"))

shutil.rmtree(LOGIT_GAMES_V1_PATH)
mlflow.sklearn.save_model(model, LOGIT_GAMES_V1_PATH)

loaded = mlflow.sklearn.load_model(LOGIT_GAMES_V1_PATH)
