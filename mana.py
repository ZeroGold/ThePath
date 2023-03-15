class Mana:
    def __init__(self,a = 100, canCast = True):
        self.a = a
        self.canCast = canCast
    def cast(self):
        if self.a <= 0:
            print("\n Out of Mana")
            self.canCast = False
        if self.a >= 0:
            self.a = self.a - 10
            return self.a









