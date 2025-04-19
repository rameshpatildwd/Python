#here instead of printing result in function we are returning it
#global variables are eliminated by this method and inputs taken while invoking function

def addition (num1, num2):
    add = num1 + num2
    return add

def subtraction (num1, num2):
    sub = num1 - num2
    return sub

def multiplication (num1, num2):
    mul = num1 * num2
    return mul

def division (num1, num2):
    div = num1 // num2
    return div

def modulus (num1, num2):
    mod = num1 % num2
    return mod


print(f"value of addition:", addition(5, 10))
print(f"value of Subtraction:", subtraction(100, 10))
print(f"value of Multiplication:", multiplication(14, 10))
print(f"Value of Division:", division(100, 10))
print(f"Value of Remainder:", modulus(200, 25))