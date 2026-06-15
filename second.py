number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))

operator = input("Select[+,-,/]: ")
try:
    if operator == "+":
        print(number1 + number2)
    elif operator == "-":
        print(number1 - number2)
    elif operator == "/":
        print(number1/number2)
    else:
        print("Invalid operator")
except KeyboardInterrupt:
    print("exiting")
except ZeroDivisionError:
    print("Cannot divide by zero")


