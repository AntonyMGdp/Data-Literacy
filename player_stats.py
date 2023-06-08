import pandas as pd
import numpy as np

def analyze_player_data(excel_file):
    # Read the Excel file
    print("reading file")
    df = pd.read_excel(excel_file)

    # Get unique player usernames
    players = np.union1d(df['white'].astype(str), df['black'].astype(str))

    # Create a list to store player statistics
    player_stats = []

    # Iterate over each player and calculate statistics
    i=0
	
    for player_name in players:
        i+=1
        print("doing: " + player_name +  "\t" + "\t" + "\t" + "\t" + "\t" + "\t" + "   | " + str(i) + "/" + str(len(players)) + "-" + str(int(i/len(players)*10000)/100) + "%")
        # Filter data for the current player
        player_data = df[(df['white'].astype(str) == player_name) | (df['black'].astype(str) == player_name)]

        # Number of played games
        num_games = len(player_data)

        # Calculate Elo gain/loss for the player
        white_elo_diff = player_data.loc[player_data['white'] == player_name, 'white_rating_diff'].sum()
        black_elo_diff = player_data.loc[player_data['black'] == player_name, 'black_rating_diff'].sum()
        elo_diff = white_elo_diff + black_elo_diff
        
        # Number of wins (white)
        num_wins_white = ((player_data['white'] == player_name) & (player_data['winner'] == player_name)).sum()

        # Number of losses (white)
        num_losses_white = ((player_data['white'] == player_name) & (player_data['loser'] == player_name)).sum()

        # Number of wins (black)
        num_wins_black = ((player_data['black'] == player_name) & (player_data['winner'] == player_name)).sum()

        # Number of losses (black)
        num_losses_black = ((player_data['black'] == player_name) & (player_data['loser'] == player_name)).sum()

        # Number of draws (white)
        num_draws_white = ((player_data['white'] == player_name) & (player_data['result'] == '1/2-1/2')).sum()

        # Number of draws (black)
        num_draws_black = ((player_data['black'] == player_name) & (player_data['result'] == '1/2-1/2')).sum()

        # Medium elo among player's games
        medium_elo = player_data.apply(
            lambda row: row['white_elo'] if row['white'] == player_name else row['black_elo'], axis=1
        ).mean()

        # Add player statistics to the list
        player_stats.append({
            'Player': player_name,
            'Number of Played Games': num_games,
            'Total Elo Gain/Loss': elo_diff,
            'Number of Wins (White)': num_wins_white,
            'Number of Losses (White)': num_losses_white,
            'Number of Draws (White)': num_draws_white,
            'Number of Wins (Black)': num_wins_black,
            'Number of Losses (Black)': num_losses_black,
            'Number of Draws (Black)': num_draws_black,
            'Number of Wins': num_wins_white + num_wins_black,
            'Number of Losses': num_losses_white + num_losses_black,
            'Number of Draws': num_draws_white + num_draws_black,
            'win/loss ratio': (num_wins_white + num_wins_black) / (num_losses_white + num_losses_black),
            'Medium Elo': medium_elo
        })

    # Create the player statistics DataFrame
    player_stats_df = pd.DataFrame(player_stats)

    # Write the player statistics to a new Excel file
    player_stats_df.to_excel('player_stats.xlsx', index=False)


# Example usage
analyze_player_data('game_info.xlsx')
