# Python script to merge two Python dictionaries
dict1 = {1: 'a', 2: 'b'}
print("Dictionary 1:", dict1)
dict2 = {3: 'x', 4: 'y'}
print("Dictionary 2:", dict2)
d = dict1.copy()
d.update(dict2)
print("Merged dictionary:", d)



# Sort the value from descending to ascending in list and convert it in to a set.
list1 = [1, 5, 23, 16, 100, 78, 69]
x = sorted(list1, reverse=True)
print("Sorted list in descending order:", x)
set1 = set(x)
print("Resultant set:", set1)



# List number of items in a dictionary key
dict3={1:'a',7:'b',3:'c'}
print("The dictionary:",dict3)
print("Number of items in dictionary key:",len(dict3.keys()))
# Sorting the list with the help of a function
list2 =[]
list3=[]
for i in dict3.keys():
    list2.append(i)
    list3.append(i)
list4=sorted(list2)
print("Sorted list using function:",list4)

# sorting list without using function
list5=[]
while list3:
    minimum = list3[0]
    for j in list3:
        if j < minimum:
            minimum = j
    list5.append(minimum)
    list3.remove(minimum)
print("Sorted list without using function:",list5)



# Change the first occurrence of string to a user specified input
string = input("Enter the string:")
char = input("Enter the replacement letter:")
new_str = string.replace(string[0], char)
print("String after first letter replaced:",new_str)



# Changing all occurrences of the first character of string to capital letter
str=input("Enter a string")
a=str[0]
print(a)
x= str.replace(a,a.upper())
print(x)



# Find the repeated items of a list
list6 = [1,3,3,5,7,4,6,5,8,7,1,5]
print("List:",list6)
list7 = []
list8 = []
for i in list6:
    if i in list7:
        list8.append(i)
    else:
        list7.append(i)
print("The repeated elements are:", list8)



# Sum of three elements and divided by a user value
print("Enter 3 numbers:")
a=int(input("Number 1:"))
b=int(input("Number 2:"))
c=int(input("Number 3:"))
sum=a+b+c
print("Sum is: ",sum)
d=int(input("Enter the number to divide sum"))
r=sum/d
print("Result",r)



# Mean,median,mode of three given numbers
given_numbers = [1,2,2]
sum=0
for i in given_numbers:
    sum+=i
print("Mean=",sum/len(given_numbers))

if len(given_numbers)%2==0:
    median1 = given_numbers[len(given_numbers)//2]
    median2=given_numbers[len(given_numbers)//2-1]
    median = (median1+median2)/2
else:
    median = given_numbers[len(given_numbers)//2]
print("Median=",median)

import statistics
mode1=statistics.mode(given_numbers)
print("mode is :",mode1)

# Program to swap cases of a given string
s1 ,s2= "dhoni","raina"
print("Initial strings:",s1,s2)
temp = s1
s1=s2
s2=temp
print("Swapped strings:",s1,s2)



# Convert an integer to binary & octa decimal

num = 16
print("The number is:",num)
print("Binary:",bin(num))
print("Octa decimal:",oct(num))





