# lib/cli.py

from helpers import (
    exit_program,
    list_foods,
    list_pantries,
    choose_pantry,
    add_pantry,
    update_owner,
    add_food
)


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
                        print("Pantry does not exist.")
                    else:
                        # Sub Menu 2
                        sub_menu_2 = True
                        while sub_menu_2 == True:
                            print(f"---{pantry.owner}'s Pantry---")
                            list_foods(pantry.id)
                            owner_menu()
                            choice = input("> ")
                            if choice == "0":
                                update_owner(pantry.id)
                            elif choice == "1":
                                add_food(pantry.id)
                            elif choice == "2":
                                pass
                            elif choice == "3":
                                sub_menu_2 = False
                            else:
                                print("Invalid choice.")
                elif choice == "1":
                    add_pantry()
                elif choice == "2":
                    print("Returning to main menu.")
                    sub_menu_1 = False
                else:
                    print("Invalid choice.")
        elif choice == "1":
            exit_program()
        else:
            print("Invalid choice.")


def menu():
    print("Please select an option:")
    print("0 - List Pantry Owners")
    print("1 - Exit")

# Sub Menu 1
def pantry_menu():
    print("Please select an option:")
    print("0 - Choose an existing pantry")
    print("1 - Add a pantry")
    print("2 - Return to main menu")

# Sub Menu 2
def owner_menu():
    print("Please select an option:")
    print("0 - Rename")
    print("1 - Add Food")
    print("2 - Remove Food")
    print("3 - Return to pantry menu")

if __name__ == "__main__":
    main()
