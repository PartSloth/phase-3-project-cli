# lib/cli.py

from helpers import (
    exit_program,
    list_foods,
    list_pantries,
    choose_pantry,
    add_pantry,
    update_owner,
    add_food,
    remove_food
)

def prLightPurple(str): print("\033[94m {}\033[00m" .format(str))
def prGreen(str): print("\033[92m {}\033[00m" .format(str))
def prRed(str): print("\033[91m {}\033[00m" .format(str))

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            # Sub Menu 1
            sub_menu_1 = True
            while sub_menu_1 == True:
                list_pantries()
                pantry_menu()
                choice = input("> ")
                if choice == "0":
                    list_pantries()
                    pantry = choose_pantry()
                    if pantry == None:
                        prRed("Pantry does not exist.")
                    else:
                        # Sub Menu 2
                        sub_menu_2 = True
                        while sub_menu_2 == True:
                            prLightPurple(f" \n---{pantry.owner}'s Pantry---")
                            list_foods(pantry.id)
                            owner_menu()
                            choice = input("> ")
                            if choice == "0":
                                update_owner(pantry.id)
                            elif choice == "1":
                                add_food(pantry.id)
                            elif choice == "2":
                                remove_food(pantry.id)
                            elif choice == "3":
                                pass
                            elif choice == "4":
                                sub_menu_2 = False
                            else:
                                prRed("Invalid choice.")
                elif choice == "1":
                    add_pantry()
                elif choice == "2":
                    prGreen(" \nReturning to main menu.")
                    sub_menu_1 = False
                else:
                    prRed("Invalid choice.")
        elif choice == "1":
            exit_program()
        else:
            prRed("Invalid choice.")


def menu():
    print(" \nPlease select an option:")
    print("0 - List Pantry Owners")
    print("1 - Exit")

# Sub Menu 1
def pantry_menu():
    print(" \nPlease select an option:")
    print("0 - Choose an existing pantry")
    print("1 - Add a pantry")
    print("2 - Return to main menu")

# Sub Menu 2
def owner_menu():
    print(" \nPlease select an option:")
    print("0 - Rename")
    print("1 - Add New Food")
    print("2 - Remove Food")
    print("3 - Update Food")
    print("4 - Return to pantry menu")

if __name__ == "__main__":
    main()
