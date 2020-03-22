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
    'Province/State',
    'Last Update',
    'Confirmed',
    'Deaths',
    'Recovered',
]


def read_csv(csv):
    return pd.read_csv(csv, dtype=dtype, usecols=columns, na_values="").fillna(0)


def file_list(path: str):
    return [read_csv(f) for f in g.glob(path)]


def read_files():
    return pd.concat(
        file_list('daily_reports/*.csv'),
        ignore_index=True
    )
