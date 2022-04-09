# Coin flip
# Write a function that will "flip a coin" and print the result.
# There should be a 50/50 chance of getting heads or tails.


import random


# def coin_flip():
#     flip = random.randint(0, 1)
#     if flip == 0:
#         print("Heads")
#     else:
#         print("Tails")


# while True:
#     coin_flip()


# Even Odd
# Write a function that when given a number as an input will return true
# if the number is odd and false if the number is even.

# Write a script that asks the user for a number.
# Pass the number to the function and then print a message to the
# console that informs the user if the number was even or odd


# def even_odd(choice):
#     if (choice % 2) == 0:
#         print("It's even")
#     else:
#         print("It's odd")


# choice = int(input("Enter a number: "))
# even_odd(choice)


# Dice Roller
# Write a function that takes two numbers as arguments,
# then returns a random whole number between those two numbers.

# Write a script that tells the user that we are going to roll the
# dice but we need to know how many sides they have.
# Ask them for a number between 2 and 20.
# Pass the number 1 and the number from the user to the function,
# then print a message that shows the result


def dice_roller(num_1, num_2):

    if num_1 < num_2:
        roll = random.randint(num_1, num_2)
        print(roll)
    elif num_1 > num_2:
        roll = random.randint(num_2, num_1)
        print(roll)


num_1 = int(input("Pick a number:"))
num_2 = int(input("Enter another number: "))

dice_roller(num_1, num_2)
