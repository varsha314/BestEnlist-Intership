# Read mode
file1 = open("30days30hours.txt", "r")
print("Initial file:")
print(file1.read())
file1.close()

# Write mode
file1 = open("30days30hours.txt", "w")
file1.write("I have completed 10 days successfully")
file1.close()

# Read mode
file1 = open("30days30hours.txt", "r")
print("File after writing:")
print(file1.read())
file1.close()

# Append mode
file1 = open("30days30hours.txt", "a")
file1.write("-Varsha")
file1.close()

# Read mode
file1 = open("30days30hours.txt", "r")
print("File after appending:")
print(file1.readlines())
file1.close()
