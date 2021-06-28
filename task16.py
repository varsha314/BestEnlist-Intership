# Lambda function that multiplies argument x with argument y
t = lambda x, y: x * y
print(t(5, 7))

# Fibonacci series to n using Lambda
from functools import reduce

fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],
                       range(n - 2), [0, 1])
n = int(input("ENTER NUMBER OF TERMS IN FIBONACCI SERIES:"))
print(fib(n))

# Multiplying each number of given list with a given number
list_1 = [2, 4, 6, 8, 10]
print("List:", list_1)
num = int(input("Number to be multiplied to elements of the list:"))
new = list(map(lambda x: x * num, list_1))
print("Resultant list:", new)

# Finding numbers divisible by 9 from a list of numbers
list_2 = [9, 11, 27, 40, 50]
print("List:", list_2)
new_1 = list(map(lambda y: y % 9 == 0, list_2))
print("Element divisible by 9:", new_1)
list_3 = list(filter(lambda y: y % 9 == 0, list_2))
print("Resultant list:", list_3)


# Counting the even numbers in a given list
list_4 = [2, 4, 5, 6, 8, 7, 9, 0, 11, 33, 24, 57, 68, 90, 100]
print("List:", list_4)
list_5 = list(filter(lambda j: j % 2 == 0, list_4))
print("Resultant list of even numbers:", list_5)
print("Total number of even numbers:", len(list_5))
