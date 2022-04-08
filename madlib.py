# Ask the user for three inputs (a noun, a present-tense verb, and a name)
# and store the values in appropriately named variables.

# Next, write a function called madlib that takes three parameters:
# a noun, a present-tense verb, and a name.
# The function should print a story that uses these parameters to the console.

# Lastly, pass the three user inputs to the madlib function,
# so that when you execute the script, it asks the user for input,
# and then prints out the madlib story.

noun = input("\nPlease enter a noun: ")
verb = input("\nPlease enter a present-tense verb: ")
name = input("\nPlease enter a name: ")


def madlib(noun, verb, name):
    print(
        "\nOnce upon a time there was a daring and cunning space explorer named "
        + name.lower().capitalize()
        + ".\nWhile out in space he likes to "
        + verb.lower()
        + " in the deepest darkest "
        + noun
        + ".\n"
    )


madlib(noun, verb, name)
