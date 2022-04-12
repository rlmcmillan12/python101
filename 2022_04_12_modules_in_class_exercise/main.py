def main():
    user_choice = input(
        f"""Chose an option
    1 - Flip a coin
    2 - Roll a die
    q - exit: """
    )

    if user_choice == "1":
        print("FLIP COIN")
    elif user_choice == "2":
        print("ROLL DIE")
