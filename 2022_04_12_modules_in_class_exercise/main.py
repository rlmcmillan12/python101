from flip_coin import flip_coin
from roll_die import roll_die
from roll_many_dice import roll_many_dice
from random import choice


players = []


def main():
    while True:

        player_name = input(
            "Enter a player name,\nif all players entered type 'done': "
        )

        if player_name == "done":
            break
        else:
            players.append(player_name)
            print(players)

    while True:
        user_choice = input(
            f"""Chose an option
    1 - Flip a coin
    2 - Roll a die
    3 - Roll multiple dice
    4 - Pick a random player
    5 - Round helper
    q - exit: """
        )

        if user_choice == "1":
            flip_coin()
        elif user_choice == "2":
            roll_die()
        elif user_choice == "3":
            roll_many_dice()
        elif user_choice == "4":
            print("\n   THE CHOSEN ONE IS: " + choice(players) + "\n")
        # elif user_choice == "5":
        #     enter = input("Hit the enter key to pick a player: ")
            # if enter == "":
            #     for i in players:
        elif user_choice == "q":
            break
        else:
            print("Pick a valid input")


main()
