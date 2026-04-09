from sklearn.model_selection import train_test_split

from xgboost import XGBClassifier
import pandas as pd


def train_xgboost(X_train: pd.DataFrame, y_train: pd.DataFrame):

    model = XGBClassifier(
        n_estimators=200,
        max_depth=5,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        eval_metric="logloss"
    )

    model.fit(X_train, y_train)
    return model