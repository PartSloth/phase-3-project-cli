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
        if name in Food.all:
            raise Exception("Food already exists in someone's pantry.")
        if isinstance(name, str) and len(name) > 2:
            self._name = name.capitalize()
        else:
            raise Exception("Name must be a string that is longer than 2 characters.")

    @property
    def qty(self):
        return self._qty
    
    @qty.setter
    def qty(self, qty):
        qty_int = int(qty)
        if 1 <= qty_int <= 10:
            self._qty = qty_int
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
            pantry_id INTEGER,
            FOREIGN KEY (pantry_id) REFERENCES pantry(id))
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

    def update(self):
        sql = """
            UPDATE foods
            SET name = ?, qty = ?, type = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.qty, self.type, self.id))
        CONN.commit()

        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, name, qty, type, pantry_id):
        food = cls(name, qty, type, pantry_id)
        food.save()
        return food
    
    def delete(self):
        sql = """
            DELETE FROM foods
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None
    
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
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM foods
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_pantry(cls, pantry_id):
        sql = """
            SELECT *
            FROM foods
            WHERE pantry_id = ?
        """

        rows = CURSOR.execute(sql, (pantry_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM foods
            WHERE name = ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None