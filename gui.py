import time

import methods
import PySimpleGUI as sg

sg.theme('DarkGrey6')

clock = sg.Text("", key="time")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
list_box = sg.Listbox(values=methods.get_todos(),key='todos',
                      enable_events= True, size=[45,10])



window = sg.Window("Joey's To-Do App",
                   layout=[[clock],[[label], [input_box, add_button]],
                           [list_box,edit_button,complete_button],[exit_button]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read(timeout=10)
    window['time'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = methods.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            methods.write_todos(todos)
            window['todos'].update(values=todos)
        case sg.WIN_CLOSED:
            break
        case "Edit":
            try:
                edit_todo = values['todos'][0]
                new_todo = values['todo'] + "\n"
                todos = methods.get_todos()
                index = todos.index(edit_todo)
                todos[index] = new_todo
                methods.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica",21))

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Complete':
            try:
                completed_todo = values['todos'][0]
                todos = methods.get_todos()
                todos.remove(completed_todo)
                methods.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 21))

        case "Exit":
            break
window.close()

