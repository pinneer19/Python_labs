from task2 import constants
from container import MyContainer


def get_command(container: MyContainer, command: str):
    command_input = command.split()[0]
    args = command.split()[1:]
    match command_input:
        case constants.HELP:
            if len(args) == 0:
                print(constants.HELP_ANSWER)
            else:
                print("'help' command requires zero arguments!")
        case constants.ADD:
            if len(args) == 0:
                print("'add' command requires > 0 arguments")
            else:
                container.add(args)
        case constants.REMOVE:
            if len(args) != 1:
                print("'remove' command requires 1 argument")
            else:
                container.remove(args[0])
        case constants.FIND:
            if len(args) == 0:
                print("'find' command requires > 0 arguments")
            else:
                container.find(args)
        case constants.LIST:
            if len(args) != 0:
                print("'list' command requires 0 arguments")
            else:
                container.list()
        case constants.GREP:
            if len(args) != 1:
                print("'grep' command requires 1 argument")
            else:
                container.grep(args)
        case constants.SAVE:
            if len(args) == 0:
                container.save()
            else:
                print("'save' command requires zero arguments!")
        case constants.LOAD:
            if len(args) == 0:
                container.load()
            else:
                print("'load' command requires zero arguments!")
        case constants.SWITCH:
            if len(args) != 1:
                print("'switch' command requires 1 string argument")
            else:
                container.switch(args[0])
        case _:
            print("Error occurred please check your command!")


def run_container(container: MyContainer):
    user = input("Enter username: ")
    container.switch(user)
    print("Write command(type 'help' to see available ones)")
    while True:
        command = input()
        if command.split()[0] == constants.EXIT:
            if len(command.split()[1:]) != 0:
                print("'exit' command requires 0 arguments")
            else:
                choice = input("Do you want to save your container(y - yes, n - no): ")
                while choice != 'y' and choice != 'n':
                    choice = input("Try again..\nDo you want to save your container(y - yes, n - no): ")
                if choice == 'y':
                    container.save()
                break
        else:
            get_command(container, command)
