x = 5 # Variable 'x' stores the integer value 10
name = "Samantha"   # Variable 'name' stores the string "Samantha"
print(x)
print(name)

# Casting variables
s = "10"  # Initially a string
n = int(s)  # Cast string to integer
cnt = 5
f = float(cnt)  # Cast integer to float
age = 25
s2 = str(age)  # Cast integer to string

# Display results
print(n)  
print(f)  
print(s2)  


# Define variables with different data types
n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {'key': 'value'}
bool = True

# Get and print the type of each variable
print(type(n))   
print(type(f)) 
print(type(s))   
print(type(li))     
print(type(d))     
print(type(bool))  

# Local Variables
def f():
    a = "I am local"
    print(a)
f()

# Counting Characters in a String
word = "Python"
length = len(word)
print("Length of the word:", length) 