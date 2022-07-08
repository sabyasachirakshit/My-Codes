class Calculator:
    @staticmethod
    def add(n1, n2):
        return n1+n2

    @staticmethod
    def substract(n1, n2):
        return n1-n2

    @staticmethod
    def multiply(n1, n2):
        return n1*n2

    @staticmethod
    def divide(n1, n2):
        if n2 == 0:
            return "Can't divide by 0"
        else:
            return n1//n2


calculator = Calculator()
print(calculator.add(5, 10))
print(calculator.substract(10, 5))
print(calculator.multiply(10, 5))
print(calculator.divide(10, 5))
