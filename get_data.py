import pandas as pd
import numpy as np

def get_data(file):
    raw_data = pd.read_csv(file)
    return raw_data

df = get_data("raw_data.csv")
#print(df)