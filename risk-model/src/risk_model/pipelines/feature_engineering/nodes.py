"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 1.2.0
"""
import pandas as pd
import numpy as np


def create_features(df, params):
    df = df.copy()

    use_log = params["use_log"]
    use_ratios = params["use_ratios"]
    use_interactions = params["use_interactions"]

    # --- term (string → numeric) ---
    if "term" in df.columns:
        df["term"] = df["term"].str.extract(r"(\d+)").astype(float)

    # --- emp_length ---
    if "emp_length" in df.columns:
        def parse_emp_length(x):
            if pd.isna(x):
                return None
            if "<" in str(x):
                return 0.5
            if "+" in str(x):
                return 10
            return float(str(x).split()[0])

        df["emp_length"] = df["emp_length"].apply(parse_emp_length)

    # --- fico ---
    if {"fico_range_low", "fico_range_high"}.issubset(df.columns):
        df["fico_score"] = (df["fico_range_low"] + df["fico_range_high"]) / 2
        df["fico_range"] = df["fico_range_high"] - df["fico_range_low"]
        df = df.drop(columns=["fico_range_low", "fico_range_high"])

    # --- grade ---
    if "grade" in df.columns:
        grade_map = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7}
        df["grade"] = df["grade"].map(grade_map)

    # --- sub_grade ---
    if "sub_grade" in df.columns:
        df["sub_grade_num"] = df["sub_grade"].str.extract(r"(\d)").astype(float)
        df = df.drop(columns=["sub_grade"])

    # --- log features ---
    if use_log:
        df["log_annual_inc"] = np.log1p(df["annual_inc"])
        df["log_loan_amnt"] = np.log1p(df["loan_amnt"])
        df["log_dti"] = np.log1p(df["dti"])
        df["log_revol_bal"] = np.log1p(df["revol_bal"])

    # --- ratios ---
    if use_ratios:
        df["loan_to_income"] = df["loan_amnt"] / (df["annual_inc"] + 1)
        df["interest_burden"] = df["loan_amnt"] * df["int_rate"] / 100
        df["revol_to_income"] = df["revol_bal"] / (df["annual_inc"] + 1)

    # --- credit behavior ---
    df["credit_events"] = df["delinq_2yrs"] + df["inq_last_6mths"]

    # --- interactions ---
    if use_interactions:
        df["fico_x_income"] = df["fico_score"] * df["annual_inc"]
        df["grade_x_dti"] = df["grade"] * df["dti"]

    # --- categorical ---
    df = pd.get_dummies(
        df,
        columns=["home_ownership", "verification_status", "purpose"],
        drop_first=True
    )

    # --- replace infinity with nan ---
    df = df.replace([np.inf, -np.inf], np.nan)

    # --- missing ---
    df = df.fillna(df.median(numeric_only=True))

    return df