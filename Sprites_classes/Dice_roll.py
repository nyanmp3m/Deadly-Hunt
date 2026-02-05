import random
class DiceRoll():
    def D4(self):
        result = random.randint(1, 4)
        return result
    def D20(self):
        result = random.randint(1, 20)
        return result
    def D6(self):
        result = random.randint(1, 6)
        return result
