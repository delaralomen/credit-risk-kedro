"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 1.2.0
"""
import pandas as pd

def clean_loans(df: pd.DataFrame) -> pd.DataFrame:
    # filter valid target rows
    df = df[df["loan_status"].isin(["Fully Paid", "Charged Off"])]

    # create target
    df["target"] = df["loan_status"].map({
        "Fully Paid": 0,
        "Charged Off": 1
    })

    # select useful features
    selected_features = [
        "loan_amnt",
        "term",
        "int_rate",
        "grade",
        "emp_length",
        "home_ownership",
        "annual_inc",
        "verification_status",
        "purpose",
        "dti",
        "fico_range_low",
        "fico_range_high",
        "delinq_2yrs",
        "inq_last_6mths",
        "target"
    ]

    df = df[selected_features]

    return df