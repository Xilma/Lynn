#An abstract class for a calculator
class Calculator:
    #the initializer method
    def __init__(self):
        #initializes sum, product, subtract and division variables
        self.addition = 0
        self.product = 1
        self.subtract = 0
        self.division = 0

    #the str method
    def __str__(self):
        #user inputs name
        name = input("Enter your name: ")
        return "Hello, " + name

    #the sum method
    def printSum(self, sumList):
        for number in sumList:
            self.addition += int(number)
        print(self.addition)

    #the subtract method
    def printSubtraction(self, num1, num2):
        self.subtract = num1 - num2
        print (self.subtract)

    #the product method
    def printProduct(self, prodList):
        for prod in prodList:
            self.product *= int(prod)
        print(self.product)

    #the division method
    def printQuotient(self, num1, num2):
        try:
            self.division = num1/num2
            print(self.division)
        except ZeroDivisionError:
            print("Error, division by zero")
