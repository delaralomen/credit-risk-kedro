"""
This is a boilerplate pipeline 'data_ingestion'
generated using Kedro 1.2.0
"""
import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

def download_kaggle_data():
    api = KaggleApi()
    api.authenticate()

    dataset = "wordsforthewise/lending-club"
    download_path = "data/raw"

    # download zip
    api.dataset_download_files(dataset, path=download_path, unzip=False)

    # unzip
    zip_path = os.path.join(download_path, "lending-club.zip")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(download_path)

    return "download completed"