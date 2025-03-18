"""
Understanding input and output operations is fundamental to Python programming. With the print() function, we can display output in various formats, 
while the input() function enables interaction with users by gathering input during program execution.
"""


print('hello World!')

#############################################################################################

name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")

#############################################################################################

x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)

#############################################################################################

# Prompting the user for input
age = int(input("Enter your age: "))

# age = int(age_input)  # Converting the input to an integer

# Checking conditions based on user input
if age < 0:
    print("Please enter a valid age.")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

#############################################################################################

#Using sep and end parameter
print("Python", end='@')
print("GeeksforGeeks")
print('G', 'F', 'G', sep='')
print('09', '12', '2016', sep='-')
print('pratik', 'geeksforgeeks', sep='@')

#############################################################################################

#Using f-string
name = 'Akshita'
age = 25
print(f"Hello, My name is {name} and I'm {age} years old.")

#############################################################################################

#Using % Operator
num = int(input("Enter a value: "))
add = num + 5
print("The sum is %d" %add)