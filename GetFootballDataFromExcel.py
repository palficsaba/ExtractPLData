import pandas as pd
import sys

sys.path.append('Home/PyCharmProjects/ExtractPLData/src/Modules')
import referees as rf
import teams as tm


file_location = '/home/csaba/Documents/Betting/PremierLeagueTripleSolo2023-24.xlsx'
extracted_data_location = '/home/csaba/Documents/Betting/ExtractedPLData.xlsx'
read_info = pd.read_excel(file_location)

referees_list = rf.referees_list(read_info)
referees_nr_games = rf.referees_nr_games(referees_list, read_info)
referees_avg_card_nr = rf.referees_avg_card_lines(referees_nr_games, read_info)
referee_history = rf.referees_history(referees_list, read_info)

# referee_history = pd.DataFrame(referee_history)
# referee_history.to_excel(extracted_data_location, index=False)

referees_top_team_cards = {}
for name in referees_list:
    nr_cards = rf.referee_teams_cards(name, read_info, tm.traditional_big_teams)
    referees_top_team_cards[name] = nr_cards

print(referees_top_team_cards)

# pd.set_option('display.max_columns', None)
# print(read_info.head())


