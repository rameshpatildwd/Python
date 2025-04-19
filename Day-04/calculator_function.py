a = 10      #Global variable
b = 15      #Global variable

#Defining a functions
def addition():
    add = a + b
    print ("Value of Addition =", add)

def subtraction():
    sub = a - b
    print("Value of Subtraction =", sub)

def multiplication():
    mul = a * b
    print("Value of Multiplication =", mul)

def division():
    div = a // b
    print("Value of Divison =", div)

def addition2():
    c = 20          #Local variable
    add2 = a + b + c
    print("Value of Addition including local varible =", add2)

#Invoke functions explicitly to print them
addition()
subtraction()
multiplication()
division()
addition2()