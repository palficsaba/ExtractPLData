import pandas as pd
import sys

sys.path.append('Home/PyCharmProjects/ExtractPLData/.venv/Modules')
import referees as ref
import teams as tm


file_location = '/home/csaba/Documents/Betting/PremierLeagueTripleSolo2023-24.xlsx'
extracted_data_location = '/home/csaba/Documents/Betting/ExtractedPLData.xlsx'
read_info = pd.read_excel(file_location)

referees_list = ref.referee_list(read_info)
referees_nr_games = ref.referee_nr_games(referees_list, read_info)
referees_avg_card_nr = ref.referee_avg_card_nr(referees_nr_games, read_info)
referee_history = ref.referee_history(referees_list, read_info)

referee_history = pd.DataFrame(referee_history)
referee_history.to_excel(extracted_data_location, index=False)







