from math import sqrt

class Hamster:

    def __init__(self, food, avarice):
        self.food = food
        self.avarice = avarice
        self.vector = sqrt(food**2+avarice**2)

    def __repr__(self):
        return '| '+str(self.food)+', '+str(self.avarice)+', '+str(self.vector)+' |'

    def __lt__(self, other):
        return self.vector < other.vector