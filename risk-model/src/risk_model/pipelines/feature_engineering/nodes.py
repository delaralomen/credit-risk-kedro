"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 1.2.0
"""
import pandas as pd


def create_features(df):
    df = df.copy()

    # --- term ---
    df["term"] = df["term"].str.extract(r"(\d+)").astype(float)

    # --- emp_length ---
    df["emp_length"] = df["emp_length"].str.extract(r"(\d+)").astype(float)

    # --- fico ---
    df["fico_score"] = (df["fico_range_low"] + df["fico_range_high"]) / 2
    df = df.drop(columns=["fico_range_low", "fico_range_high"])

    # --- grade ordinal ---
    grade_map = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7}
    df["grade"] = df["grade"].map(grade_map)

    # --- categorical ---
    categorical_cols = [
        "home_ownership",
        "verification_status",
        "purpose"
    ]

    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    # --- missing values ---
    df = df.fillna(df.median(numeric_only=True))

    return df