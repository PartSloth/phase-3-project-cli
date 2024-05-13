# lib/helpers.py
from models.element import Element
from models.molecule import Molecule

def list_elements():
    elements = Element.get_all()
    for element in elements:
        print(element)

def exit_program():
    print("Goodbye!")
    exit()
