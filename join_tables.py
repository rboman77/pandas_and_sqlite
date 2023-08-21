"""
Simple example of how to join two tables that were saved in sqlite.
Note that pandas has it's join as well.
"""
import pathlib
import sqlite3

import pandas as pd

# This is to suppress warnings from mypy about pandas.
# mypy: disable-error-code=import

# Data folder is relative to the location of this file.
code_folder = pathlib.Path(__file__).resolve().parents[0]
data_folder = code_folder.parents[0] / 'data'
if not data_folder.exists():
    data_folder.mkdir()

table_a = pd.DataFrame({
    'month': ('January', 'February', 'March'),
    'revenue': (1000, 2000, 1500)
})
table_b = pd.DataFrame({
    'month': ('January', 'February', 'March'),
    'expenses': (900, 950, 975)
})

conn = sqlite3.connect(data_folder / 'sqlite_join.sqlite')

table_a.to_sql('table_a', conn, if_exists='replace', index=False)
table_b.to_sql('table_b', conn, if_exists='replace', index=False)

QUERY = """
SELECT table_a.month, table_a.revenue, table_b.expenses
from table_a
INNER JOIN table_b
ON table_a.month = table_b.month
"""
joined_table = pd.read_sql_query(QUERY, conn)

print('table a')
print(table_a)
print('table_b')
print(table_b)
print('joined')
print(joined_table)
