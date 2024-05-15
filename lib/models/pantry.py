from models.__init__ import CURSOR, CONN
from models.food import Food

class Pantry:

    all = {}

    def __init__(self, owner, id=None):
        self.id = id
        self.owner = owner

    def __repr__(self):
        return (f"<Owner {self.id}: {self.owner}")

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        if isinstance(owner, str) and len(owner) > 0:
            format_owner = owner.capitalize()
            self._owner = format_owner
        else:
            raise Exception("Owner name must be a string with at least 1 character.")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS pantries (
            id INTEGER PRIMARY KEY,
            owner TEXT)
        """

        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS pantries;
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO pantries (owner)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.owner,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, owner):
        pantry = cls(owner)
        pantry.save()
        return pantry
    
    @classmethod
    def instance_from_db(cls, row):
        pantry = cls.all.get(row[0])
        if pantry:
            pantry.owner = row[1]
        else:
            pantry = cls(row[1])
            pantry.id = row[0]
            cls.all[pantry.id] = pantry
        return pantry
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM pantries
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
