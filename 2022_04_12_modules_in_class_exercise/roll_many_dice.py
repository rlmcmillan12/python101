from random import randint


def roll_many_dice():
    number_dice = int(input("How many dice would you like to roll?: "))
    sides = int(input("How man side do your dice have?: "))

    roll_number = 1
    total = 0

    while roll_number <= number_dice:
        roll = randint(1, sides)
        total += roll
        roll_number += 1
    print(total)

