
"""
To install, type the following command on the python terminal:
pip install pgn2data
"""
from converter.pgn_data import PGNData
pgn_data = PGNData("lichess_tournament_2023.04.15_spring23_2023-spring-marathon.pgn")
pgn_data.export()