import sqlite3
import pandas as pd

try:
    conn = sqlite3.connect('../data/traffic.db')
    df = pd.read_sql("select * from traffic where cast(substr(date_time, 1, 4) as integer) >= 2013", conn)
    df.to_csv('../data/traffic.csv', index = False)
except:
    print("Data was NOT extracted")
    print("Have you downloaded and saved traffic.db into the data folder?")
