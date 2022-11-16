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

First, you’ll need to setup a `database.ini` file (it’s only about 5
lines). This should be stored in the `pklshop` root directory. Check out
`connect` for an example of how to write this.

Once that’s done, this lib provides a function
[`get_tab_as_df`](https://NolanSmyth.github.io/pklshop/data.html#get_tab_as_df)
you can use to create and display tables within the database

Available tables are:

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
match_df = get_tab_as_df("match")
match_df.head()
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>match_id</th>
      <th>tourn_id</th>
      <th>consol_ind</th>
      <th>team_id_1</th>
      <th>team_id_2</th>
      <th>maint_dtm</th>
      <th>maint_app</th>
      <th>create_dtm</th>
      <th>create_app</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>M1</td>
      <td>T1</td>
      <td>N</td>
      <td>T1</td>
      <td>T2</td>
      <td>2022-04-09 03:19:33.840951+00:00</td>
      <td>postgres</td>
      <td>2022-04-09 03:19:33.840951+00:00</td>
      <td>postgres</td>
    </tr>
    <tr>
      <th>1</th>
      <td>M2</td>
      <td>T2</td>
      <td>N</td>
      <td>T2</td>
      <td>T3</td>
      <td>2022-05-26 00:45:11.301752+00:00</td>
      <td>postgres</td>
      <td>2022-05-26 00:45:11.301752+00:00</td>
      <td>postgres</td>
    </tr>
    <tr>
      <th>2</th>
      <td>M5</td>
      <td>T5</td>
      <td>N</td>
      <td>T6</td>
      <td>T5</td>
      <td>2022-06-28 00:40:22.948360+00:00</td>
      <td>postgres</td>
      <td>2022-06-28 00:40:22.948360+00:00</td>
      <td>postgres</td>
    </tr>
    <tr>
      <th>3</th>
      <td>M6</td>
      <td>T6</td>
      <td>N</td>
      <td>T5</td>
      <td>T7</td>
      <td>2022-07-07 23:01:45.921540+00:00</td>
      <td>postgres</td>
      <td>2022-07-07 23:01:45.921540+00:00</td>
      <td>postgres</td>
    </tr>
    <tr>
      <th>4</th>
      <td>M7</td>
      <td>T7</td>
      <td>N</td>
      <td>T8</td>
      <td>T9</td>
      <td>2022-07-11 02:40:50.597016+00:00</td>
      <td>postgres</td>
      <td>2022-07-11 02:40:50.597016+00:00</td>
      <td>postgres</td>
    </tr>
  </tbody>
</table>
</div>

To see a more complete analysis in action, check out the
[examples](https://github.com/NolanSmyth/pklshop/tree/main/examples).
Also check out Connor and
[this](https://github.com/conner-mcnicholas/pickleball_analysis/)
analysis by conner-mcnicholas on timeout momentum!
