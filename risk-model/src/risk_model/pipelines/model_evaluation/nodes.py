"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 1.2.0
"""
from sklearn.metrics import roc_auc_score, accuracy_score
import pandas as pd


def evaluate_models(X_test, y_test, logreg_model, xgb_model):
    # Logistic Regression
    log_preds = logreg_model.predict_proba(X_test)[:, 1]
    log_auc = roc_auc_score(y_test, log_preds)

    # XGBoost
    xgb_preds = xgb_model.predict_proba(X_test)[:, 1]
    xgb_auc = roc_auc_score(y_test, xgb_preds)

    results = pd.DataFrame({
        "model": ["logistic_regression", "xgboost"],
        "auc": [log_auc, xgb_auc]
    })

    print("\nModel comparison:")
    print(results)

    return results