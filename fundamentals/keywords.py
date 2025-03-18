"""
The list of keywords are: 
['False', 'None', 'True',"__peg_parser__ 'and', 'as', 'assert', 'async', 'await', 'break', 
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 
'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""

import keyword

# printing all keywords at once using "kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)

#############################################################################################

#Value Keywords: True, False, None Keyword, del
print(False == 0)
print(True == 1)

print(True + True + True) ## True + True + True is  3
print(True + False + False) # True + False + False is  1
print(None == 0) # None isn't equal to  0  or an empty list []
print(None == [])

#############################################################################################

# Operator Keywords: and, or, not, in, is
a = True
b = False

## Logical operations
print(a and b)  # AND: True if both a and b are True
print(a or b)   # OR: True if at least one of a or b is True
print(not a)    # NOT: Inverts the value of a


## in keyword (membership operator)
print(3 in [1,2,3])
if 's' in 'geeksforgeeks':
    print("s is part of geeksforgeeks")
else:
    print("s is not part of geeksforgeeks")


## is keyword
print(2 is 2)

# example 2
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b) # True: a and b refer to the same object
print(a is c) # False: a and c have same value but are different objects

#############################################################################################

# # Conditional keywords in Python: if, else, elif
x = 0

# python if elif else statement
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

#############################################################################################

# # Iteration Keywords: for, while, break, continue, pass
for num in range(3):
    if num == 2:
        continue  # Skip number 2
    print(num)

count = 0
while count < 4:
    count += 1
    if count == 3:
        break  # Exit the loop when count reaches 4
    print(count)

n = 10
for i in range(n):

    # pass can be used as placeholder
    # when code is to added later
    pass

#############################################################################################

# Exception Handling Keywords
a, b = 4, 0
try:
    k = a // b  # Attempt integer division (4 // 0)
    print(k)
    
# This block catches the ZeroDivisionError
except ZeroDivisionError: 
    print("Can't divide by zero")

finally:
    # This block is always executed regardless of the exception
    print('This is always executed')


print("The value of a / b is : ")

# Will raise an AssertionError because b == 0
assert b != 0, "Divide by 0 error" 

# Division is attempted but will not reach due to assert
print(a / b)  

# Raise a TypeError if the strings are different
temp = "geeks for geeks"
if temp != "geeks":
    raise TypeError("Both the strings are different.")

#############################################################################################

# Structure Keywords : def, class, return, lambda
def fun():
  
     # Assign the value 2 to variable S
    s = 2  
    
    # Return the value of S
    return s

# Call the function and print the result
print(fun())  

# Yield Keyword
def fun():
  
      # Yield the value 1, pausing the function here
    yield 1
    # Yield the value 2, pausing the function again
    yield 2
    # Yield the value 3, pausing the function once more
    yield 3  

# Iterate through the values yielded by the function
for value in fun():
    print(value)  

#############################################################################################

# Lambda keyword
g = lambda x: x*x*x

print(g(7))

#############################################################################################

# Context Keywords: With, as Keyword in Python
with open('file_path', 'w') as file:
    file.write('hello world !')

import math as gfg

print(gfg.factorial(5))

#############################################################################################

# Import and Module: Import, From in Python
from math import factorial
import math
print(math.factorial(10))

# from keyword
print(factorial(10))

#############################################################################################

# Scope and Namespace: Global, Nonlocal in Python
a = 15
b = 10

def add():
  
      # Add global variables a and b
    c = a + b  
    print(c)

add()  # Output: 25

def fun():
  
  # Local variable in fun()
    var = 10  

    def gun():
      
          # Modify var1 in the enclosing scope (fun)
        nonlocal var  
        var += 10  
        print(var)  

    gun() 

fun() # Output: 20