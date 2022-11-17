# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/06_player.ipynb.

# %% auto 0
__all__ = ['Player', 'head_to_head']

# %% ../nbs/06_player.ipynb 3
from .data import *
from .stats import *
from .name import *
from .game import *
from .match import *
import pandas as pd

# %% ../nbs/06_player.ipynb 5
class Player():

    def __init__(self, player_id: str):
        self.player_id = player_id
        self.name = get_player_name(self.player_id)
        self.teams = self.associated_teams()

        self.matches_played = self.matches_played()
        self.num_matches_played = len(self.matches_played)
        self.matches_won = self.matches_won()
        self.num_matches_won = len(self.matches_won)

        self.games_played = self.games_played()
        self.num_games_played = len(self.games_played)
        self.games_won = self.games_won()
        self.num_games_won = len(self.games_won)

    def __str__(self):
        return f"{self.name}, id: {self.player_id}"
    __repr__ = __str__

    def associated_teams(self):
        '''
        Returns the team_ids of the teams that the player played for.
        '''
        return team[team.player_id == self.player_id].team_id.values
    
    def games_played(self):
        '''
        Returns the game_ids of games played (in the database) by the player
        '''
        gs = []
        for team_id in self.teams:
            team_games = game[(game.w_team_id == team_id) | (game.l_team_id == team_id)].game_id.values
            gs += team_games.tolist()
        return gs
    
    def matches_played(self):
        '''
        Returns the match_ids of matches played (in the database) by the player
        '''
        ms = []
        for team_id in self.teams:
            team_matches = match[(match.team_id_1 == team_id) | (match.team_id_2 == team_id)].match_id.values
            ms += team_matches.tolist()
        return ms
        
    def matches_won(self):
        ms = []
        for m_id in self.matches_played:
            m = Match(m_id)
            if m.w_team_id in self.teams:
                ms += [m_id]
        return ms
    
    def games_won(self):
        gs = []
        for g_id in self.games_played:
            g = Game(g_id)
            if g.w_team_id in self.teams:
                gs += [g_id]
        return gs
    
    def summarize_player(self):
        '''
        Prints a summary of the player's stats
        '''
        print(f"Player: {self.name}")
        print(f"Matches played: {self.num_matches_played}")
        print(f"Matches won: {self.num_matches_won}")
        print("Percentage of matches won: {:.2f}%".format(self.num_matches_won/self.num_matches_played*100))
        print(f"Games played: {self.num_games_played}")
        print(f"Games won: {self.num_games_won}")
        print("Percentage of games won: {:.2f}%".format(self.num_games_won/self.num_games_played*100))
        print(f"Teams: {[get_team_name(team) for team in self.teams]}")


# %% ../nbs/06_player.ipynb 10
def head_to_head(p1: Player, p2: Player):
    '''
    Returns the results of matches where p1 and p2 have played against each other
    '''
    p1_matches = p1.matches_played
    p2_matches = p2.matches_played

    p1_count = 0
    p2_count = 0
    for m_id in p1_matches:
        if m_id in p2_matches:
            m = Match(m_id)
            if (p.name in m.w_team_name and p2.name in m.l_team_name):
                p1_count += 1
            elif (p.name in m.l_team_name and p2.name in m.w_team_name):
                p2_count += 1
    print(f"{p1.name} has played against {p2.name} in {p1_count + p2_count} matches and has won {p1_count} times")
