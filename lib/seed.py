from models.__init__ import CONN, CURSOR
from models.pantry import Pantry
from models.food import Food

def seed_database():
    Food.drop_table()
    Pantry.drop_table()
    Food.create_table()
    Pantry.create_table()
    
    Pantry.create("Johnny")
    Pantry.create("Beth")
    Food.create('Extra Virgin Olive Oil', 1, "Oil", 1)

seed_database()
print("Seeded database")