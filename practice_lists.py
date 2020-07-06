players = []

add_player = input("Would you like to add a player to the list? (Y / N) ")

while add_player.lower() == "y":
    player = input("Please provide player name: ")
    players.append(player)
    add_player = input("Would you like to add another player? (Y / N) ")

print("\nThere are currently {} players on the team.".format(len(players)))

for player in players:
    player_number = players.index(player) + 1
    print("Player {}: {}".format(player_number, player))

goalie = input("\nPlease select a goalkeeper: ")

print("{} is the goalie!".format(players[(int(goalie) - 1)]))
