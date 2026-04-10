"""
This is a boilerplate pipeline 'split_data'
generated using Kedro 1.2.0
"""
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

def split_data(df):
    X = df.drop(columns=["target"])
    y = df["target"]

    print("Any inf:", np.isinf(X).any().any())
    print("Any NaN:", X.isna().any().any())
    print("Max value:", X.max().max())

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # --- Feature scaling (unscaled feature: fico_score) ---
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)


    # --- Ensure pandas ---
    X_train = pd.DataFrame(X_train, columns=X.columns)
    X_test = pd.DataFrame(X_test, columns=X.columns)

    y_train = pd.DataFrame(y_train, columns=["target"])
    y_test = pd.DataFrame(y_test, columns=["target"])
    
    return X_train, X_test, y_train, y_test