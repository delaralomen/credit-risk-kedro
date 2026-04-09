from kedro.pipeline import Pipeline, node
from .nodes import train_xgboost


def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=train_xgboost,
            inputs=["X_train","y_train","params:xgboost"],
            outputs="xgb_model",
            name="train_xgb_node",
        )
    ])