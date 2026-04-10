"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 1.2.0
"""
import numpy as np
import pandas as pd


def clean_loans(df: pd.DataFrame, params) -> pd.DataFrame:
    df = df.copy()

    # --- filter valid target rows ---
    df = df[df["loan_status"].isin(["Fully Paid", "Charged Off"])]

    # --- create target ---
    df["target"] = df["loan_status"].map({
        "Fully Paid": 0,
        "Charged Off": 1
    })

    # --- explicitly drop leakage columns if present ---
    leakage_cols = [
        "recoveries",
        "collection_recovery_fee",
        "last_pymnt_amnt",
        "last_pymnt_d",
        "total_pymnt",
        "total_pymnt_inv",
        "total_rec_prncp",
        "total_rec_int",
        "total_rec_late_fee",
        "last_credit_pull_d",
        "next_pymnt_d"
    ]

    df = df.drop(columns=[col for col in leakage_cols if col in df.columns], errors="ignore")

    if params['pure_model']:
        df = df.drop(columns=["grade","sub_grade"], errors="ignore")

    # --- core + extended feature set ---
    selected_features = [
        # loan info
        "loan_amnt",
        "term",
        "int_rate",

        # credit quality
        "grade",
        "sub_grade",  # if available
        "fico_range_low",
        "fico_range_high",

        # financials
        "annual_inc",
        "dti",

        # credit behavior
        "delinq_2yrs",
        "inq_last_6mths",
        "pub_rec",

        # credit structure (VERY important)
        "revol_bal",
        "revol_util",
        "open_acc",
        "total_acc",

        # borrower profile
        "emp_length",
        "home_ownership",
        "verification_status",
        "purpose",

        # target
        "target"
    ]

    # --- keep only columns that exist ---
    available_features = [col for col in selected_features if col in df.columns]
    df = df[available_features]
    
    print("\n=== FINAL COLUMNS ===")
    print(df.dtypes)

    return df