"""
This is a boilerplate pipeline 'model_training'
generated using Kedro 1.2.0
"""
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import pandas as pd




def train_model(df):
    X = df.drop(columns=["target"])
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # --- Feature scaling (unscaled feature: fico_score) ---
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # --- Feature importance ---
    importance = pd.Series(
        model.coef_[0],
        index=X.columns
    ).sort_values(key=abs, ascending=False)

    print("\nTop 10 important features:")
    print(importance.head(10))

    return model