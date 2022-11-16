# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_game.ipynb.

# %% auto 0
__all__ = ['Game']

# %% ../nbs/03_game.ipynb 3
from .data import *
from .stats import *
from .name import *
import pandas as pd

# %% ../nbs/03_game.ipynb 6
class Game:
    """
    A class to represent a game of pickleball.
    """
    def __init__(self, game_id:str):
        #Create dfs for this game
        self.game_id = game_id
        self.rally = rally[rally.game_id == game_id]
        self.num_rallies = len(self.rally)
        self.game = game[game.game_id == game_id]

        #get the teams and players for this game
        self.w_team_id = self.game[self.game.game_id == self.game_id].w_team_id.values[0]
        self.l_team_id = self.game[self.game.game_id == self.game_id].l_team_id.values[0]
        self.team = team[team.team_id.isin([self.w_team_id, self.l_team_id])]
        self.p1, self.p2 = self.team[self.team.team_id == self.w_team_id].player_id.values #winning players are p1 and p2
        self.p3, self.p4 = self.team[self.team.team_id == self.l_team_id].player_id.values #losing team are p3 and p4

        self.players = players[players.player_id.isin([self.p1, self.p2, self.p3, self.p4])]
        
        self.w_team_name = get_team_name(self.w_team_id, self.team)
        self.l_team_name = get_team_name(self.l_team_id, self.team)

        #get the scores
        self.score_w = self.game[self.game.game_id == self.game_id].score_w.values[0]
        self.score_l = self.game[self.game.game_id == self.game_id].score_l.values[0]

    def __str__(self):
        return "Game({})".format(self.game_id)
    __repr__ = __str__

    def get_error_rate(self, player_id:str):
        """
        Returns the error rate for a given player in a game.
        """
        num_unforced_errors = sum((self.rally.ending_player_id == player_id) & ((self.rally.ending_type == 'Unforced Error') | (self.rally.ending_type == 'Error')))
        return num_unforced_errors/self.num_rallies
    
    def get_winners_rate(self, player_id:str):
        """
        Returns the number of winners for a given player in a game.
        """
        return sum((self.rally.ending_player_id == player_id) & (self.rally.ending_type == 'Winner'))/self.num_rallies

    def first_serve_team(self):
        '''
        Returns the team_id of the team that served first for a given game with game_id.
        '''
        return self.rally[self.rally.rally_nbr == 1].srv_team_id.values[0]

    def first_serve_team_name(self):
        '''
        Returns the team_id of the team that served first for a given game with game_id.
        '''
        first_team_id = self.first_serve_team()
        return self.get_team_name(first_team_id)
        
    def summarize_game(self):
        print("{} beat {} {}-{} in game {}".format(self.w_team_name, self.l_team_name, self.score_w, self.score_l, self.game_id))

        summary_df = pd.DataFrame({'Player': [get_player_name(p_id, self.players) for p_id in self.players.player_id.values]})
        summary_df['Error %'] = [round(self.get_error_rate(p_id)*100,2) for p_id in self.players.player_id.values]
        summary_df['Winner %'] = [round(self.get_winners_rate(p_id)*100,2) for p_id in self.players.player_id.values]
        print(summary_df)

