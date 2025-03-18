"""
In Python, when defining methods within a class, the first parameter is always self. 
The parameter self is a convention not a keyword and it plays a key role in Python’s object-oriented structure.
"""

class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Set instance attribute
        self.model = model  # Set instance attribute

    def display(self):
        return self.brand, self.model

# Create an instance of Car
car1 = Car("Toyota", "Corolla")

# Call the display_info method
print(car1.display())  # Output: This car is a Toyota Corolla

#############################################################################################

class gfg:
    def __init__(self, topic):
        self._topic = topic  # Rename the instance variable to avoid conflict

    def topic(self):
        print("Topic:", self._topic)  # Access the renamed variable

# Creating an instance of gfg
ins = gfg("Python")

# Calling the topic method
ins.topic()  

#############################################################################################

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        a = 3.14 * self.r ** 2
        return a

# Creating an instance of Circle
ins = Circle(5)

# Calling the area method
print("Area of the circle:", ins.area())