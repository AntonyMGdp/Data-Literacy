import pandas as pd

# Read the input Excel file
input_file = 'lichess_tournament_2023-spring-marathon_game_info.xlsx'
df = pd.read_excel(input_file)

# Compute the bins using cut based on 'winner_loser_elo_diff' column
num_bins = 20  # Adjust the number of bins as per your preference
df['elo_diff_bins'] = pd.cut(df['winner_loser_elo_diff'], num_bins, include_lowest=True)

# Group the data by 'elo_diff_bins' and calculate the count of games in each bin
result = df.groupby('elo_diff_bins').size().reset_index(name='count')

# Create a new DataFrame with elo_diff_bins as columns and counts as values
output_df = pd.DataFrame()
output_df['elo_diff_bins'] = result['elo_diff_bins']
output_df['count'] = result['count']

# Transpose the DataFrame to have the elo_diff_bins as columns
output_df = output_df.pivot(columns='elo_diff_bins', values='count')

# Output the result to a new Excel file
output_file = 'elo_analysis.xlsx'
output_df.to_excel(output_file, index=False)
