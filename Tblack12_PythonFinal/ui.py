# Import modules
from datetime import datetime
import business

# displaying different parts of the menu
def display_menu():
    print("MENU OPTIONS")
    print("1 – Display Roster")
    print("2 – Display Schedule")
    print("3 – Add Player")
    print("4 – Add Game")
    print("5 – Exit program")
    print()

def display_roster():
    players = business.get_players()
    if players:
        print("ROSTER")
        print("ID  | First Name | Last Name  | Position")
        print("-" * 40)
        for player in players:
            print(f"{player['id']:3} | {player['first_name']:10} | {player['last_name']:10} | {player['position']:8}")
    else:
        print("No players in the roster.")

def display_schedule():
    print("Game Schedule:")
    print("=" * 40)
    print("ID  | Date      | Opponent  | Result")
    print("-" * 40)
    games = business.get_games()
    for game in games:
        if 'ID' in game:  # Corrected key name to match the CSV header
            print(f"{game['ID']:3} | {game['Date']:10} | {game['Opponent']:10} | {game['Result']:8}")
        else:
            print("Game ID not found in the database.")
    print()

def add_player():
    first_name = input("Enter player's first name: ")
    last_name = input("Enter player's last name: ")
    position = input("Enter player's position: ")
    player = {'first_name': first_name, 'last_name': last_name, 'position': position}
    business.add_player(player)
    print("Player added successfully!")

def add_game():
    date = input("Enter game date (MM-DD-YYYY): ")
    opponent = input("Enter opponent: ")
    result = input("Enter game result (Win/Loss/Tie): ")
    game = {'Date': date, 'Opponent': opponent, 'Result': result}
    business.add_game(game)
    print("Game added successfully!")

# Define main function
def main():
    while True:
        display_menu()
        try:
            option = int(input("Menu option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if option == 1:
            display_roster()
        elif option == 2:
            display_schedule()
        elif option == 3:
            add_player()
        elif option == 4:
            add_game()
        elif option == 5:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid menu option.")

# Check if the script is being run directly
if __name__ == "__main__":
    main()
