from models.__init__ import CONN, CURSOR
from models.molecule import Molecule
from models.element import Element

def seed_database():
    Element.drop_table()
    Element.create_table()

    Element.create('H', 1, 1.01)

seed_database()
print("Seeded database")