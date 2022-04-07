# Write functions that accept two parameters, a and b, that print the result for each to the console

a = 5
b = 4

# add - print the result of a + b


def add(a, b):
    print(a + b)


# add(a, b)

# subtract - print the result of a - b


def subtract(a, b):
    print(a - b)


# subtract(a , b)

# multiply - print the result of a * b


def multiply(a, b):
    print(a * b)


# multiply(a, b)

# divide - print the result of a / b


def divide(a, b):
    print(a / b)


# divide(a, b)


# You need to calculate how many pancakes to make for a large conference breakfast.
# Write a function that accepts two parameters: number of guests, number of pancakes per guest.
# The calculation for the total number of pancakes should be 12% higher than the number of guests
# multiplied by the number of pancakes per guest, rounded up to the nearest whole number. Print the result to the console.

# guests = int(input("How many guests will be attending: "))
# ppg = int(input("How many pancakes will each guest be eating: "))


# def pancake_calculator(guests, ppg):
#     return round((guests * ppg) * 1.12)


# total = pancake_calculator(guests, ppg)

# print("You need to make " + str(total) + " pancakes")

# pancake_calculator(guests, ppg)


# Write a function called fahrenheitToCelsius that accepts a parameter for the temperature.
# Convert the temperature from celsius to fahrenheit and print the result.
# Do the opposite conversion in a function called celsiusToFahrenheit.

temp = int(input("\nWhat is the temperature?: "))
unit = input(
    "\nIs that in degrees Fahrenheit or Celsius? \nPlease enter f for Fahrenheit or c for Celsius: "
)


def cel_to_far(temp):
    fahrenheit = round(temp * 1.8 + 32)
    return fahrenheit


def far_to_cel(temp):
    celsius = round((temp - 32) * (5 / 9))
    return celsius


if unit == "c" or unit == "C":
    converted_temp = cel_to_far(temp)

if unit == "f" or unit == "F":
    converted_temp = far_to_cel(temp)
else:
    print("Please enter a valid input")
    exit()

print("The temperature is " + str(converted_temp) + " degrees " + unit.upper())


# Write a function that will convert the price of fuel in Sydney, NSW, Australia (which is in AUD$/liter)
# to USD$/gal. Make the function take a parameter for the AU price and another for the US price.
# Print the price in USD/gal.

# price = float(input("\nWhat is the current gas price per liter of gas in Sydney?: "))

# def gas_price_converter_(price):
#     converted_price = price / 1.34 *
