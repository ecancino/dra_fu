import pandas as pd

from datareader import read_files

df = read_files()

for row in df.iterrows():
    print(row)
