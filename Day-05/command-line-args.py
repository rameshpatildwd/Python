import sys      #required to read command line args

def addition(num1, num2):       #defining addition function
    add = num1 + num2
    return(add)

def subtraction(num1, num2):    #defining subtraction function
    sub = num1 - num2
    return(sub)

def multiplication(num1, num2): #defining multiplication function
    mul = num1 * num2
    return(mul)

def division(num1, num2):       #defining division function
    div = num1 // num2
    return(div)

def remainder(num1, num2):      #defining remainder function
    rem = num1 % num2
    return(rem)

num1 = float(sys.argv[1])       #command line args
operator = sys.argv[2]
num2 = float(sys.argv[3])

if operator == "add":
    print(f"Value of Addition:", addition(num1, num2))

if operator == "sub":
    print(f"Value of Subtraction:", subtraction(num1, num2))

if operator == "mul":
    print(f"Value of Multiplication:", multiplication(num1, num2))

if operator == "div":
    print(f"Value of Division:", division(num1, num2))

if operator == "rem":
    print(f"Value of Remainder:", remainder(num1, num2))
