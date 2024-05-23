# lib/cli.py

from helpers import (
    exit_program,
    list_foods,
    list_pantries,
    choose_pantry,
    add_pantry,
    update_owner,
    add_food,
    remove_food,
    select_food,
    update_food,
    category_list,
    delete_pantry,
    list_all_foods
)

def prLightPurple(str): print("\033[94m {}\033[00m" .format(str))
def prGreen(str): print("\033[92m {}\033[00m" .format(str))
def prRed(str): print("\033[91m {}\033[00m" .format(str))

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            while True:
                sub_1()
        elif choice == "2":
            list_all_foods()
        elif choice == "3":
            exit_program()
        else:
            prRed("Invalid choice.")

def sub_1():
    list_pantries()
    pantry_menu()
    choice = input("> ")
    if choice == "1":
        list_pantries()
        pantry = choose_pantry()
        if pantry:
            while True:
                sub_2(pantry)
    elif choice == "2":
        add_pantry()
    elif choice == "3":
        delete_pantry()
    elif choice == "4":
        prGreen(" \nReturning to main menu.")
        main()
    else:
        prRed("Invalid choice.")

def sub_2(pantry):
    prLightPurple(f" \n--- {pantry.owner}'s Pantry ---")
    list_foods(pantry.id)
    owner_menu()
    choice = input("> ")
    if choice == "1":
        update_owner(pantry.id)
    elif choice == "2":
        delete_pantry(pantry.id)
        sub_1()
    elif choice == "3":
        add_food(pantry.id)
    elif choice == "4":
        remove_food(pantry.id)
    elif choice == "5":
        selected_food = select_food(pantry.id)
        if selected_food:
            while True:
                sub_3(pantry, selected_food)
    elif choice == "6":
        while True:
            sub_4(pantry)
    elif choice == "7":
        sub_1()
    else:
        prRed("Invalid choice.")

def sub_3(pantry, selected_food):
    prLightPurple(f" \n--- Updating {selected_food.name} ---")
    print(f"Stored Quantity: {selected_food.qty} \nCategory: {selected_food.type}")
    food_update_menu(pantry.owner)
    choice = input("> ")
    if choice == "1" or choice == "2" or choice == "3":
        update_food(selected_food, choice)
    elif choice == "4":
        sub_2(pantry)
    else:
        prRed("Invalid choice.")

def sub_4(pantry):
    category_list(pantry.id)
    category_menu(pantry.owner)
    choice = input("> ")
    if choice == "1":
        sub_4(pantry)
    elif choice == "2":
        sub_2(pantry)
    else: 
        prRed("Invalid choice.")


def menu():
    prLightPurple("\n\
██████╗░░█████╗░███╗░░██╗████████╗██████╗░██╗░░░██╗  ░█████╗░██╗░░░░░██╗\n\
██╔══██╗██╔══██╗████╗░██║╚══██╔══╝██╔══██╗╚██╗░██╔╝  ██╔══██╗██║░░░░░██║\n\
██████╔╝███████║██╔██╗██║░░░██║░░░██████╔╝░╚████╔╝░  ██║░░╚═╝██║░░░░░██║\n\
██╔═══╝░██╔══██║██║╚████║░░░██║░░░██╔══██╗░░╚██╔╝░░  ██║░░██╗██║░░░░░██║\n\
██║░░░░░██║░░██║██║░╚███║░░░██║░░░██║░░██║░░░██║░░░  ╚█████╔╝███████╗██║\n\
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░  ░╚════╝░╚══════╝╚═╝")
    print(" \nPlease select an option:")
    print("1 - List pantry owners")
    print("2 - List foods")
    print("3 - Exit")

# Sub Menu 1
def pantry_menu():
    print(" \nPlease select an option:")
    print("1 - Choose an existing pantry")
    print("2 - Add a pantry")
    print("3 - Delete a pantry")
    print("4 - Return to main menu")

# Sub Menu 2
def owner_menu():
    print(" \nPlease select an option:")
    print("1 - Rename pantry")
    print("2 - Delete this pantry")
    print("3 - Add new food")
    print("4 - Remove food")
    print("5 - Update food")
    print("6 - List foods from category")
    print("7 - Return to pantry menu")

# Sub Menu 3
def food_update_menu(name):
    print(" \nPlease select an option:")
    print("1 - Update name")
    print("2 - Update quantity")
    print("3 - Update category")
    print(f"4 - Return to {name}'s pantry menu")

# Sub Menu 4
def category_menu(name):
    print(" \nPlease select an option:")
    print("1 - List foods from another category")
    print(f"2 - Return to {name}'s pantry menu")

if __name__ == "__main__":
    main()
