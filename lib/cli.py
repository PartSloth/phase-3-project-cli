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
                            prLightPurple(f" \n--- {pantry.owner}'s Pantry ---")
                            list_foods(pantry.id)
                            owner_menu()
                            choice = input("> ")
                            if choice == "0":
                                update_owner(pantry.id)
                            elif choice == "1":
                                delete_pantry(pantry.id)
                                sub_menu_2 = False
                            elif choice == "2":
                                add_food(pantry.id)
                            elif choice == "3":
                                remove_food(pantry.id)
                            elif choice == "4":
                                selected_food = select_food(pantry.id)
                                if selected_food:
                                    # Sub Menu 3
                                    sub_menu_3 = True
                                    while sub_menu_3 == True:
                                        prLightPurple(f" \n--- Updating {selected_food.name} ---")
                                        print(f"Stored Quantity: {selected_food.qty} \nCategory: {selected_food.type}")
                                        food_update_menu(pantry.owner)
                                        choice = input("> ")
                                        if choice == "0" or choice == "1" or choice == "2":
                                            update_food(selected_food, choice)
                                        elif choice == "3":
                                            sub_menu_3 = False
                                        else:
                                            prRed("Invalid choice.")
                                else:
                                    prRed("This food does not exist in this pantry.")
                            elif choice == "5":
                                # Sub Menu 4
                                sub_menu_4 = True
                                while sub_menu_4 == True:
                                    category_list(pantry.id)
                                    category_menu(pantry.owner)
                                    choice = input("> ")
                                    if choice == "0":
                                        sub_menu_4 = False
                                        sub_menu_4 = True
                                    elif choice == "1":
                                        sub_menu_4 = False
                                    else: 
                                        prRed("Invalid choice.")
                            elif choice == "6":
                                sub_menu_2 = False
                            else:
                                prRed("Invalid choice.")
                elif choice == "1":
                    add_pantry()
                elif choice == "2":
                    delete_pantry()
                elif choice == "3":
                    prGreen(" \nReturning to main menu.")
                    sub_menu_1 = False
                else:
                    prRed("Invalid choice.")
        elif choice == "1":
            list_all_foods()
        elif choice == "2":
            exit_program()
        else:
            prRed("Invalid choice.")


def menu():
    print(" \nPlease select an option:")
    print("0 - List pantry owners")
    print("1 - List foods")
    print("2 - Exit")

# Sub Menu 1
def pantry_menu():
    print(" \nPlease select an option:")
    print("0 - Choose an existing pantry")
    print("1 - Add a pantry")
    print("2 - Delete a pantry")
    print("3 - Return to main menu")

# Sub Menu 2
def owner_menu():
    print(" \nPlease select an option:")
    print("0 - Rename pantry")
    print("1 - Delete this pantry")
    print("2 - Add new food")
    print("3 - Remove food")
    print("4 - Update food")
    print("5 - List foods from category")
    print("6 - Return to pantry menu")

# Sub Menu 3
def food_update_menu(name):
    print(" \nPlease select an option:")
    print("0 - Update name")
    print("1 - Update quantity")
    print("2 - Update category")
    print(f"3 - Return to {name}'s pantry menu")

# Sub Menu 4
def category_menu(name):
    print(" \nPlease select an option:")
    print("0 - List foods from another category")
    print(f"1 - Return to {name}'s pantry menu")

if __name__ == "__main__":
    main()
