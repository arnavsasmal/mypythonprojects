#This code asks the user for a name of a game and checks the dictionary for the game and prints the description as an output
#It also gives the user an option to add games to the dictionary


games = {"Fortnite": "A cartoonish Battle Royale game",
          "CSGO": "A fast paced First Person Shooter",
          "PUBG": "The original, more realistic Battle Royale",
          "GTA5": "A open world game in which the player is free to do anything",
          "Superhot": "A fighting game in which time only moves when the player moves",
          "FIFA": "A realistic football game with accurate graphics",
          "F12018": "A realistic Formula One Racing game made by Codemasters"}

while True:
    print("What game would you like to know info about?")
    game_request = input()

    if game_request == "quit":
        break

    if game_request in games:
        game_descrpition = games.get(game_request)
        print(game_descrpition)

    else:
        print("We dont have that game in our records")
        print("Would you like to add it to our records?")
        game_record_add = input()
        if game_record_add == "no":
            continue
        else:
            print("What is the name of the game that you want to add?")
            game_record_add_name = input()
            print("What is the description of this game?")
            game_record_add_desc = input()
            games[game_record_add_name] = game_record_add_desc
