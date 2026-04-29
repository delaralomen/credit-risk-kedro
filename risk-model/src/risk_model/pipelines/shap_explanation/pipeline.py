"""
This is a boilerplate pipeline 'shap_explanation'
generated using Kedro 1.2.0
"""

from kedro.pipeline import node, Pipeline
from .nodes import generate_shap_values, plot_shap_summary

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=generate_shap_values,
            inputs=["xgb_model", "X_train"],
            outputs="shap_values",
        ),
        node(
            func=plot_shap_summary,
            inputs="shap_values",
            outputs="shap_plot",
        ),
    ])