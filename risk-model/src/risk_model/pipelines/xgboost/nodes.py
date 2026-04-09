from xgboost import XGBClassifier
import pandas as pd


def train_xgboost(X_train: pd.DataFrame, y_train: pd.DataFrame, params):

    model = XGBClassifier(**params)

    model.fit(X_train, y_train)
    return model