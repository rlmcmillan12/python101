# # Define two variables: firstname and lastname.

# first_name = 'Ryan'
# last_name = 'McMillan'


# # Assign some string values to the variables. You can use your own name or someone else's.
# # Use those two variables to print a greeting that uses the firstname and lastname variables in the output.

# # greeting generator
# greeting = ('Welcome to the workshop! ' + first_name + " " + last_name)
# # print(greeting)

# # Using the two variables you set earlier, generate a company email address that follows the pattern: "first initial, period, last name @ company domain".
# # Assign the result to a new variable called email and print the email to the console.

# # email generator
# email = ('Email: ' + first_name[0] + '.' +
#          last_name + '@mcmillancarpentry.com')
# # print(email.lower())

# # Using the firstname and lastname variables, generate a username to a new variable and print it to the console.
# # The username should follow this format: first three letters from firstname, underscore, five letters from lastname.

# # username generator
# username = ('Username ' + first_name[0:3] + "_" + last_name[0:5])
# # print(username.lower())

# # contact card generator
# # print(greeting)
# # print(email.lower())
# # print(username.lower())


# Working with functions

# inputs
first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
domain = "@mcmillancarpentry.com"
# Greeter


def greeter(first_name, last_name):
    print(f"Thank you and welcome to the woodshop, {first_name} {last_name}\n")

    # greeter(first_name, last_name)

    # Email generator


def email_generator(first_name, last_name, domain):
    print(f"Email: {first_name[0:1].lower()}.{last_name.lower()}@{domain}\n")

    # email_generator(first_name, last_name, domain)

    # Username generator


def username_generator(first_name, last_name):
    print(f"Username: {first_name[0:3].lower()}_{last_name[0:5].lower()}")

    # username_generator(first_name, last_name)

    # New user contact information


def new_user_contact_info(first_name, last_name, domain):
    greeter(first_name, last_name)
    email_generator(first_name, last_name, domain)
    username_generator(first_name, last_name)


new_user_contact_info(first_name, last_name, domain)
