from datareader import read_files
from database import add_report

for index, row in read_files().iterrows():
    add_report(
        row['Country/Region'],
        row['Province/State'],
        row['Last Update'],
        row['Confirmed'],
        row['Deaths'],
        row['Recovered']
    )
