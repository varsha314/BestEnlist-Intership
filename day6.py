# Merging two Python dictionaries
d1 = {1: "Apple", 2: "Orange", 3: "Grapes"}
d2 = {'a': "apple", 'o': "orange", 'g': "grapes"}
print("Dictionary 1", d1)
print("Dictionary 2", d2)
d3 = d1.copy()
for key, value in d2.items():
    d3[key] = value
print("Merged dictionary", d3)

# Removing a key from dictionary
d1 = {5: "Ball", 8: "Bat", 10: "Helmet"}
print("Dictionary", d1)
del d1[8]
print("Dictionary after removing an element", d1)

# Mapping two lists into a dictionary
l1 = [10, 20, 30, 40]
print("List1", l1)
l2 = ["Cricket", "Football", "Badminton", "Tennis"]
print("List2", l2)
new_dict = dict(zip(l1, l2))
print("Mapped dictionary", new_dict)

# Finding length of a set
Csk = {"Dhoni", "Raina", "Jadeja"}
print("Set", Csk)
length = len(Csk)
print("Length of the set:", length)

# Removing the intersection of a 2nd set from the 1st set
s1 = {1, 2, 4, 6, 7, 8}
s2 = {1, 3, 5, 7, 8, 9}
print("Set 1", s1)
print("Set 2", s2)
s1 = s1 - s2
print("After removing intersection", s1)
