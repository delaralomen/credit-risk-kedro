"""
This is a boilerplate pipeline 'split_data'
generated using Kedro 1.2.0
"""


from kedro.pipeline import Pipeline, node
from .nodes import split_data

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=split_data,
            inputs="features",
            outputs=["X_train", "X_test", "y_train", "y_test"],
            name="data_split_node",
        )
    ])