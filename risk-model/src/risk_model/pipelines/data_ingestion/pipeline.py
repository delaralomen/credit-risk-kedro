"""
This is a boilerplate pipeline 'data_ingestion'
generated using Kedro 1.2.0
"""
from kedro.pipeline import Pipeline, node
from .nodes import download_kaggle_data

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=download_kaggle_data,
            inputs=None,
            outputs="download_status",
            name="download_data_node",
        )
    ])