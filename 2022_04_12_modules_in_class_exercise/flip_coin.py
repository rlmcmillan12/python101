from random import randint

def flip_coin():
    flip = randint(0,1)
    if flip == 1:
        print("It's a heads!")
    else:
        print("It's a tails!")