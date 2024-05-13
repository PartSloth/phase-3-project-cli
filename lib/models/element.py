from models.__init__ import CURSOR, CONN

class Element:
    all = {}

    def __init__(self, letter, number, mass, id = None):
        self.letter = letter
        self.mass = mass
        self.number = number

    def __repr__(self):
        return f"<Element {self.id}: {self.letter}, {self.number}, {self.mass}>"

    @property
    def letter(self):
        return self._letter
    
    @letter.setter
    def letter(self, letter):
        if isinstance(letter, str) and 1 <= len(letter) <= 2:
            formatted_letter = letter.capitalize()
            self._letter = formatted_letter
        else:
            raise Exception("Element must be a string of 1-2 characters long.")
        
    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, number):
        if isinstance(number, int) and 1 <= number <= 118:
            self._number = number
        else:
            raise Exception("Atomic number must be an integer between 1-118 inclusive.")

    @property
    def mass(self):
        return self._mass
    
    @mass.setter
    def mass(self, mass):
        if isinstance(mass, float) and 1.01 <= mass <= 294.0:
            self._mass = mass
        else:
            raise Exception("Atomic mass must be between 1.01 and 294.0")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS elements (
            id INTEGER PRIMARY KEY,
            letter TEXT,
            number INT,
            mass FLOAT)
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS elements;
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO elements (letter, number, mass)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.letter, self.number, self.mass))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, letter, number, mass):
        element = cls(letter, number, mass)
        element.save()
        return element
    
    @classmethod
    def instance_from_db(cls, row):
        element = cls.all.get(row[0])
        if element:
            element.letter = row[1]
            element.number = row[2]
            element.mass = row[3]
        else:
            element = cls(row[1], row[2], row[3])
            element.id = row[0]
            cls.all[element.id] = element
        return element
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM elements
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]