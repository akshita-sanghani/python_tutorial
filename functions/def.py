"""
Python def keyword is used to define a function, it is placed before a function name that is provided by the user to create a user-defined function. 
In Python, a function is a logical unit of code containing a sequence of statements indented under a name given using the “def” keyword. 
In Python def keyword is the most used keyword.

Table of Content------------

Python def Syntax
Passing Function as an Argument
Python def keyword example with *args
Python def keyword example with **kwargs
Python def keyword example with the class

"""

# defining function
def func():
    print("Hello")

# calling function    
func()

#############################################################################################

# Example 1: Create function to find the subtraction of two Numbers
# function for subtraction of 2 numbers.
def subNumbers(x, y):
    return (x-y)

# main code
a = 90
b = 50

# finding subtraction
res = subNumbers(a, b)

# print statement
print("subtraction of ", a, " and ", b, " is ", res)

# Example 2: Create function with the first 10 prime numbers
def fun(n):
    x = 2
    count = 0
    while count < n:
        for d in range(2, int(x ** 0.5) + 1):  # check divisibility only up to sqrt(x)
            if x % d == 0:
                break  # if divisible, it's not prime, so break the loop
        else:
            print(x)  # prime number
            count += 1
        x += 1

# Driver Code
n = 10

fun(n)

#############################################################################################

# Passing Function as an Argument
# A function that takes another function as an argument
def fun(func, arg):
    return func(arg)
  
def square(x):
    return x ** 2
  
# Calling fun and passing square function as an argument  
res = fun(square, 5)
print(res)

#############################################################################################

# Python def keyword example with *args
def fun(*args):
    for arg in args:
        print(arg)

# Calling the function with multiple arguments
fun(1, 2, 3, 4, 5)

#############################################################################################

# Python def keyword example with **kwargs
def fun(**kwargs):
    for k, val in kwargs.items():
        print(f"{k}: {val}")

#############################################################################################

# Calling the function with keyword arguments
fun(name="Alice", age=30, city="New York")

# Python def keyword example with the class
class Person:
    # Constructor to initialize the person's name and age
    def __init__(self, name, age):
        self.name = name  # Set the name attribute
        self.age = age    # Set the age attribute
    
    # Method to print a greeting message
    def greet(self):
        print(f"Name - {self.name} and Age - {self.age}.")

# Create an instance of the Person class
p1 = Person("Alice", 30)

# Call the greet method to display the greeting message
p1.greet()