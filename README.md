# Credit Risk Modeling Using Kedro Pipeline

## Install Dependencies

```bash
conda env create -f environment.yml
```

## Start Pipeline

```bash
conda run
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

