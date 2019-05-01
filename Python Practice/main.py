#imports the module Calculator from the calculator file
from calculator import Calculator

#creates an object of the Calculator class
calculate = Calculator()

#calls the __str__ method that returns my name
print(calculate)

#calculates the sum
def addNumbers():    
    input_string = input("Enter the numbers you want to add, separated by space: ")
    list_add = input_string.split()
    print("The sum is: ")
    calculate.printSum(list_add)

#calculates the subtraction
def subtractNumbers():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(str(num1) + " - " + str(num2) + " is: ")
    calculate.printSubtraction(num1, num2)

#calculates the quotient
def divideNumbers():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(str(num1) + " divided by " + str(num2) + " is: ")
    calculate.printQuotient(num1, num2)

#calculate the product
def multiplyNumbers():    
    input_string = input("Enter the numbers you want to multiply, separated by space: ")
    list_add = input_string.split()
    print("The product is: ")
    calculate.printProduct(list_add) 

#display menu
input_operation = input("What would you like to do today?\n" +
                        " 1. Add numbers \n 2. Subtract numbers" +
                        "\n 3. Multiply numbers \n 4. Divide numbers\n\n")
if input_operation == '1':
    #call the add numbers method
    addNumbers()
elif input_operation == '2':
    #call the subtract numbers method
    subtractNumbers()
elif input_operation == '3':
    #call the multiply numbers method
    multiplyNumbers()
elif input_operation == '4':
    #call the divide numbers method
    divideNumbers()
else:
    print("Sorry, no such option exists!")
    


