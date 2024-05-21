# lib/helpers.py
from models.food import Food
from models.pantry import Pantry

# Need to change choosing method from typing names to numbered lists.

def prLightPurple(str): print("\033[94m {}\033[00m" .format(str))
def prGreen(str): print("\033[92m {}\033[00m" .format(str))
def prRed(str): print("\033[91m {}\033[00m" .format(str))

def exit_program():
    prLightPurple("Goodbye!")
    exit()

def list_pantries():
    pantries = Pantry.get_all()
    prLightPurple(" \n--- Pantries ---")
    if len(pantries) > 0:
        x = 0
        for pantry in pantries:
            print(f"{x}. {pantry.owner}")
            x += 1
    else:
        print("There are no pantries. Please add a pantry!")

def list_all_foods():
    foods = Food.get_all()
    pantries = Pantry.get_all()
    for pantry in pantries:
        prLightPurple(f" \n--- {pantry.owner}'s Pantry ---")
        for food in foods:
            if food.pantry_id == pantry.id:
                print(f'{food.name} ({food.qty}) - {food.type}')
    

def choose_pantry():
    prLightPurple(" \n--- Choosing Pantry ---")
    pantries = Pantry.get_all()
    choice = input("Enter the pantry number > ")
    if choice.isnumeric():
        choice = int(choice)
        if 0 <= choice <= len(pantries):
            name = pantries[choice].owner
            print(name)
            return Pantry.find_by_owner(name)
        else:
            prRed("Pantry does not exist.")
    else:
        prRed("Enter numbers only.")

def add_pantry():
    prLightPurple(" \n--- Adding Pantry ---")
    name = input("Enter the name of the pantry owner > ").strip().capitalize()
    try:
        while Pantry.find_by_owner(name):
            prRed("This person already has a pantry.")
            name = input("Please enter a new owner > ").strip().capitalize()
        pantry = Pantry.create(name)
        prGreen(f"Added: {pantry.owner}'s Pantry")
    except Exception as exc:
        prRed("Error creating pantry: ")
        prRed(exc)

def update_owner(pantry_id):
    prLightPurple(" \n--- Updating Pantry ---")
    if pantry := Pantry.find_by_id(pantry_id):
        try:
            name = input("Enter name of the pantry's new owner > ").strip().capitalize()
            while Pantry.find_by_owner(name):
                prRed("This person already has a pantry.")
                name = input("Enter name of the pantry's new owner > ").strip().capitalize()
            pantry.owner = name
            pantry.update()
            prGreen(f'Updated: {name}')
        except Exception as exc:
            prRed("Error updating pantry: ")
            prRed(exc)
    else:
        prRed(f"Pantry does not exist")

def list_foods(pantry_id):
    foods = Food.find_by_pantry(pantry_id)
    if len(foods) > 0:
        for food in foods:
            print(f"{food.name} ({food.qty})")  
    else:
        print("This pantry is empty.")

def add_food(pantry_id):
    prLightPurple(" \n--- Adding Food ---")
    name = input("Enter name of the food > ").capitalize()
    while Food.find_by_name(name):
        owner = Pantry.find_by_id(Food.find_by_name(name).pantry_id).owner
        prRed(f"This food already exists in {owner}'s pantry")
        name = input("Enter name of the food > ").capitalize()
    qty = input("Enter the qty of food > ")
    type = category_select()
    try: 
        food = Food.create(name, qty, type, pantry_id)
        prGreen(f"Added to {Pantry.find_by_id(pantry_id).owner}'s pantry: {food.name}")
    except Exception as exc:
        prRed("Error adding food: ")
        prRed(exc)

# Need to iterate through pantry's foods and remove before deleting the pantry instance.
def delete_pantry(pantry_id = None):
    if Pantry.get_all() == None:
        prRed("There are no pantries to delete.")
    elif pantry_id != None: 
        pantry = Pantry.find_by_id(pantry_id)
        pantry.delete()
    else:
        prLightPurple(" \n--- Deleting Pantry ---")
        pantries = Pantry.get_all()
        choice = input("Enter the pantry number > ")
        if choice.isnumeric():
            choice = int(choice)
            if 0 <= choice <= len(pantries):
                pantry = pantries[choice]
                pantry.delete()
            else:
                prRed("Pantry does not exist.")
        else:
            prRed("Enter numbers only.")
    

def category_select():
    type_dict = {"A": "Canned Goods",
                 "B": "Baking Staples",
                 "C": "Condiments",
                 "G": "Grains",
                 "M": "Misc",
                 "N": "Snacks",
                 "O": "Oils",
                 "P": "Pastas",
                 "S": "Spices"}
    key = input(
        " \nSelect the category of food. \n\
        A - Canned Goods \n\
        B - Baking Staples \n\
        C - Condiments \n\
        G - Grains \n\
        M - Misc \n\
        N - Snacks \n\
        O - Oils \n\
        P - Pastas \n\
        S - Spices \n\
        > ").strip().capitalize()
    while type_dict.get(key) == None:
        prRed(f"{key} is not an available selection.")
        key = input(
        " \nSelect the category of food. \n\
        A - Canned Goods \n\
        B - Baking Staples \n\
        C - Condiments \n\
        G - Grains \n\
        M - Misc \n\
        N - Snacks \n\
        O - Oils \n\
        P - Pastas \n\
        S - Spices \n\
        > ").strip().capitalize()
    type = type_dict[key]
    return type

def remove_food(pantry_id):
    max_input = len(Food.find_by_pantry(pantry_id))
    if max_input == 0:
        prRed("Pantry is empty. Please add food first!")
    else: 
        name = input("Which food do you want to remove > ").capitalize()
        food = Food.find_by_name(name)
        if food == None:
            prRed("This food does not exist in this pantry.")
        elif food.pantry_id == pantry_id:
            food.delete()
            prGreen(f"{name} has been removed from the pantry.")
        else:
            prRed("This food is not in this pantry.")

def select_food(pantry_id):
    max_input = len(Food.find_by_pantry(pantry_id))
    if max_input == 0:
        prRed("Pantry is empty. Please add food first!")
    else: 
        name = input("Which food do you want to update > ").capitalize()
        food = Food.find_by_name(name)
        if food == None:
            return None
        elif food.pantry_id == pantry_id:
            return food
        else:
            return None

def update_food(food, choice):
    try:
        if choice == "0":
            name = input("Enter new name > ")
            food.name = name
        elif choice == "1":
            qty = input("Enter new quantity > ")
            food.qty = qty
        elif choice == "2":
            type = category_select()
            food.type = type

        food.update()
        prGreen('Updated!')
    except Exception as exc:
        prRed("Error updating pantry: ")
        prRed(str(exc)) 

def category_list(pantry_id):
    type = category_select()
    list = Food.find_by_category(type, pantry_id)
    owner = Pantry.find_by_id(pantry_id).owner
    prLightPurple(f" \n---{owner}'s {type}---")
    if len(list) > 0:
        for food in list:
            print(food.name)
    else:
        prRed(f"{owner} doesn't have any {type.lower()}.")
