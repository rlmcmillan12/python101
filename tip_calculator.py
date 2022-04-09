# Write a function called percentage_plus that takes a bill total and a tip percentage
# and returns (not prints) the total plus tip.
#
# Create a second function called tip_calculator that asks the user
# for the bill total and the tip percentage.
#
# Pass those values through to the tip_calculator function
# and then print the result in a nice format.


def percentage_plus(total, tip_percentage):
    tip_ammt = total * (tip_percentage / 100)
    return round(total + tip_ammt, 2)


def tip_calculator():
    total = float(input("What is the total of the bill?: "))
    tip_percentage = int(input("What percent would you like to tip?: "))
    print("Your total with the tip is " + str(percentage_plus(total, tip_percentage)))


tip_calculator()
