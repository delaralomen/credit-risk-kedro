"""
This is a boilerplate pipeline 'shap_explanation'
generated using Kedro 1.2.0
"""
import shap
import pandas as pd
import matplotlib.pyplot as plt


def generate_shap_values(model, X_train: pd.DataFrame):
    X = X_train.drop(columns=["prediction", "actual"], errors="ignore")

    X_shap = X.sample(
        n=min(1000, len(X)),
        random_state=42,
    )

    explainer = shap.Explainer(model)
    shap_values = explainer(X_shap)

    return shap_values


def plot_shap_summary(shap_values):
    shap.summary_plot(
        shap_values,
        shap_values.data,
        feature_names=shap_values.feature_names,
        show=False,
    )

    plt.tight_layout()
    return plt.gcf()