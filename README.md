pklshop
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

A library for accessing and analyzing Pickleball data from
[pklmart](https://github.com/aspancake/pklmart). You can find the full
documentation [here](https://nolan-smyth.com/pklshop/).

## Install

Install using:

``` sh
pip install pklshop
```

## How to use

This package includes the latest pickleball data from pklmart already
convieniently loaded into pandas dataframes. You can access this data by
importing the `pklshop.data` module using:

``` python
from pklshop.data import *
```

(Note that since this package is writen using
[nbdev](https://nbdev.fast.ai/) it is safe to wildcard import because
the `__all__` variable is automatically generated for each module.)

Available dataframes are:

``` python
table_names
```

    ['tournament',
     'match',
     'game',
     'rally',
     'shot_type_ref',
     'shot',
     'player',
     'team']

``` python
print(type(team))
team.columns
```

    <class 'pandas.core.frame.DataFrame'>

    Index(['team_id', 'player_id', 'player_seq_nbr', 'team_nm', 'maint_dtm',
           'maint_app', 'create_dtm', 'create_app'],
          dtype='object')

There are also built-in classes to help you analyze the data. For
example, you can use the
[`Player`](https://NolanSmyth.github.io/pklshop/player.html#player)
class to get a player’s stats or attributes:

``` python
p = Player("P1")
p2 = Player("P2")
head_to_head(p,p2)
```

    Jesse Irvine has played against Catherine Parenteau in 1 matches and has won 1 times

And likewise for Games, Teams, Matches, and Rallys. e.g.:

``` python
g = Game("G1")
g.summarize_game()
```

    Anna Leigh Waters & Leigh Waters beat Jesse Irvine & Catherine Parenteau 12-10 in game G1
                 Player  Error %  Winner %
           Jesse Irvine    17.46      9.52
    Catherine Parenteau     1.59      0.00
      Anna Leigh Waters     1.59      3.17
           Leigh Waters     9.52      4.76

``` python
g.plot_impact_flow()
```

![](index_files/figure-commonmark/cell-6-output-1.png)

To see a more complete analysis in action, check out the
[examples](https://github.com/NolanSmyth/pklshop/tree/main/examples).
For more details, look at the source notebooks in the
[nbs](https://github.com/NolanSmyth/pklshop/tree/main/nbs) directory.
Also check out Connor and
[this](https://github.com/conner-mcnicholas/pickleball_analysis/)
analysis by conner-mcnicholas on timeout momentum!

r = Rally(“R1020”) r.animate_rally() ![Fun
Vizualizations!](figures/rally.gif)
