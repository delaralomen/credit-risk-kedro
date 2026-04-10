"""
This is a boilerplate pipeline 'model_training'
generated using Kedro 1.2.0
"""
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
import pandas as pd


def train_models(X_train: pd.DataFrame, y_train: pd.DataFrame, training_params):
    lr_model = LogisticRegression(**training_params["log_reg"])
    lr_model.fit(X_train, y_train)

    xgb_model = XGBClassifier(**training_params["xgboost"])
    xgb_model.fit(X_train, y_train)

    return lr_model, xgb_model