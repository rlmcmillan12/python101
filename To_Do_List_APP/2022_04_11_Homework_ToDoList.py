## TO DO LIST:


# def print_to_do(to_do):
#     for i in to_do:
#         print(f'{to_do.index(i + 1)} - {i["task"]} - {i["priority"]} ')


# def To_Do_List(to_do):
#     while True:

#         menu_selection = input(
#             "Press 1 to add a task\nPress 2 to delete a task\nPress 3 to view all tasks\nPress 4 to quit\nEnter your option now: "
#         )

#         if menu_selection == "4":
#             break
#         if menu_selection == "1":
#             task = input("What is your task?: ")
#             priority_select = input(
#                 "Press 1 for high priority\nPress 2 for medium priority\nPress 3 for low: "
#             )
#             if priority_select == "1":
#                 priority = "High"
#             elif priority_select == "2":
#                 priority = "Medium"
#             else:
#                 priority = "Low"
#             current_task = {"task": task, "priority": priority}
#             to_do.append(current_task)
#         print_to_do(to_do)

# elif menu_selection == "2":
#     count = 0
#     for i in to_do:
#         count += 1
#         print(f"{count} - {i} - {to_do[i]}")
#     del_task = input("Which task would you like removed?: ")
#     del to_do[del_task]

# elif menu_selection == 3:
#     count = 0
#     for i in to_do:
#         count += 1
#         print(str(count) + " - " + str(i) + " - " + to_do[i])
# else:
#     print("\nPlease enter a valid entry")


# to_do = []
# To_Do_List(to_do)
