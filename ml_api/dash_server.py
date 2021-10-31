import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import mlflow.sklearn
import pandas as pd
from dash.dependencies import Input, Output

LOGIT_GAMES_V1_PATH = os.environ["LOGIT_GAMES_V1_PATH"]

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Model UI"),
        html.P(
            [
                html.Label("Game 1 "),
                dcc.Input(value="1", type="text", id="g1"),
            ]
        ),
        html.Div(
            [
                html.Label("Game 2 "),
                dcc.Input(value="0", type="text", id="g2"),
            ]
        ),
        html.P(
            [html.Label("Prediction "), dcc.Input(value="0", type="text", id="pred")]
        ),
    ]
)


model = mlflow.sklearn.load_model(LOGIT_GAMES_V1_PATH)


@app.callback(
    Output(component_id="pred", component_property="value"),
    [
        Input(component_id="g1", component_property="value"),
        Input(component_id="g2", component_property="value"),
    ],
)
def update_prediction(game1, game2):

    new_row = {
        "G1": float(game1),
        "G2": float(game2),
        "G3": 0,
        "G4": 0,
        "G5": 0,
        "G6": 0,
        "G7": 0,
        "G8": 0,
        "G9": 0,
        "G10": 0,
    }

    new_x = pd.DataFrame.from_dict(new_row, orient="index").transpose()
    return str(model.predict_proba(new_x)[0][1])


if __name__ == "__main__":
    app.run_server(host="0.0.0.0")
