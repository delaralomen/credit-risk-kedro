"""
This is a boilerplate pipeline 'hyperparam_tuning'
generated using Kedro 1.2.0
"""

from kedro.pipeline import node, Pipeline  # noqa
from .nodes import tune_xgboost

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func=tune_xgboost,
            inputs=["features", "params:hyperparam_tuning"],
            outputs=["best_params","hyperparam_study"],
            name="hyperparam_tuning_node"
        )
    ]
)
