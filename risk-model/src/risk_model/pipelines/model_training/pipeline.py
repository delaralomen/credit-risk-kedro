"""
This is a boilerplate pipeline 'model_training'
generated using Kedro 1.2.0
"""


from kedro.pipeline import node, Pipeline  # noqa
from .nodes import train_model

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=train_model,
            inputs=["X_train","y_train","params:log_reg","params:xgboost"],
            outputs=["log_reg_model", "xgb_model"],
            name="model_training_node",
        )
    ])