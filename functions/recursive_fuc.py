"""
Recursion involves a function calling itself directly or indirectly to solve a problem by breaking it down into simpler and more manageable parts. 
In Python, recursion is widely used for tasks that can be divided into identical subtasks.
"""

# factorial program
def factorial(n):
    if n in (0, 1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  

#############################################################################################

# fibonacci program
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage
print(fibonacci(10))  