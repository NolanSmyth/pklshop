# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_name.ipynb.

# %% auto 0
__all__ = ['get_team_name', 'get_team_id', 'get_player_name', 'get_player_id']

# %% ../nbs/02_name.ipynb 3
from .data import *
import pandas as pd

# %% ../nbs/02_name.ipynb 4
def get_team_name(team_id: str) -> str:
    '''
    Returns the name of the team with team_id
    Optionally pass a team_df to use a different table
    '''
    if team_id in team.team_id.values:
        return team[team.team_id == team_id].team_nm.values[0]
    else:
        raise ValueError(f"team_id \"{team_id}\" not found in team_df")

def get_team_id(team_name: str) -> str:
    '''
    Returns the team_id of the team with team_name
    Optionally pass a team_df to use a different table
    '''
    if team_name in team.team_nm.values:
        return team[team.team_nm == team_name].team_id.values[0]
    else:
        raise ValueError(f"team_name \"{team_name}\" not found in team_df")

def get_player_name(player_id: str) -> str:
    '''
    Returns the name of the player with player_id
    Optionally pass a player_df to use a different table
    '''
    if player_id in players.player_id.values:
        return players[players.player_id == player_id].first_nm.values[0] + " " + players[players.player_id == player_id].last_nm.values[0]
    else:
        raise ValueError(f"player_id \"{player_id}\" not found in player_df")

def get_player_id(player_name: str) -> str:
    '''
    Returns the player_id of the player with player_name
    Optionally pass a player_df to use a different table
    '''
    full_names = players.first_nm.values + " " + players.last_nm.values
    if player_name in full_names:
        return players[(players.first_nm + " " + players.last_nm) == player_name].player_id.values[0]
    else:
        raise ValueError(f"player_name \"{player_name}\" not found in player_df")
