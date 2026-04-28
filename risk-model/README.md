# Risk Model

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)

## Overview

This Kedro project was generated using `kedro 1.2.0`.

Take a look at the [Kedro documentation](https://docs.kedro.org) for more information.



## Dataset

The project uses the **LendingClub loan dataset**, available on Kaggle:
[https://www.kaggle.com/datasets/wordsforthewise/lending-club](https://www.kaggle.com/datasets/wordsforthewise/lending-club)

### Kaggle Setup

To reproduce the project, configure your Kaggle API key:

**File:** `~/.kaggle/kaggle.json`

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



## Installation

### Using Conda (recommended)

```bash
conda env create -f environment.yml
```

### Using pip

```bash
pip install -r requirements.txt
pip install "kedro[pandas]"
```



## Project Structure

The project is organized into modular Kedro pipelines in:

```
src/risk-model/pipelines/
```

### Pipeline Components

* **Pipeline definition:**
  `pipeline.py`

* **Node logic (functions):**
  `node.py`

* **Data catalog (inputs/outputs):**
  `conf/base/catalog.yml`



## Running the Project

All commands must be executed from the project root (`./risk-model`).

### Run full pipeline

```bash
kedro run
```

### Run a specific pipeline

```bash
kedro run --pipeline=<pipeline_name>
```



## Parameters

Each pipeline has configurable parameters stored in:

```
conf/base/
```

Usage in pipeline:

```python
inputs=["params:<param_name>"]
```

Usage in node:

```python
def my_function(..., **params):
```



## Notebooks

You can explore data interactively using Jupyter notebooks.

### Start notebook server

```bash
kedro jupyter notebook
```

### Alternative environments

* JupyterLab:

  ```bash
  kedro jupyter lab
  ```

* IPython:

  ```bash
  kedro ipython
  ```

Kedro automatically provides useful variables in notebooks:

* `context`
* `session`
* `catalog`
* `pipelines`



## Testing

Run tests using:

```bash
pytest
```

See:

```
tests/test_run.py
```

Coverage settings can be configured in:

```
pyproject.toml
```



## Project Guidelines

* Store local configs are stored in:

  ```
  conf/local/
  ```



## Dependencies

All dependencies are listed in:

```
requirements.txt
```

Install with:

```bash
pip install -r requirements.txt
```



## Working with Notebooks in Git

To remove notebook output before committing:

Use [`nbstripout`](https://github.com/kynan/nbstripout):

```bash
nbstripout --install
```



## Packaging & Documentation

Refer to Kedro docs for packaging:
[https://docs.kedro.org/en/stable/deploy/package_a_project/](https://docs.kedro.org/en/stable/deploy/package_a_project/)



## Notes

* All Kedro commands must be run from the project root directory.
* Pipelines must have their inputs/outputs defined before execution.
