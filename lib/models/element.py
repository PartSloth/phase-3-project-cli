from models.__init__ import CURSOR, CONN

class Element:
    all = {}

    def __init__(self, name, letter, number, mass, id = None):
        self.name = name
        self.letter = letter
        self.mass = mass
        self.number = number

    def __repr__(self):
        return f"<Element {self.id}: {self.name}, {self.letter}, {self.number}, {self.mass}>"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            formatted_name = name.capitalize()
            self._name = formatted_name
        else:
            raise Exception("Name must be a string.")

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
            name TEXT,
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
            INSERT INTO elements (name, letter, number, mass)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.letter, self.number, self.mass))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, name, letter, number, mass):
        element = cls(name, letter, number, mass)
        element.save()
        return element
    
    @classmethod
    def instance_from_db(cls, row):
        element = cls.all.get(row[0])
        if element:
            element.name = row[1]
            element.letter = row[2]
            element.number = row[3]
            element.mass = row[4]
        else:
            element = cls(row[1], row[2], row[3], row[4])
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