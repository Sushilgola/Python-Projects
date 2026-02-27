num1 = float(input("Enter Number 1: "))
opr = input("Enter operation symbols: ")
num2 = float(input("Enter Number 2: "))

try:
    if opr == '+':
        print("Sum : ",num1+num2)
    elif opr == '-':
        print("Subtraction: ", num1-num2)
    elif opr == '*':
        print("Multiplication ", num1*num2)
    elif opr == '/':
        print("Division: ", num1/num2)
except ZeroDivisionError:
    print("We can't divide any number with 0. ")
except ValueError:
    print("Please Enter the Numeric Values.")
