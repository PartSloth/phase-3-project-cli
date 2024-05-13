from models.__init__ import CURSOR, CONN

class Element:
    all = []

    def __init__(self, letter, number, mass, id = None):
        self.letter = letter
        self.mass = mass
        self.number = number
        Element.all.append(self)

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
    