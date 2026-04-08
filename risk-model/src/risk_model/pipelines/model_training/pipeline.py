from kedro.pipeline import Pipeline, node
from .nodes import train_xgboost


def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=train_xgboost,
            inputs="features",
            outputs="xgb_model",
            name="train_xgb_node",
        )
    ])