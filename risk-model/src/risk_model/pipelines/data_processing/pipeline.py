"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 1.2.0
"""

from kedro.pipeline import node, Pipeline  # noqa
from .nodes import clean_loans

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=clean_loans,
            inputs="raw_loans",
            outputs="clean_loans",
            name="clean_data_node",
        )
    ])