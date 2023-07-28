#Portfolio Project
#Roulette Application in Python
#By Vince Muller

import os #Module for clearing the terminal
from roulette_pkg.homepage import startgame, gamegraphic #Module with functions for game graphics and displays
from roulette_pkg.user import login, user #Module with classes and functions for new and existing users
from roulette_pkg.gameplay import gameplay #Module with functions for game play

useraccounts = {}

#Roulette game play loop
while True:
    player = []

    homepage_selection = startgame()

#Conditions for each of the 3 home page options
    #Create new player account
    if homepage_selection == "1":
        player = user()
        player = player.register()

        if player[0] in useraccounts:
            input("Username already exists")
            continue

        #Add new player to global dictionary along with associated attributes
        useraccounts[player[0]] = [player[1], int(player[2])]
        player = gameplay(player[0], int(player[2]))
        useraccounts[player[0]][1] = int(player[1])

    #Log in existing player
    elif homepage_selection == "2":
      player = login()

      if player[0] not in useraccounts or useraccounts[player[0]][0] != player[1]:
            input("Username or password is incorrect")
            continue
      else:
            gamegraphic()
            print("                     Welcome Back to Roulette!!!")
            input("                    Press Enter to Start Playing ")
            player = gameplay(player[0],int(useraccounts[player[0]][1])) #Pull existing player's attributes from global accounts dictionary
            useraccounts[player[0]][1] = player[1]

    #Exit game
    elif homepage_selection == "3":
        gamegraphic()
        print("                      Thank you for playing!!\n                             Gameover")
        break

    #Communicate invalid user inputs
    else:
        gamegraphic()
        input("                            Invalid Entry")
        continue
