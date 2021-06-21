# Looping through a list of numbers and add +2 to every element
list_1 = [1, 7, 14, 99, 200]
print("List:", list_1)
for i in range(len(list_1)):
    list_1[i] += 2
print("List after adding 2", list_1)

# Printing a pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")

    print()

# Fibonacci sequence
n_terms = int(input("Enter number of terms"))
n1, n2 = 0, 1
count = 0

if n_terms <= 0:
    print("Enter a positive integer")

elif n_terms == 1:
    print("Fibonacci sequence:")
    print(n1)

else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(n1, end=" ")
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1

    print()

# Armstrong number- a number that is equal to the sum of cubes of its digits
num = int(input("Enter a number:"))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

# Multiplication table of 9
print("Multiplication table of 9")
for i in range(1, 11):
    print(9, 'x', i, '=', 9 * i)

# Number is negative or positive
num_1 = int(input("Enter a number"))
if num_1 > 0:
    print(num_1, "is positive")
else:
    print(num_1, "is negative")

# Converting number of days to ages
days = int(input("Enter number of days:"))
yrs = int(days / 365)
print("No of years:", yrs)

# Trigonometry problem using math function
import math


def trig(n, m):
    if n == 'sin':
        print("Sine of ", m, " is", math.sin(m))
    elif n == 'cos':
        print("Cosine of ", m, " is", math.cos(m))
    elif n == 'tan':
        print("Tangent of ", m, " is", math.tan(m))
    elif n == 'sec':
        print("Secant of ", m, " is", (1 / math.cos(m)))
    elif n == 'cosec':
        print("Cosecant of ", m, " is", (1 / math.sin(m)))
    elif n == 'cot':
        print("Cotangent of ", m, " is", (1 / math.tan(m)))


trig("sin", 90)
trig("cos", 90)
trig("tan", 90)
trig("cosec", 90)
trig("sec", 90)
trig("cot", 90)

# Basic arithmetic calculator
print('+')
print('-')
print('*')
print('/')
choice = input("Enter your choice")
if choice == '+':
    num_1 = int(input("Number 1:"))
    num_2 = int(input("Number 2:"))
    print("Sum is", num_1 + num_2)
elif choice == '-':
    num_1 = int(input("Number 1:"))
    num_2 = int(input("Number 2:"))
    print("Difference is", num_1 - num_2)
elif choice == '*':
    num_1 = int(input("Number 1:"))
    num_2 = int(input("Number 2:"))
    print("Product is", num_1 * num_2)
elif choice == '/':
    num_1 = int(input("Number 1:"))
    num_2 = int(input("Number 2:"))
    print("Quotient is", num_1 / num_2)
else:
    print('Invalid Input')
