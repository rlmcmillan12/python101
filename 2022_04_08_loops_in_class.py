import random


# Write a script that asks the user for a number,
# then prints all of the numbers up to and including that number:

# user_input = int(input("Please enter a number: "))
# count = 0

# while count < user_input:
#     print(count + 1)
#     count += 1


# Write a script that asks the user for a two numbers,
# then prints all of the numbers including and between both numbers

# user_input_1 = int(input("Please enter a number: "))
# user_input_2 = int(input("Please enter another number: "))

# if user_input_1 < user_input_2:
#     count = user_input_1
#     while count <= user_input_2:
#         print(count)
#         count += 1

# elif user_input_2 < user_input_1:
#     count = user_input_2
#     while count <= user_input_1:
#         print(count)
#         count += 1

# elif user_input_1 == user_input_2:
#     print(user_input_1)

# print(" THANKS FOR THE NUMBERS! HAVE A WONDERFUL DAY!")

# Write a script that asks the user for a two numbers,
# then prints all of the odd numbers including and between both numbers

# user_input_1 = int(input("Please enter a number: "))
# user_input_2 = int(input("Please enter another number: "))

# if user_input_1 < user_input_2:
#     while user_input_1 <= user_input_2:
#         if user_input_1 % 2 == 1:
#     user_input_1 += 1

# elif user_input_2 < user_input_1:
#     while user_input_2 <= user_input_1:
#         if user_input_2 % 2 == 1:
#             print(user_input_2)
#         user_input_2 += 1

# elif user_input_1 == user_input_2 and user_input_1 % 2 == 1:
#     print(user_input_1)

# if user_input_1 == user_input_2 and user_input_1 % 2 == 0:
#     print("You have no odd numbers")

# print(" THANKS FOR THE NUMBERS! HAVE A WONDERFUL DAY!")


# Write a script that asks the user for a number.
# Print all the numbers between 0 and that number except:

# If the number is divisible by 3, print fizz
# If the number is divisible by 5, print buzz
# if the number is divisible by both 3 and 5, print fizzbuzz

# user_input = int(input("please enter a number: "))
# count = 0

# while count - 1 < user_input:
#     if (count + 1) % 3 == 0 and (count + 1) % 5 == 0:
#         print("fizzbuzz")
#     elif (count + 1) % 3 == 0:
#         print("fizz")
#     elif (count + 1) % 5 == 0:
#         print("buzz")

#     print(count)
#     count += 1

# print(" THANKS FOR THE NUMBERS! HAVE A WONDERFUL DAY!")


# Write a grandma script that interacts with the user.

# Whatever you say to grandma (whatever you type in), she should respond with:
# HUH?! SPEAK UP, SONNY!
# However, if you shout it (type in all capitals), she can hear you (or at least she thinks so)
# and yells back NO, NOT SINCE 1938!
# You can’t stop talking to grandma until you shout BYE

# user_input = input("What would you like to say to grandma?: ")

# while user_input != "BYE":

#     if user_input == user_input.upper():
#         print("NO, NOT SINCE 1938!")

# while user_input != user_input.upper():
#         print("HUH?! SPEAK UP, SONNY!")
#         user_input = input("What would you like to say to grandma?: ")


# Print a 5x5 square of * characters.

# stars = "*****"
# for num in range(5):
#     print(stars)


# Print a Triangle
# Ask the user for a height and print a pyramid that is that many rows tall

# height = int(input("How many rows high would you like your pyramid?: "))

# for i in range(0, height):
#     spaces = height - 1 - i
#     stars = i * 2 + 1
#     print(" " * spaces + "*" * stars)


# Write a script that will print the multiplication table for numbers from 1 up to 10.


# for multiplier in range(1, 11):
#     for multiplicand in range(1, 11):
#         product = multiplier * multiplicand
#         print(f"{multiplier} * {multiplicand} = {product}")


# Write a script that asks the user for a two numbers, height and width,
# then prints a box according to that size

# height = int(input("How high would you like your box?: "))
# width = int(input("How wide would you like your box?: "))

# for i in range(0, height):
#     if i == 0 or i == height - 1:
#         print("*" * width)
#     else:
#         print("*" + " " * (width - 2) + "*")


# Coin Flipper
# Write a script that tells the user they have 1 coin and asks them if they want another.
# Keep adding coins until they say 'no'.
# Flip each coin print the result for each (coins are 50/50 chance of heads vs tails).


# def coin_flip():
#     flip = random.randint(0, 1)
#     flip_count = 1
#     if flip == 0:
#         print(str(i + 1) + " Heads")
#         flip_count += 1
#     else:
#         print(str(i + 1) + " Tails")
#         flip_count += 1


# user_input_1 = input("Do you want to flip a coin?\nEnter yes or no: ")
# coin_count = 0

# if user_input_1.lower() == "yes":
#     coin_count += 1

# elif user_input_1.lower() == "no":
#     print("You don't have any coins to flip, Goodbye.")
#     exit()

# while True:
#     user_input_2 = input("Would you like to flip another?: ")

#     if user_input_2.lower() == "yes":
#         coin_count += 1
#         print(f"You have {coin_count} coins")

#     elif user_input_2.lower() == "no":
#         break

#     else:
#         print("Please enter yes or no.")
# for i in range(coin_count):
#     coin_flip()
