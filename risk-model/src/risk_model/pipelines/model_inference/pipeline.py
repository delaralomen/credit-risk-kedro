"""
This is a boilerplate pipeline 'model_inference'
generated using Kedro 1.2.0
"""

from kedro.pipeline import node, Pipeline  # noqa
from .nodes import predict_with_truth

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([node(
            func=predict_with_truth,
            inputs=["X_test", "y_test", "xgb_model"],  # use best model
            outputs="predictions",
            name="prediction_node",

    )])
