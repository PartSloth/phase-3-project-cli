# lib/cli.py

from helpers import (
    exit_program,
    list_elements
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_elements()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List elements")


if __name__ == "__main__":
    main()
