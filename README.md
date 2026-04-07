# Credit Risk Modeling Using Kedro Pipeline

## Install Dependencies

```bash
conda env create -f environment.yml
```

## Start Pipeline

```bash
conda run
```

## Dataset
LendingClub, the dataset used in this project, can be found [here](https://www.kaggle.com/datasets/wordsforthewise/lending-club).

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


## Data Ingestion

**1. Create the pipeline**

```bash
kedro pipeline create data_ingestion
```

**2. Run the pipeline**

```bash
kedro run --pipeline=data_ingestion
```

**3. Check out the downloaded files**

```bash
ls data/raw/
```

