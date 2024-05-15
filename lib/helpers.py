# lib/helpers.py
from models.food import Food
from models.pantry import Pantry

def list_foods():
    foods = Food.get_all()
    print("***")
    for food in foods:
        print(f"{food.name} ({food.qty})")
    print("***")

def exit_program():
    print("Goodbye!")
    exit()
