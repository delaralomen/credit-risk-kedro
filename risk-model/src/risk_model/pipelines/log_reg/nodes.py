"""
This is a boilerplate pipeline 'model_training'
generated using Kedro 1.2.0
"""
from sklearn.linear_model import LogisticRegression
import pandas as pd


def train_model(X_train: pd.DataFrame, y_train: pd.DataFrame, params):
    model = LogisticRegression(**params)
    model.fit(X_train, y_train)

    return model