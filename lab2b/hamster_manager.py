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

    def check_rice(self, food_sum, array, i, position, step_avarice):
        if food_sum + array[i + 1].food + array[i + 1].avarice * (position - 1) + step_avarice > self.stock:
            print(position)
            return True
        else:
            return False

    def hmstr_rice(self, position, array, food_sum, i, prev, step_avarice):
        if position == len(array):
            return str(position)
        else:
            if self.check_rice(food_sum, array, i, position, step_avarice):
                return True
            vari = position
            pre_position = position + position // 2
            if prev < pre_position:
                position = (position + prev) // 2
            else:
                position = pre_position
            prev = vari
            self.hmstr_half(array, position, prev)

    def check_down(self, food_sum, array, i, position, step_avarice):
        if food_sum - array[i].food - array[i].avarice * (position - 1) - step_avarice < self.stock:
            print(position - 1)
            return True
        return False

    def hmstr_down(self, food_sum, array, i, position, step_avarice, prev):
        if self.check_down(food_sum, array, i, position, step_avarice):
            return True
        vari = position
        pre_position = position // 2
        if prev > pre_position:
            position = (position + prev) // 2
        else:
            position = pre_position
        prev = vari
        if position == 0:
            return position
        else:
            self.hmstr_half(array, position, prev)

    def hmstr_half(self, array, position, prev):
        food_sum = 0
        step_avarice = 0
        for i in range(0, position):
            food_sum += array[i].food + array[i].avarice * (position-1)
            step_avarice += array[i].avarice
        if food_sum <= self.stock:
            if self.hmstr_rice(position, array, food_sum, i, prev, step_avarice):
                return
        else:
            if self.hmstr_down(food_sum, array, i, position, step_avarice, prev):
                return
