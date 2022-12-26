import random
import math

class Calculations:
    @staticmethod
    def random_choice(self, arr: [], repeats: int) -> []:
        arr_ret = []
        for i in range(repeats):
            arr_ret.append(random.choice(arr))
        return arr_ret
    @staticmethod
    def check_chance(self, chance_percent: int) -> bool: return random.randint(0, 100) > chance_percent


calc = Calculations()

print(calc.check_chance(calc, 50))