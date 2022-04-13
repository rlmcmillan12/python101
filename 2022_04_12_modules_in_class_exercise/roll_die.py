from random import randint


def roll_die():
    sides = int(input("How many sides does the die have?: "))
    roll = randint(1, sides)
    print("\nYour dice roll is: " + str(roll))

