# lib/helpers.py
from models.food import Food
from models.pantry import Pantry

def prLightPurple(str): print("\033[94m {}\033[00m" .format(str))
def prGreen(str): print("\033[92m {}\033[00m" .format(str))
def prRed(str): print("\033[91m {}\033[00m" .format(str))

def exit_program():
    prLightPurple("Goodbye!")
    exit()

def list_pantries():
    pantries = Pantry.get_all()
    prLightPurple(" \n---Pantries---")
    for pantry in pantries:
        print(f"{pantry.owner}")

def choose_pantry():
    prLightPurple(" \n--- Choosing Pantry ---")
    name = input("Enter the name of the pantry owner > ").strip().capitalize()
    return Pantry.find_by_owner(name)

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
    prLightPurple(" \n---Updating Pantry---")
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
    prLightPurple(" \n---Adding Food---")
    name = input("Enter name of the food > ").capitalize()
    while Food.find_by_name(name):
        pantry_id = Food.find_by_name(name).pantry_id
        owner = Pantry.find_by_id(pantry_id).owner
        prRed(f"This food already exists in {owner}'s pantry")
        name = input("Enter name of the food > ").capitalize()
    qty = input("Enter the qty of food > ")
    type_dict = {"A": "Canned Goods",
                 "B": "Baking Staples",
                 "C": "Condiments",
                 "G": "Grains",
                 "M": "Misc",
                 "N": "Snacks",
                 "P": "Pastas",
                 "S": "Spices"}
    key = input(
        "Select the type of food. \n\
        A - Canned Goods \n\
        B - Baking Staples \n\
        C - Condiments \n\
        G - Grains \n\
        M - Misc \n\
        N - Snacks \n\
        P - Pastas \n\
        S - Spices \n\
        > ").strip().capitalize()
    while type_dict.get(key) == None:
        prRed(f"{key} is not an available selection.")
        key = input(
        "Select the type of food. \n\
        A - Canned Goods \n\
        B - Baking Staples \n\
        C - Condiments \n\
        G - Grains \n\
        M - Misc \n\
        N - Snacks \n\
        P - Pastas \n\
        S - Spices \n\
        > ").strip().capitalize()
    type = type_dict[key]
    try: 
        food = Food.create(name, qty, type, pantry_id)
        prGreen(f"Added to {Pantry.find_by_id(pantry_id).owner}'s pantry: {food.name}")
    except Exception as exc:
        prRed("Error adding food: ")
        prRed(exc)

def remove_food(pantry_id):
    owner_foods = Food.find_by_pantry(pantry_id)
    max_input = len(owner_foods)
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
