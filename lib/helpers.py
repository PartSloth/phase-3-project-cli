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
    prLightPurple(" \n--- Pantries ---")
    for i, pantry in enumerate(pantries, 1):
        print(f"{i}. {pantry.owner}")
    if len(pantries) == 0:
        prRed("There are no pantries. Please add a pantry!")

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
        choice = int(choice) - 1
        if 0 <= choice <= len(pantries) - 1:
            return pantries[choice]
        else:
            prRed(f"Input is out of bounds, maximum input is: {len(pantries)}.")
    else:
        prRed("Enter numbers only.")

def add_pantry():
    prLightPurple(" \n--- Adding Pantry ---")
    name = input("Enter the name of the pantry owner > ").strip().capitalize()
    try:
        Pantry.is_owner_new(name)
        Pantry.create(name)
        prGreen(f"Added: {name}'s Pantry")
    except Exception as exc:
        prRed(f"Error creating pantry: {exc}")

def update_owner(pantry):
    prLightPurple(" \n--- Updating Pantry ---")
    name = input("Enter name of the pantry's new owner > ").strip().capitalize()
    try:
        Pantry.is_owner_new(name)
        pantry.owner = name
        pantry.update()
        prGreen(f'Updated: {name}')
    except Exception as exc:
        prRed(f"Error creating pantry: {exc}")

def list_foods(pantry):
    foods = pantry.foods()
    for i, food in enumerate(foods, 1):
        print(f"{i}. {food.name} ({food.qty})")  
    if len(foods) == 0:
        print("This pantry is empty.")

def add_food(pantry):
    prLightPurple(" \n--- Adding Food ---")
    name = input("Enter name of the food > ").capitalize()
    qty = input("Enter the qty of food > ")
    type = category_select()
    try: 
        Food.is_food_new(name)
        food = Food.create(name, qty, type, pantry.id)
        prGreen(f"Added to {pantry.owner}'s pantry: {name}")
    except Exception as exc:
        prRed(f"Error adding food: {exc}")

def delete_pantry(pantry = None):
    pantries = Pantry.get_all()
    if pantries == None:
        prRed("There are no pantries to delete.")
    elif pantry: 
        foods = pantry.foods()
        for food in foods:
            food.delete()
        pantry.delete()
    else:
        prLightPurple(" \n--- Deleting Pantry ---")
        choice = input("Enter the pantry number > ")
        if choice.isnumeric():
            choice = int(choice) - 1
            if 0 <= choice <= len(pantries) - 1:
                foods = pantries[choice].foods()
                for food in foods:
                    food.delete()
                pantries[choice].delete()
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
    return type_dict[key]

def remove_food(pantry):
    foods = pantry.foods()
    if len(foods) == 0:
        prRed("Pantry is empty. Please add food first!")
    else: 
        choice = input("Which food do you want to remove > ")
        if choice.isnumeric():
            choice = int(choice) - 1
            if 0 <= choice <= len(foods) - 1:
                foods[choice].delete()
                prGreen(f"{foods[choice].name} has been removed from the pantry.")
            else:
                prRed(f"Input is out of bounds, maximum input is: {len(foods)}.")
        else:
            prRed("Please enter numbers only.")

def select_food(pantry):
    foods = pantry.foods()
    if len(foods) == 0:
        prRed("Pantry is empty. Please add food first!")
    else: 
        choice = input("Which food do you want to update > ")
        if choice.isnumeric():
            choice = int(choice) - 1
            if 0 <= choice <= len(foods) - 1:
                return foods[choice]
            else:
                prRed(f"Input is out of bounds, maximum input is: {len(foods)}.")
        else: prRed("Please enter numbers only.")

def update_food(food, choice):
    if choice == "1":
        name = input("Enter new name > ")
        food.name = name
    elif choice == "2":
        qty = input("Enter new quantity > ")
        food.qty = qty
    elif choice == "3":
        type = category_select()
        food.type = type
    try:
        food.update()
        prGreen('Updated!')
    except Exception as exc:
        prRed(f"Error updating pantry: {exc}")

def category_list(pantry):
    type = category_select()
    list = [food for food in pantry.foods() if food.type == type]
    prLightPurple(f" \n---{pantry.owner}'s {type}---")
    if len(list) > 0:
        for food in list:
            print(food.name)
    else:
        prRed(f"{pantry.owner} doesn't have any {type.lower()}.")
