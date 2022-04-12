## TO DO LIST:


def To_Do_List():
    to_do = {}
    while True:

        menu_selection = int(
            input(
                "Press 1 to add a task\nPress 2 to delete a task\nPress 3 to view all tasks\nPress 4 to quit\nEnter your option now: "
            )
        )

        if menu_selection == 4:
            break
        if menu_selection == 1:
            task = input("What is your task?: ")
            priority_select = int(
                input("Press 1 for high priority\nPress 2 for low priority: ")
            )
            if priority_select == 1:
                priority = "High"
                to_do[task] = priority
            else:
                priority = "Low"
                to_do[task] = priority
        elif menu_selection == 2:
            count = 0
            for i in to_do:
                count += 1
                print(f"{count} - {i} - {to_do[i]}")
            del_task = input("Which task would you like removed?: ")
            del to_do[del_task]

        elif menu_selection == 3:
            count = 0
            for i in to_do:
                count += 1
                print(str(count) + " - " + str(i) + " - " + to_do[i])


# delete, task, view all tasks, quit
# assign priority to each task
# print high to low priority


To_Do_List()
