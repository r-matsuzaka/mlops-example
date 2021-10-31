import os
import pickle
import shutil

import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.linear_model import LogisticRegression

MODEL_PATH = os.environ["MODEL_PATH"]

df = pd.read_csv(
    "https://github.com/bgweber/Twitch/raw/master/Recommendations/games-expand.csv"
)
x = df.drop(["label"], axis=1)
y = df["label"]

model = LogisticRegression()
model.fit(x, y)

pickle.dump(model, open(MODEL_PATH, "wb"))

model = pickle.load(open(MODEL_PATH, "rb"))
# model.predict_proba(x)

model_path = "ml_api/model/logit_games_v1"
shutil.rmtree(model_path)
mlflow.sklearn.save_model(model, model_path)

loaded = mlflow.sklearn.load_model(model_path)

print(loaded.predict_proba(x))
