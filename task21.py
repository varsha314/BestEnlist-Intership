# Merged list of tuples from the given two lists using zip() and list()
def merge(list1, list2):
    merged_list = list(zip(list1, list2))
    return merged_list


list_1 = [1, 2, 3]
list_2 = ['a', 'b', 'c']
print("LIST 1:", list_1)
print("List 2:", list_2)
print("MERGED LIST OF TUPLES:", merge(list_1, list_2))

# Merge the given list and the range[1 to 8] together to create a new list of tuples using zip
range = [1, 2, 3, 4, 5, 6, 7, 8]
print("RANGE:", range)
list_3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print("LIST:", list_3)
result = list(zip(range, list_3))
print("MERGED LIST OF TUPLES WITH RANGE:", result)

# Sorting list in ascending order using sorted()
list_4 = [3, 1, 8, 6, 9, 4, 2]
print("LIST:", list_4)
list_5 = sorted(list_4)
print("SORTED LIST:", list_5)

# Filter the even numbers so that only odd numbers are passed to the new list
numbers = [2, 1, 4, 3, 5, 8, 9, 7, 0, 11, 25, 36]
print("NUMBERS:",numbers)
is_odd = lambda x: x % 2 != 0
list_6 = list(filter(is_odd, numbers))
print("FILTERED OUTPUT:", list_6)
