import pandas as pd
import numpy as np

# Read the Excel file
data = pd.read_excel('lichess_tournament_2023-spring-marathon_game_info.xlsx')

# Calculate the mean ELO for each game
data['mean_elo'] = (data['white_elo'] + data['black_elo']) / 2

# Define the number of elo groups and calculate the elo ranges
num_groups = 9

# Calculate the elo ranges
elo_ranges, bins = pd.qcut(data['mean_elo'], num_groups, retbins=True)

# Map elo range labels to elo ranges
elo_labels = [f'{int(bins[i])}-{int(bins[i+1])}' for i in range(len(bins)-1)]+["elo ranges"]

# Group the data by ECO and elo ranges
grouped_data = data.groupby(['eco', elo_ranges])

# Calculate the number of games and mean ELO for each group
result = grouped_data['eco'].count().unstack().fillna(0)
result['mean_elo'] = grouped_data['mean_elo'].mean()

result.columns = elo_labels

# Save the result to a new Excel file
result.to_excel('chess_openings_stats.xlsx')
