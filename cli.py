from methods import get_todos, write_todos
import time

time_now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is " + time_now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    a = user_action

    if a.startswith("add"):
        todo = a[4:]
        todos = get_todos()
        todos.append('\n')
        todos.append(todo)
        write_todos(todos)

    elif a.startswith('show'):
        todos = get_todos()

        new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(new_todos):
            row = f"{index + 1}-{item}"
            print(row)
    elif a.startswith('exit'):
        break
    elif a.startswith('edit'):
        try:
            todos = get_todos()

            num = int(a[5:])

            edited_todo = input("Enter an edited todo ")
            edited_todo = edited_todo + "\n"
            indexOftask = num - 1
            todos[indexOftask] = edited_todo
            print(todos[indexOftask])

            write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif a.startswith('complete'):
        try:
            todos = get_todos()

            completed_task_num = int(a[9:])
            removed_to_do = todos[(completed_task_num - 1)].strip('\n')
            todos.pop(completed_task_num - 1)

            write_todos(todos)
            message = f"ToDo {removed_to_do} was removed from the list"
            print(message)
        except IndexError:
            print("There is no task with that number.")
            continue
    else:
        print("Command entered is not valid")

print("Have a great day!")
