# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_stats.ipynb.

# %% auto 0
__all__ = ['table_names', 'get_tab_as_df']

# %% ../nbs/01_stats.ipynb 3
from .connect import *

# %% ../nbs/01_stats.ipynb 4
table_names = ["tournament", "match", "game", "player", "team"]

# %% ../nbs/01_stats.ipynb 6
def get_tab_as_df(table_name:str):
    "Returns a pandas dataframe for a given table"
    if not isinstance(table_name, str):
        raise TypeError(f"table_name must be a string within {table_names}")
    if table_name not in table_names:
        raise ValueError(f"Table name {table_name} is not a name in table_names")
    params = config()
    conn = DbConnection(params)
    df = conn.pull_data(table_name)
    return df
