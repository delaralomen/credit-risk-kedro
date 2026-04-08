"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 1.2.0
"""


from kedro.pipeline import node, Pipeline  # noqa
from .nodes import create_features

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=create_features,
            inputs="clean_loans",
            outputs="feature_loans",
            name="feature_eng_node",
        )
    ])