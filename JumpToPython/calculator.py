# calculator.py
class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self,a,b):
        self.first = a
        self.second = b
    def sum(self):
        return self.first + self.second
    def mul(self):
        return self.first * self.second
    def sub(self):
        return self.first - self.second
    def div(self):
        return self.first / self.second

a = Calculator(4,0)
print ("sum = "+f'{a.sum()}')
print ("sub = "+f'{a.sub()}')
print ("mul = "+f'{a.mul()}')
print ("div = "+f'{a.div()}')

class MoreCalculator(Calculator):
    def pow(self):
        return self.first ** self.second
a = MoreCalculator(2,3)
print ("pow = "+f'{a.pow()}')