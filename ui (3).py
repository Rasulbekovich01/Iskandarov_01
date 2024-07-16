import service
from colorama import Fore

from utils import Response
from form import UserRegisterForm


def print_response(response: Response):
    color = Fore.GREEN if response.status_code == 200 else Fore.RED
    print(color + response.data + Fore.RESET)


def login_page():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    response = service.login(username, password)
    print_response(response)


def register_page():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    form = UserRegisterForm(username, password)
    response = service.register(form)
    print_response(response)


def logout_page():
    response = service.logout()
    print_response(response)


def add_todo():
    name = input('Enter name: ')
    description = input('Enter description: ')
    response = service.todo_add(name, description)
    print_response(response)


def update_todo():
    todo_id = input('Enter id: ')
    name = input('Enter new name: ')
    description = input('Enter new description: ')
    response = service.todo_update(todo_id, name, description)
    print_response(response)

def delete_todo():
    todo_id = input('Enter the ID : ')
    response = service.todo_delete(todo_id)
    print_response(response)

def block_user():
    username = input('Enter the username: ')
    response = service.block_user(username)
    print_response(response)

while True:

    choice = input('enter your choice : ')
    if choice == '1':
        login_page()
    elif choice == '2':
        register_page()
    elif choice == '3':
        logout_page()
    elif choice == '4':
        add_todo()

    elif choice == 'q':
        break
