class Number:
    def __init__(self,  modulo, number):
        self.modulo = modulo
        self.number = number

    def __eq__(self, other: int):
        first = self.number if self.number >= 0 else self.modulo + self.number
        second = other if other >= 0 else self.modulo + other
        return first == second

    def __gt__(self, other: int):
        return self.number > other

    def __pow__(self, power):
        return Number(self.modulo, pow(self.number, power, self.modulo))

    def __mod__(self, other: int):
        return self.number % other

    def __imod__(self, other: int):
        return Number(self.modulo, self.number % other)

    def __isub__(self, other: int):
        return Number(self.modulo, self.number - other)
