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
    Food.create('Extra virgin olive oil', 1, "Oils", 1)
    Food.create('Spaghetti', 3, 'Pastas', 1)
    Food.create('Linguine', 6, 'Pastas', 1)
    Food.create('Canned corn', 7, 'Canned Goods', 1)
    Food.create('Canola oil', 1, 'Oils', 2)
    Food.create('Water Bottles', 2, 'Misc', 2)

seed_database()
print("Seeded database")