from unicodedata import name


phonebook = []

while True:

    print(
        """
DigitalCrafts WebDev Phone Book
===============================
1) Look up entry
2) Set an Entry
3) Delete an entry
4) List all entries
5) Quit
6) Look up an entry by phone number """
    )

    user_input = input("Pick an action 1-5: ")

    if user_input == "5":
        break
    if user_input == "1":
        look_up_name = input("Which entry would you like to find?: ")
        for contact in phonebook:
            if look_up_name == contact["Name"]:
                print(
                    "Name: " + contact["Name"] + "\nNumber: " + contact["Phone Number"]
                )

    if user_input == "2":
        enter_name = input("What is the name for the new entry?: ")
        enter_number = input("What is the number of the new entry?: ")
        new_entry = {"Name": enter_name, "Phone Number": enter_number}
        phonebook.append(new_entry)
        print(
            "Name: "
            + new_entry["Name"]
            + "\nPhone Number: "
            + new_entry["Phone Number"]
            + "\nEntry stored for "
            + new_entry["Name"]
        )
    if user_input == "3":
        print(phonebook)
        del_name = input("What is the entry you would like to delete?: ")
        for contact in phonebook:
            if del_name == contact["Name"]:
                index = phonebook.index(contact)
                print("\nDeleted")
                del phonebook[index]

    if user_input == "4":
        for contact in phonebook:
            print(
                "Name: "
                + contact["Name"]
                + "\nPhone Number: "
                + contact["Phone Number"]
            )
    if user_input == "6":
        for contact in phonebook:
            if look_up_name == contact["Name"]:
                print(
                    "Name: " + contact["Name"] + "\nNumber: " + contact["Phone Number"]
                )


phonebook = [
    {"name": "ryan", "phone number": "2346236"},
    {"name": "maggie", "phone number": "2345234"},
]
