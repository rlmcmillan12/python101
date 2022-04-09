# Coin flip
# Write a function that will "flip a coin" and print the result.
# There should be a 50/50 chance of getting heads or tails.


import random


def coin_flip():
    flip = random.randint(0, 1)
    if flip == 0:
        print("Heads")
    else:
        print("Tails")


coin_flip()
