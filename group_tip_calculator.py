# Write a function called group_tip_calculator that asks the user for the bill total,
# the tip percentage, and the number of people.
#
# Pass the total and percentage values to the percentage_plus function
# and then divide the result by the number of people in the group.
# Print the total including the tip as well as the cost per person.


def percentage_plus(total, tip_percentage):
    tip_ammt = total * (tip_percentage / 100)
    return total + tip_ammt


def group_tip_calculator():
    total = float(input("What is the total of the bill?: "))
    tip_percentage = int(input("What percent would you like to tip?: "))
    group_size = int(input("How many people are in your group?: "))
    individual_total = round(percentage_plus(total, tip_percentage) / group_size, 2)

    print(
        "\nYour total with the tip is $"
        + str(round(percentage_plus(total, tip_percentage), 2))
    )
    print("\nEach person will owe $" + str(individual_total))


group_tip_calculator()
