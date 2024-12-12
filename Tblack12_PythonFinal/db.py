import csv

# Define the filenames for player and game data
PLAYER_FILE = "players.csv"
GAME_FILE = "games.csv"

# Retrieve player data from the CSV file and return it 
def get_players():
    players = []
    with open(PLAYER_FILE, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            players.append(row)
    return players

# Append a new player's data to the CSV file
def add_player(player):
    fieldnames = ["id", "first_name", "last_name", "position"]
    with open(PLAYER_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(player)

# Retrieve game data from the CSV file and return it 
def get_games():
    games = []
    with open(GAME_FILE, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            games.append(row)
    return games

# Append a new game's data to the CSV file
def add_game(game):
    fieldnames = ["ID", "Date", "Opponent", "Result"]
    with open(GAME_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(game)

