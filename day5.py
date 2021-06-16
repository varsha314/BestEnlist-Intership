# List creation
l = [1, 3, 5, 7]
print(l)

# Add an item in to the list
l.append(9)
print(l)
l.insert(2, 0)
print(l)

# Delete an item from the list
del l[2]
print(l)
a = l.pop()
print("The deleted element is ", a)
print(l)
l.remove(5)
print(l)

# Storing the largest number from the list to a variable
g = max(l)
print("Largest number is", g)

# Storing the Smallest number from the list to a variable
s = min(l)
print("Smallest number is", s)





# Creation of a tuple
t = (10, 8, 6, 4)
print(t)

# Printing reverse of the tuple
r = reversed(t)
print(tuple(r))





# Converting tuple to list
x = ('s', 't', 'r', 'i', 'n', 'g')
print(x)
y = list(x)
print(y)
