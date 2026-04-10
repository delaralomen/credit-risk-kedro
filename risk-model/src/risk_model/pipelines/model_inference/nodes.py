"""
This is a boilerplate pipeline 'model_inference'
generated using Kedro 1.2.0
"""


def predict_with_truth(X_test, y_test, model):
    preds = model.predict_proba(X_test)[:, 1]

    df_out = X_test.copy()
    df_out["prediction"] = preds
    df_out["actual"] = y_test.values

    return df_out