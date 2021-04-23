import pandas as pd
import sqlite3 as sql

conn = sql.connect('Student.db')
data = pd.read_csv('student.csv')

data.to_sql('Student',conn, if_exists='replace',index=False)
cur = conn.cursor()

conn.close()