"""
Loops in Python are used to repeat actions efficiently. 
The main types are For loops (counting through items) and While loops (based on conditions). 
Additionally, Nested Loops allow looping within loops for more complex tasks. 
While all the ways provide similar basic functionality, they differ in their syntax and condition-checking time.
"""

# While Loop
cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")

# Using else statement with While Loop
cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")
else:
    print("In Else Block")

# Infinite While Loop
count = 0
while (count == 0):
    print("Hello Geek")

#############################################################################################

# For Loop
n = 4
for i in range(0, n):
    print(i)

# Example with List, Tuple, String, and Dictionary Iteration Using for Loops
li = ["geeks", "for", "geeks"]
for i in li:
    print(i)
    
tup = ("geeks", "for", "geeks")
for i in tup:
    print(i)
    
s = "Geeks"
for i in s:
    print(i)
    
d = dict({'x':123, 'y':354})
for i in d:
    print("%s  %d" % (i, d[i]))
    
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i),

# Iterating by the Index of Sequences
list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])

# Using else Statement with for Loop
list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])
else:
    print("Inside Else Block")

#############################################################################################

# Nested Loops
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()

#############################################################################################

# Loop Control Statements
# Continue Statement
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)

# Break Statement
for letter in 'geeksforgeeks':    
    if letter == 'e' or letter == 's':
        break

print('Current Letter :', letter)

# Pass Statement
for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)

#############################################################################################

# How for loop works internally in Python?
fruits = ["apple", "orange", "kiwi"]
iter_obj = iter(fruits)
while True:
    try:
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
        break