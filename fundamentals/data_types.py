"""
Python Data types are the classification or categorization of data items. 
It represents the kind of value that tells what operations can be performed on a particular data. 
Since everything is an object in Python programming, Python data types are classes and variables are instances (objects) of these classes. 
The following are the standard or built-in data types in Python:

Numeric: int, float, complex
Sequence Type: string, list, tuple
Mapping Type: dict
Boolean: bool
Set Type: set, frozenset
Binary Types: bytes, bytearray, memoryview

"""

# 1. Numeric Data Types
a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2 + 4j
print(type(c))

#############################################################################################

# 2. Sequence Data Types
# 2.1 String Data Type
s = 'Welcome to the Geeks World'
print(s)

# check data type 
print(type(s))

# access string with index
print(s[1])
print(s[2])
print(s[-1])

# 2.2 List Data Type
# Empty list
a = []

# list with int values
a = [1, 2, 3]
print(a)

# list with mixed int and string
b = ["Geeks", "For", "Geeks", 4, 5]
print(b)

a = ["Geeks", "For", "Geeks"]
print("Accessing element from the list")
print(a[0])
print(a[2])

print("Accessing element using negative indexing")
print(a[-1])
print(a[-3])

# 2.3 Tuple Data Type
# initiate empty tuple
tup1 = ()

tup2 = ('Geeks', 'For')
print("\nTuple with the use of String: ", tup2)

tup1 = tuple([1, 2, 3, 4, 5])

# access tuple items
print(tup1[0])
print(tup1[-1])
print(tup1[-3])

#############################################################################################

# 3. Boolean Data Type
print(type(True))
print(type(False))
# print(type(true)) # NameError: name 'true' is not defined

#############################################################################################

# 4. Set Data Type
# initializing empty set
s1 = set()

s1 = set("GeeksForGeeks")
print("Set with the use of String: ", s1)

s2 = set(["Geeks", "For", "Geeks"])
print("Set with the use of List: ", s2)

set1 = set(["Geeks", "For", "Geeks"])
print(set1)

# loop through set
for i in set1:
    print(i, end=" ")
    
# check if item exist in set    
print("Geeks" in set1)

#############################################################################################

# 5. Dictionary Data Type
# initialize empty dictionary
d = {}


d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)

d = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# Accessing an element using key
print(d['name'])

# Accessing a element using get
print(d.get(3))