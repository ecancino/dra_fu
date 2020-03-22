import glob
import pandas as pd
import numpy as np

files = glob.glob('daily_reports/*.csv')

dtype = {
    'Province/State': str,
    'Country/Region': str,
    'Confirmed': np.float64,
    'Deaths': np.float64,
    'Recovered': np.float64
}


def read_csv(csv):
    return pd.read_csv(csv, dtype=dtype, parse_dates=['Last Update'], keep_default_na=False)


csvs = [read_csv(f) for f in files]

df = pd.concat(csvs, ignore_index=True)

# summatory = df.groupby('Country/Region').filter(
# lambda row: row['Country/Region'].equals('Italy'))
# .pipe(lambda row: row['Deaths'])
# .sum()

print(df)
