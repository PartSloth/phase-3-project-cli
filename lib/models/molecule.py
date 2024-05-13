from models.__init__ import CURSOR, CONN
from models.element import Element

class Molecule:

    all = []

    def __init__(self, formula, id = None):
        self.formula = formula
        Molecule.all.append(self)

    @property
    def formula(self):
        return self.formula
    
    @formula.setter
    def formula(self, formula):
        pass