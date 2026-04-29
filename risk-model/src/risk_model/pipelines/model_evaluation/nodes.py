"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 1.2.0
"""
from sklearn.metrics import roc_auc_score, accuracy_score
import pandas as pd

def evaluate_models(X_test, y_test, logreg_model, xgb_model):
    # Logistic Regression
    log_probs = logreg_model.predict_proba(X_test)[:, 1]
    log_preds = logreg_model.predict(X_test)
    log_auc = roc_auc_score(y_test, log_probs)
    log_acc = accuracy_score(y_test, log_preds)

    # XGBoost
    xgb_probs = xgb_model.predict_proba(X_test)[:, 1]
    xgb_preds = xgb_model.predict(X_test)
    xgb_auc = roc_auc_score(y_test, xgb_probs)
    xgb_acc = accuracy_score(y_test, xgb_preds)

    results = pd.DataFrame({
        "model": ["logistic_regression", "xgboost"],
        "auc": [log_auc, xgb_auc],
        "accuracy": [log_acc, xgb_acc],
    })

    print("\nModel comparison:")
    print(results)

    return results