"""
This is a boilerplate pipeline 'hyperparam_tuning'
generated using Kedro 1.2.0
"""
import optuna
import pandas as pd
import numpy as np

from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score
from xgboost import XGBClassifier


def tune_xgboost(df: pd.DataFrame, params: dict) -> dict:
    X = df.drop(columns=["target"])
    y = df["target"]

    search_space = params["xgboost_search_space"]
    n_trials = params["optuna"]["n_trials"]

    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    def objective(trial):
        # --- Sample hyperparameters from YAML-defined ranges ---
        xgb_params = {
            "n_estimators": trial.suggest_int(
                "n_estimators",
                search_space["n_estimators"][0],
                search_space["n_estimators"][1],
            ),
            "max_depth": trial.suggest_int(
                "max_depth",
                search_space["max_depth"][0],
                search_space["max_depth"][1],
            ),
            "learning_rate": trial.suggest_float(
                "learning_rate",
                search_space["learning_rate"][0],
                search_space["learning_rate"][1],
            ),
            "subsample": trial.suggest_float(
                "subsample",
                search_space["subsample"][0],
                search_space["subsample"][1],
            ),
            "colsample_bytree": trial.suggest_float(
                "colsample_bytree",
                search_space["colsample_bytree"][0],
                search_space["colsample_bytree"][1],
            ),
            "random_state": 42,
            "eval_metric": "logloss",
        }

        model = XGBClassifier(**xgb_params)

        scores = []

        # --- K-Fold Cross Validation ---
        for train_idx, val_idx in skf.split(X, y):
            X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]
            y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]

            model.fit(X_train, y_train)
            preds = model.predict_proba(X_val)[:, 1]

            auc = roc_auc_score(y_val, preds)
            scores.append(auc)

        return np.mean(scores)

    # --- Run optimization ---
    study = optuna.create_study(direction="maximize")
    study.optimize(objective, n_trials=n_trials)

    best_params = study.best_params

    print("\n=== Optuna Results ===")
    print("Best Params:", best_params)
    print(f"Best AUC: {study.best_value:.4f}")

    return best_params, study