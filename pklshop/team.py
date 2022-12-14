# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/08_team.ipynb.

# %% auto 0
__all__ = ['Team']

# %% ../nbs/08_team.ipynb 3
from .data import *
from .name import *
from .game import *
from .match import *
import pandas as pd
import matplotlib.pyplot as plt

# %% ../nbs/08_team.ipynb 4
class Team:
    ''' A class to represent a team'''
    def __init__(self, team_id: str):
        self.team_id = team_id
        self.team = team[team["team_id"] == team_id]
        self.team_name = self.team["team_nm"].values[0]
        self.players = self.team.player_id.values

        game_mask = (game.w_team_id == self.team_id) | (game.l_team_id == self.team_id)
        self.game = game[game_mask]
        
        self.games_played = self.game.game_id.values
        self.num_games_played = len(self.games_played)
        self.games_won = self.game[self.game.w_team_id == self.team_id].game_id.values
        self.num_games_won = len(self.games_won)
    
    def summarize_team(self) -> None:
        '''Prints a summary of the team'''
        print(f"{self.team_name} have played {self.num_games_played} games and won {self.num_games_won} games")

    def __str__(self):
        return self.team_name
    __repr__ = __str__

