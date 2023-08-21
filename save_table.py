"""
Simple example of how to save a pandas data frame to an sqlite file.
"""
import pathlib
import sqlite3

import pandas as pd

# This is to suppress warnings from mypy about pandas.
# mypy: disable-error-code=import


def generate_data_frame() -> pd.DataFrame:
    """Generate a test pandas data frame."""
    return pd.DataFrame({'col_a': [1, 2, 3, 4, 5], 'col_b': [6, 7, 8, 9, 10]})


def save_data_frame(frame: pd.DataFrame, path: pathlib.Path, table_name: str):
    """Save the data frame to sqlite."""
    conn = sqlite3.connect(path)
    frame.to_sql(table_name, conn, if_exists='replace')


# Data folder is relative to the location of this file.
code_folder = pathlib.Path(__file__).resolve().parents[0]
data_folder = code_folder.parents[0] / 'data'
if not data_folder.exists():
    print('creating data folder')
    data_folder.mkdir()

data_frame = generate_data_frame()

save_data_frame(data_frame, data_folder / 'pandas_sqlite.sqlite',
                'simple_table')

