def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b 
##Don't include the print infront of the input because it is used to store as string and if you use the float or int in front of input it is used to store in the form of int or float
a=float(input("Enter your first number:"))
op = input("Enter the operator:")
b=float(input("Enter your second number:" ))

if op == "+" :
    print("Result:",addition(a, b))
elif op == "-" :
    print("Reuslt:",subtraction(a, b))
elif(op =="*"):
    print(multiplication(a, b))
elif(op == "/"):
    print(division(a, b))
else:
    print("please enter the operator")

    

    