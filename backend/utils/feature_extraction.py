import numpy as np
import pandas as pd

def engineer_features(df):
    # Normalize continuous variables
    df["Humidity_norm"] = (df["Humidity"] - df["Humidity"].mean()) / df["Humidity"].std()
    df["Temperature_norm"] = (df["Temperature"] - df["Temperature"].mean()) / df["Temperature"].std()
    df["StepCount_norm"] = (df["StepCount"] - df["StepCount"].mean()) / df["StepCount"].std()

    # Derived features
    df["Temp_Humidity_ratio"] = df["Temperature"] / (df["Humidity"] + 1e-5)
    df["Activity_level"] = pd.cut(df["StepCount"], bins=[0,50,150,300], labels=["Low","Medium","High"])

    return df