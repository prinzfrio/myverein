import pandas as pd

def import_prowinner_csv(path):
    df = pd.read_csv(path, sep=";")
    return df
