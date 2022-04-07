# Write a script that asks for a day of the week.
# If the day is a business day, print 'go to work!'.
# If the day is a weekend day, print 'sleep in!'.
# If whatever the user entered is not a day, print 'enter a valid day'.

day_of_the_week = input("What day of the week is it?: ")

day_lower = day_of_the_week.lower()

if day_lower == "saturday" or day_lower == "sunday":
    print("Sleep in!!!")

if (
    day_lower == "monday"
    or day_lower == "tuesday"
    or day_lower == "wednesday"
    or day_lower == "thursday"
    or day_lower == "friday"
):
    print("Go to work!")

else:
    print("Enter a valid day")


# Write a script that asks the user for a password.
# If the user enters the correct word (pick one yourself) then print 'Welcome!',
# otherwise print 'Try Again!'

# username = input("Please enter your username: ")
# password = input("\nPlease enter your password: ")

# if username == "rlmcmillan12" and password == "Piccard is better":
#     print("Welcome to the Thunderdome!")

# else:
#     print("Try again!")
