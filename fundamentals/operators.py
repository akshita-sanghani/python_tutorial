"""
In Python programming, Operators in general are used to perform operations on values and variables. 
These are standard symbols used for logical and arithmetic operations. In this article, we will look into different types of Python operators. 

OPERATORS: These are the special symbols. Eg- + , * , /, etc.
OPERAND: It is the value on which the operator is applied.

Types of Operators in Python-----------
Arithmetic Operators
Comparison Operators
Logical Operators
Bitwise Operators
Assignment Operators
Identity Operators and Membership Operators
"""


# Arithmetic Operators
a = 15
b = 4

print("Addition:", a + b)  # Addition
print("Subtraction:", a - b) # Subtraction
print("Multiplication:", a * b)  # Multiplication
print("Division:", a / b) # Division
print("Modulus:", a % b) # Modulus
print("Exponentiation:", a ** b) # Exponentiation

#############################################################################################

# Comparison Operators
a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

#############################################################################################

# Logical Operators
a = True
b = False
print(a and b)
print(a or b)
print(not a)

#############################################################################################

# Bitwise Operators
a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

#############################################################################################

# Assignment Operators
a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

#############################################################################################

# Identity Operators
a = 10
b = 20
c = a

print(a is not b)
print(a is c)

#############################################################################################

# Membership Operators
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

#############################################################################################

# Ternary Operator
a, b = 10, 20
min = a if a < b else b

print(min)