# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_data.ipynb.

# %% auto 0
__all__ = ['table_names', 'table_dict', 'rally', 'players', 'game', 'team', 'match', 'shot', 'tournament', 'load_dfs_from_csv',
           'get_tab_as_df', 'database_tables_to_csv']

# %% ../nbs/01_data.ipynb 4
from .connect import *
import pkgutil
from io import BytesIO
import pandas as pd

# %% ../nbs/01_data.ipynb 5
table_names = ["tournament", "match", "game", "rally", "shot_type_ref", "shot", "player", "team",]

# %% ../nbs/01_data.ipynb 8
#This is a function to get the dataframes from the csv files
def load_dfs_from_csv():
    "Returns a dictionary of dataframes from the table csv files"
    table_dict = {}
    for table_name in table_names:
        table_dat = pkgutil.get_data('pklshop', f"datasets/{table_name}.csv")
        df = pd.read_csv(BytesIO(table_dat))
        table_dict[table_name] = df
    return table_dict

table_dict = load_dfs_from_csv()

rally = table_dict["rally"]
players = table_dict["player"]
game = table_dict["game"]
team = table_dict["team"]
match = table_dict["match"]
shot = table_dict["shot"]
tournament = table_dict["tournament"]

# %% ../nbs/01_data.ipynb 10
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

# %% ../nbs/01_data.ipynb 14
#Pull data from the database and save it to csv files. Only need to do this when the datbase is updated.
def database_tables_to_csv():
    "Saves the dataframes to csv files"
    for table_name in table_names:
        df = get_tab_as_df(table_name)
        df.to_csv(f"datasets/{table_name}.csv", index=False)
