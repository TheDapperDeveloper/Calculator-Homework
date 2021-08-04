firstNumber = input("Enter first number")
intFirstNumber = int(firstNumber)
print("Select an operation: add, subtract, multiply, divide")
operand = input()
secondNumber = input("Enter second number")
intSecondNumber = int(secondNumber)

if operand == "add":
    print(intFirstNumber + intSecondNumber)
if operand == "subtract":
    print(intFirstNumber - intSecondNumber)
if operand == "multiply":
    print(intFirstNumber * intSecondNumber)
if operand == "divide":
    print(intFirstNumber / intSecondNumber)