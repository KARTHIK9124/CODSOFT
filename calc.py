#simple calculator to demonstrate use of switch and functions.

def add():
    print("Addition of ",a," and ",b," is ",a+b)
def sub():
    print("Subtraction of ",a," and ",b," is ",a-b)
def pod():
    print("Multiplication of ",a," and ",b," is ",a*b)
def div():
    try:
        print("Division  of ",a," and ",b," is ",a/b)
    except ZeroDivisionError:
        print("Division by zero error. Try different input")
def mod():
    try:
        print("Remainder when ",b," is divided with ",a," is ",a%b)
    except ZeroDivisionError:
        print("Division by zero error. Try different input")


a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))
op=input("Enter operator  (+, - , * or /): ")

if op=='+':
    add()
elif op=='-':
    sub()
elif op=='*':
    pod()
elif op=='/':
    div()
elif op=='%':
    mod()
else:
    print("Please enter a valid operator")