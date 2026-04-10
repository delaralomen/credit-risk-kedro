# Credit Risk Modeling Using Kedro

This project is an end-to-end credit risk modeling system built with [Kedro](https://kedro.org/), an open-source framework for data engineering and data science code, created by QuantumBlack Labs AI at McKinsey.

## Dataset
LendingClub, the loan information dataset used in this project, can be found [here](https://www.kaggle.com/datasets/wordsforthewise/lending-club).

To reproduce this project, you need a Kaggle API key configured on your system (typically placed in `~/.kaggle/kaggle.json`) with the correct structure and permissions.

**Structure of** `~/.kaggle/kaggle.json`:
```json
{
    "username": "your_username",
    "key": "your_key"
}
```

**Permissions:**
```bash
chmod 600 ~/.kaggle/kaggle.json
```


## Dependencies

```bash
conda env create -f environment.yml
```

### Kedro Dependencies

Inside the project directory (`./risk-model`), run the following:

```bash
pip install -r requirements.txt && pip install "kedro[pandas]"
```


## Project Structure

The project currently consists of 7 different steps (pipelines):
1. Data Ingestion
2. Data Processing
3. Feature Engineering
4. Split Data
5. Logistic Regression
6. XGBoost
7. Model Evaluation
8. Cross Validation (for picking the superior model)

Pipelines used in this project can be found in `./risk-model/src/risk-model/pipelines`. Each of them was created using:

```bash
kedro pipeline create <pipeline_name>
```

and run using:

```bash
kedro run --pipeline=<pipeline_name>
```

The input dataset(s) and output dataset(s) of each pipeline must first be defined in the data catalog (`./risk-model/conf/base/catalog.yml`).


The input dataset(s), output dataset(s), and functions used in each pipeline are set in `./risk-model/src/risk-model/pipelines/<pipeline_name>/pipeline.py`.


The functionality of each step/pipeline (also known as a *node*) is defined in `./risk-model/src/risk-model/pipelines/<pipeline_name>/node.py`.


## Notebooks

Aside from creating a pipeline, we can use notebooks to explore our datasets. For example, during the data processing step, we can explore our data independently using a Jupyter notebook before building the `data_processing` pipeline (so that we don't have to run a pipeline every time, e.g. just to check the shape and columns of the dataset), as seen in `./risk-model/notebooks/data_processing.ipynb`.

To be able to run the notebook, you first need to start the Kedro Jupyter Notebook server:

```bash
kedro jupyter notebook
```

## Parameters

Each pipeline has a corresponding parameters file in `./risk-model/conf/base`, where, for instance, model parameters which need tuning can be defined.

They are fed to the node in `pipeline.py` under `inputs` using`params:<param_name>` and fed to the `node.py` as a function parameter, unpacked using `**`; example usage: `**params`.

## Important Note

All `kedro` commands are run from the Kedro project directory (`./risk-model`).

## TODO
- adding a hyperparameter tuning pipeline
- adding SHAP explanations
