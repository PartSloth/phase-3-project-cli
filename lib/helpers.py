# lib/helpers.py
from models.element import Element
from models.molecule import Molecule

def list_elements():
    elements = Element.get_all()
    print("***")
    for element in elements:
        print(f"{element.name} ({element.letter})")
    print("***")

def exit_program():
    print("Goodbye!")
    exit()
