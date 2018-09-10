#class of an object we compare
class Printer:

    def __init__(self, name, speed, price, *args):
        self.name = name
        self.speed = speed
        self.price = price

    def __repr__(self):
        return str(self.name)+" "+str(self.speed)+" "+str(self.price)+" | "
