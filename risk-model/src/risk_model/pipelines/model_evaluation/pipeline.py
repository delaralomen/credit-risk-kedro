"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 1.2.0
"""


from kedro.pipeline import Pipeline, node
from .nodes import evaluate_models

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=evaluate_models,
            inputs=["X_test","y_test", "log_reg_model", "xgb_model"],
            outputs="model_metrics",
            name="evaluate_models_node",
        )
    ])