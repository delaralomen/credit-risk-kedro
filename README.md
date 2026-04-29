# Credit Risk Prediction Pipeline

This project is an end-to-end credit risk modeling system using the LendingClub dataset and built with [Kedro (QuantumBlack Labs at McKinsey)](https://kedro.org/), an open-source framework for data engineering and data science code. It compares Logistic Regression with XGBoost, and enforces a clean separation of concerns between data engineering, modeling, and evaluation steps.


## Overview

This project builds a full ML workflow to assess whether a borrower is likely to default on a loan.

Key goals:

* Predict credit default risk
* Compare linear vs non-linear models
* Build a reproducible ML pipeline
* Interpret model predictions using SHAP




## Results

| Model               | Accuracy | ROC-AUC |
| - | -- | -- |
| Logistic Regression | 0.803    | 0.708    |
| XGBoost             | 0.804    | 0.720    |

**Finding:** Both models capture patterns in loan data similarly, with the XGBoost non-linear model at a minimal advantage.



## Model Interpretability (SHAP)

We use SHAP (SHapley Additive exPlanations) to understand how features influence model predictions.

<p align="center">
  <img src="img/shap_summary.png" alt="SHAP Summary" width="500"/>
</p>

Key insights:

* Interest rate is the strongest driver of default risk
* Loan term and credit score also significantly influence predictions
* Loan-to-income ratio plays a role but is less dominant
* Several features show non-linear effects on model output


## Dataset

This project uses the LendingClub dataset available on Kaggle:
https://www.kaggle.com/datasets/wordsforthewise/lending-club


## Project Workflow

The pipeline follows a standard ML lifecycle:

1. Data ingestion (LendingClub dataset)
2. Data cleaning and preprocessing
3. Feature engineering
4. Train/test split
5. Model training (Logistic Regression, XGBoost)
6. Model selection (cross-validation)
7. Hyperparameter tuning
8. Model evaluation
9. Interpretation with SHAP



## Tech Stack

* Python
* Kedro
* Pandas / NumPy
* Scikit-learn
* XGBoost
* SHAP



## Project Structure

```
credit-risk-kedro/
│
├── risk-model/        # Kedro project (pipelines & core logic)
├── reports/           # Figures (SHAP plots)
└── README.md          # This file
```

> For detailed pipeline implementation and developer instructions, see the Kedro project README inside <a href="https://github.com/delaralomen/credit-risk-kedro/tree/main/risk-model" target="_blank">`risk-model/`</a>.



## Future Improvements

* Deploy model as an API
* Add more advanced feature engineering
* Experiment with additional models (e.g., LightGBM, neural networks)
* Improve calibration and probability estimates



## Getting Started

```bash
git clone https://github.com/your-username/credit-risk-kedro.git
cd credit-risk-kedro/risk-model
conda env create -f environment.yml
pip install -r requirements.txt
kedro run
```



