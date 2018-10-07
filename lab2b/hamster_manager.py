class HamsterManager:

    def __init__(self, stock):
        self.stock = stock
        self.choosen = []

    def hmstr_choose(self, array):
        food_sum = 0
        avarice_by_step = 0
        for hamster in array:
           if food_sum + hamster.food + (len(self.choosen)-1) * hamster.avarice + avarice_by_step <= self.stock:
               self.choosen.append(hamster)
               food_sum += hamster.food
               food_sum += (len(self.choosen)-1)*hamster.avarice
               food_sum += avarice_by_step
               avarice_by_step += hamster.avarice
           else:
               break
        return self.choosen