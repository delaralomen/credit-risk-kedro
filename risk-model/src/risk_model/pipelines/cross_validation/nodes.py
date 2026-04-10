"""
This is a boilerplate pipeline 'cross_validation'
generated using Kedro 1.2.0
"""
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
import pandas as pd
import numpy as np


def cross_validate_models(df: pd.DataFrame, training_params):
    X = df.drop(columns=["target"])
    y = df["target"]

    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    lr_scores = []
    xgb_scores = []

    for fold, (train_idx, val_idx) in enumerate(skf.split(X, y)):
        X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]
        y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]

        # --- Logistic Regression ---
        lr_model = LogisticRegression(**training_params["log_reg"])
        lr_model.fit(X_train, y_train)
        lr_preds = lr_model.predict_proba(X_val)[:, 1]
        lr_auc = roc_auc_score(y_val, lr_preds)
        lr_scores.append(lr_auc)

        # --- XGBoost ---
        xgb_model = XGBClassifier(**training_params["xgboost"])
        xgb_model.fit(X_train, y_train)
        xgb_preds = xgb_model.predict_proba(X_val)[:, 1]
        xgb_auc = roc_auc_score(y_val, xgb_preds)
        xgb_scores.append(xgb_auc)

        print(f"Fold {fold+1}: LR={lr_auc:.4f}, XGB={xgb_auc:.4f}")

    results = pd.DataFrame({
        "model": ["logistic_regression", "xgboost"],
        "mean_auc": [np.mean(lr_scores), np.mean(xgb_scores)],
        "std_auc": [np.std(lr_scores), np.std(xgb_scores)]
    })

    print("\n=== Cross-validation results ===")
    print(results)

    return results