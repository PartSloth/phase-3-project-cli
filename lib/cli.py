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

def create_main_menu():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "1":
            while True:
                create_pantry_menu()
        elif choice == "2":
            list_all_foods()
        elif choice == "3":
            exit_program()
        else:
            prRed("Invalid choice.")
            create_main_menu()

def create_pantry_menu():
    list_pantries()
    pantry_menu_list()
    choice = input("> ")
    if choice == "1":
        pantry = choose_pantry()
        if pantry:
            while True:
                create_owner_menu(pantry)
    elif choice == "2":
        add_pantry()
    elif choice == "3":
        delete_pantry()
    elif choice == "4":
        prGreen(" \nReturning to main menu.")
        create_main_menu()
    else:
        prRed("Invalid choice.")
        create_pantry_menu()

def create_owner_menu(pantry):
    prLightPurple(f" \n--- {pantry.owner}'s Pantry ---")
    list_foods(pantry)
    owner_menu_list()
    choice = input("> ")
    if choice == "1":
        update_owner(pantry)
    elif choice == "2":
        delete_pantry(pantry)
        create_pantry_menu()
    elif choice == "3":
        add_food(pantry)
    elif choice == "4":
        remove_food(pantry)
    elif choice == "5":
        selected_food = select_food(pantry)
        if selected_food:
            while True:
                create_food_update_menu(pantry, selected_food)
    elif choice == "6":
        while True:
            create_category_menu(pantry)
    elif choice == "7":
        create_pantry_menu()
    else:
        prRed("Invalid choice.")
        create_owner_menu(pantry)

def create_food_update_menu(pantry, selected_food):
    prLightPurple(f" \n--- Updating {selected_food.name} ---")
    print(f"Stored Quantity: {selected_food.qty} \nCategory: {selected_food.type}")
    food_update_menu_list(pantry.owner)
    choice = input("> ")
    if choice == "1" or choice == "2" or choice == "3":
        update_food(selected_food, choice)
    elif choice == "4":
        create_owner_menu(pantry)
    else:
        prRed("Invalid choice.")
        create_food_update_menu(pantry, selected_food)

def create_category_menu(pantry):
    category_list(pantry)
    category_menu_list(pantry.owner)
    choice = input("> ")
    if choice == "1":
        create_category_menu(pantry)
    elif choice == "2":
        create_owner_menu(pantry)
    else: 
        prRed("Invalid choice.")
        create_category_menu(pantry)


def main_menu():
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
def pantry_menu_list():
    print(" \nPlease select an option:")
    print("1 - Choose an existing pantry")
    print("2 - Add a pantry")
    print("3 - Delete a pantry")
    print("4 - Return to main menu")

# Sub Menu 2
def owner_menu_list():
    print(" \nPlease select an option:")
    print("1 - Rename pantry")
    print("2 - Delete this pantry")
    print("3 - Add new food")
    print("4 - Remove food")
    print("5 - Update food")
    print("6 - List foods from category")
    print("7 - Return to pantry menu")

# Sub Menu 3
def food_update_menu_list(name):
    print(" \nPlease select an option:")
    print("1 - Update name")
    print("2 - Update quantity")
    print("3 - Update category")
    print(f"4 - Return to {name}'s pantry menu")

# Sub Menu 4
def category_menu_list(name):
    print(" \nPlease select an option:")
    print("1 - List foods from another category")
    print(f"2 - Return to {name}'s pantry menu")

if __name__ == "__main__":
    create_main_menu()
