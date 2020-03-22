import glob as g
import pandas as pd
import numpy as np

dtype = {
    'Province/State': str,
    'Country/Region': str,
    'Confirmed': np.float64,
    'Deaths': np.float64,
    'Recovered': np.float64
}

columns = [
    'Country/Region',
    'Last Update',
    'Confirmed',
    'Deaths',
    'Recovered',
]


def read_csv(csv):
    return pd.read_csv(csv, dtype=dtype, parse_dates=['Last Update'], usecols=columns, na_values="").fillna(0)


def read_files():
    csvs = [read_csv(f) for f in g.glob('*.csv')]
    return pd.concat(csvs, ignore_index=True)
