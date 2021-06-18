# Function to input two integers from user and perform addition subtraction,division and multiplication
def get():
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))
    print("Addition of two numbers is", num1 + num2)
    print("Subtraction of two numbers is", num1 - num2)
    print("Division of two numbers is", int(num1 / num2))
    print("Multiplication of two numbers is", num1 * num2)


# Function call
get()





# Function accepting 2 parameters one with a default value
def covid(patient_name, body_temp=98):
    print("Patient name:", patient_name)
    print("Body temperature in degree celsius:", body_temp)


# Function call with arguments
covid("Ram", 105)
covid("Priya")
