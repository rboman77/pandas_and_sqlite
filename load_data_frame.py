"""
Simple example of how to load a pandas data frame from an sqlite file.
"""
import pathlib
import sqlite3
import sys

import pandas as pd

# This is to suppress warnings from mypy about pandas.
# mypy: disable-error-code=import

# Testing github.

# Data folder is relative to the location of this file.
code_folder = pathlib.Path(__file__).resolve().parents[0]
data_folder = code_folder.parents[0] / 'data'
input_file = data_folder / 'pandas_sqlite.sqlite'
if not input_file.exists():
    print('not found:', input_file)
    sys.exit(1)

conn = sqlite3.connect(input_file)
data_frame = pd.read_sql_query('select * from simple_table', conn)
print(data_frame)
