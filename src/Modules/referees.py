import pandas as pd


def referees_list(read_info: pd.DataFrame) -> list:
    return read_info['referees'].unique()


def referees_nr_games(referees_list: list, read_info: pd.DataFrame) -> dict:
    referees_nr_games = {}

    for element in referees_list:
        filtered_df = read_info[read_info['referees'] == element]
        referees_nr_games[element] = filtered_df.shape[0]

    return referees_nr_games


def referees_avg_card_lines(referees_nr_games: dict, read_info: pd.DataFrame) -> dict:
    referee_average_card_nr = {}

    for key, value in referees_nr_games.items():
        filtered_df = read_info[read_info['referees'] == key]
        nr_cards = (filtered_df['Hyellows'].sum() + filtered_df['Ayellows'].sum()) / value
        referee_average_card_nr[key] = round(nr_cards, 2)

    return referee_average_card_nr


def referees_history(referee_list: list, read_info: pd.DataFrame) -> dict:
    history = {}

    for element in referee_list:

        referee_history = {}

        filtered_df = read_info[read_info['referees'] == element]
        for index, row in filtered_df.iterrows():
            match_name = f"{row['Home']}-{row['Away']}"
            referee_history[match_name] = row['Hyellows'] + row['Ayellows']
        history[element] = referee_history

    return history

"""
Parameters: 
referee_name: the referee's name
read_info: the DataFrame 
teams: a list with team names (check correct names) 

Returns
Calculates nr of cards, or average nr of cards given by a referee for a list of teams
if per_games is set to True, than the function 
"""
def referee_teams_cards(
        referee_name: str,
        read_info: pd.DataFrame,
        teams: list,
        per_games=False,
        home_results=False,
        away_results=False,
        in_form_teams=False,
        out_of_form_teams=False
):
    df = read_info[read_info['referees'] == referee_name]
    nr_games = len(df)
    nr_cards = df[df['Home'].isin(teams)]['Hyellows'].sum()

    if per_games:
        nr_cards = nr_cards/nr_games

    return nr_cards


