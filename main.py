print("********************************************")
print("*****                                  *****")
print("*****             WELCOME              *****")
print("*****            THANK YOU             *****")
print("*****      For Using My TODO App       *****")
print("*****           😊😊😊😊😊            *****")
print("*****                                  *****")
print("********************************************")


# get the todos text file contents and return each line as a list
def get_todos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos


# add a list of todos to wright to the todos.txt file
def wright_todos(todos):
    with open('todos.txt', 'w') as file:
        file.writelines(todos)


while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    break_commands = ['break', 'exit', 'end', 'kill', 'back']

    # add a todo item to the list
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        wright_todos(todos)

    # show all todo list items
    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}. {item}")

    # edit the todo list by item number
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter a new todo item: ")
            todos[number] = new_todo + '\n'

            wright_todos(todos)
        except ValueError:
            print("There was an error editing your item for item: " + number)
            continue

    #Complete a todo list item
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            wright_todos(todos)
        except ValueError:
            print("There was an error trying to delete item: " + number)
            continue
    elif user_action.startswith('exit'):
        exit()
    else:
        #Defalut error if not command matches
        print("There is no command for " + user_action)

print("BYE Thanks for using the app")


