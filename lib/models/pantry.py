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
        if isinstance(owner, str) and len(owner) > 0 and not owner.isdigit():
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

    @classmethod
    def create(cls, owner):
        pantry = cls(owner)
        pantry.save()
        return pantry

    def save(self):
        sql = """
            INSERT INTO pantries (owner)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.owner,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def update(self):
        sql = """
            UPDATE pantries
            SET owner = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.owner, self.id))
        CONN.commit()

        type(self).all[self.id] = self
    
    def delete(self):
        sql = """
            DELETE FROM pantries
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None
    
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
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM pantries
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_owner(cls, owner):
        sql = """
            SELECT *
            FROM pantries
            WHERE owner = ?
        """

        row = CURSOR.execute(sql, (owner,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
