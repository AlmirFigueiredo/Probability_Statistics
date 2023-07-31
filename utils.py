class ArithmeticMeanCalculator:
    def __init__(self, data):
        self.data = data
    def calculate(self):
        return sum(self.data)/len(self.data)