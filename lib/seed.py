from models.__init__ import CONN, CURSOR
from models.molecule import Molecule
from models.element import Element

def seed_database():
    Element.drop_table()
    Element.create_table()

    Element.create('Hydrogen', 'H', 1, 1.01)
    Element.create('Carbon', 'C', 12, 12.01)
    Element.create('Oxygen', 'O', 16, 16.0)

seed_database()
print("Seeded database")