"""
This is a boilerplate pipeline 'cross_validation'
generated using Kedro 1.2.0
"""

from kedro.pipeline import node, Pipeline
from .nodes import cross_validate_models

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([node(
        func=cross_validate_models,
        inputs=["features", "params:model_training"],
        outputs="cross_val_metrics",
    )
])
