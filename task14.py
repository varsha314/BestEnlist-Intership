# Simple calculator with try and except for all use cases
def addition(a, b):
    try:
        result = a + b
        print("Addition is : ", result)
    except Exception as e:
        print("Error:", e)


def subtraction(a, b):
    try:
        result = a - b
        print("subtraction is : ", result)
    except Exception as e:
        print("Error:", e)


def multiplication(a, b):
    try:
        result = a * b
        print("multiplication is : ", result)
    except Exception as e:
        print("Error:", e)


def division(a, b):
    try:
        result = a / b
        print("division is : ", result)
    except Exception as e:
        print("Error:", e)


def calculation(ch):
    try:
        a = int(input("enter first number : "))
        b = int(input("enter second number : "))
        if (ch == '+'):
            addition(a, b)
        elif (ch == '-'):
            subtraction(a, b)
        elif (ch == '*'):
            multiplication(a, b)
        elif (ch == '/'):
            division(a, b)
        else:
            print("Invalid Choice")

    except Exception as e:
        print("Only Integers Allowed")
        calculation(ch)


print("OPTIONS\n+\n-\n*\n/\n")
choice = input("Enter your choice")
calculation(choice)

# Printing one message if NameError is raised and another for other errors
try:
    c = 10
    print("Value=", c)
    print("Value=", a)
except NameError:
    print("Variable is not defined:Name Error")
except Exception as e:
    print("Other error:", e)

# When try-except scenario is not required?
# Python Exceptions are error scenarios that alter the normal execution flow of the program.
# Try catch is needed only if expected error is small and does not affect the program, in case of fatal errors try catch block is not recommended


# Getting input inside try catch block
try:
    age = int(input('Enter your age: '))
except Exception as e:
    print('You have entered an invalid value:', e)
finally:
    print("Try And Exception are finished")
