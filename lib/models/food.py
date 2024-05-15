from models.__init__ import CURSOR, CONN

class Food:
    all = {}

    def __init__(self, name, qty, type, pantry_id = None, id = None):
        self.name = name
        self.qty = qty
        self.type = type
        self.pantry_id = pantry_id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 2:
            self._name = name
        else:
            raise Exception("Name must be a string that is longer than 2 characters.")

    @property
    def qty(self):
        return self._qty
    
    @qty.setter
    def qty(self, qty):
        if isinstance(qty, int) and 1 <= qty <= 10:
            self._qty = qty
        else:
            raise Exception("Qty must be an integer between 1-10 inclusive.")

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        if isinstance(type, str):
            self._type = type
        else:
            raise Exception("Food type must be a string.")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS foods (
            id INTEGER PRIMARY KEY,
            name TEXT,
            qty INTEGER,
            type TEXT,
            pantry_id INTEGER)
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS foods;
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO foods (name, qty, type, pantry_id)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.qty, self.type, self.pantry_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, name, qty, type, pantry_id):
        food = cls(name, qty, type, pantry_id)
        food.save()
        return food
    
    @classmethod
    def instance_from_db(cls, row):
        food = cls.all.get(row[0])
        if food:
            food.name = row[1]
            food.qty = row[2]
            food.type = row[3]
            food.pantry_id = row[4]
        else:
            food = cls(row[1], row[2], row[3], row[4])
            food.id = row[0]
            cls.all[food.id] = food
        return food
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM foods
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]