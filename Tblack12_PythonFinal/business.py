import db

# Function to retrieve players from the database
def get_players():
    return db.get_players()

# Function to add a new player to the database
def add_player(player):
    db.add_player(player)

# Function to retrieve games from the database
def get_games():
    return db.get_games()

# Function to add a new game to the database
def add_game(game):
    db.add_game(game)
