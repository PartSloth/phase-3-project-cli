# lib/helpers.py
from models.food import Food
from models.pantry import Pantry

def exit_program():
    print("Goodbye!")
    exit()

def list_pantries():
    pantries = Pantry.get_all()
    print("---Pantries---")
    for pantry in pantries:
        print(f"   {pantry.owner}")

def choose_pantry():
    print("--- Choosing Pantry ---")
    name = input("Enter the name of the pantry owner > ").strip().capitalize()
    return Pantry.find_by_owner(name)

def add_pantry():
    print("--- Adding Pantry ---")
    name = input("Enter the name of the pantry owner > ").strip().capitalize()
    try:
        while Pantry.find_by_owner(name):
            print("This person already has a pantry.")
            name = input("Please enter a new owner > ").strip().capitalize()
        pantry = Pantry.create(name)
        print(f"Added: {pantry}'s Pantry")
    except Exception as exc:
        print("Error creating pantry: ", exc)

def update_owner(pantry_id):
    print("---Updating Pantry---")
    if pantry := Pantry.find_by_id(pantry_id):
        try:
            name = input("Enter name of the pantry's new owner > ").strip().capitalize()
            while Pantry.find_by_owner(name):
                print("This person already has a pantry.")
                name = input("Enter name of the pantry's new owner > ").strip().capitalize()
            pantry.owner = name
            pantry.update()
            print(f'Updated: {name}')
        except Exception as exc:
            print("Error updating pantry: ", exc)
    else:
        print(f"Pantry does not exist")

def list_foods(pantry_id):
    foods = Food.find_by_pantry(pantry_id)
    for food in foods:
        print(f"{food.name} ({food.qty})")

def add_food(pantry_id):
    print("---Adding Food---")
    name = input("Enter name of the food > ").capitalize()
    while Food.find_by_name(name):
        pantry_id = Food.find_by_name(name).pantry_id
        owner = Pantry.find_by_id(pantry_id).owner
        print(f"This food already exists in {owner}'s pantry")
        name = input("Enter name of the food > ").capitalize()
    qty = input("Enter the qty of food > ")
    type_dict = {"A": "Canned Goods",
                 "B": "Baking Staples",
                 "C": "Condiments",
                 "G": "Grains",
                 "P": "Pastas",
                 "S": "Spices"}
    key = input(
        "Select the type of food. \n\
        A - Canned Goods \n\
        B - Baking Staples \n\
        C - Condiments \n\
        G - Grains \n\
        P - Pastas \n\
        S - Spices \n\
        > ").strip().capitalize()
    type = type_dict[key]
    try: 
        food = Food.create(name, qty, type, pantry_id)
        print(f"Added to {Pantry.find_by_id(pantry_id).owner}'s pantry: {food.name}")
    except Exception as exc:
        print("Error adding food: ", exc)
