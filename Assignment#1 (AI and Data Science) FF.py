# 1. What is OOP?
# Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects",
# which can contain data (attributes) and code (methods). It promotes organized and reusable code.

# Example of OOP:
class Dog:
    def bark(self):
        return "Woof!"

my_dog = Dog()
print(my_dog.bark())


# 2. What is a Class?
# A class is a blueprint for creating objects. It defines properties (attributes) and methods (functions)
# that the objects created from the class will have.

# Example of a Class:
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Attribute for brand
        self.model = model  # Attribute for model

my_car = Car("Toyota", "Corolla")
print(my_car.brand)


# 3. What is an Object?
# An object is an instance of a class. It represents a specific entity with attributes and behaviors defined by its class.

# Example of an Object:
my_other_car = Car("Honda", "Civic")
print(my_other_car.model)


# 4. What is a Constructor?
# A constructor is a special method called when an object is created. It initializes the object's attributes.

# Example of a Constructor:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Florans", 30)
print(person1.name)


# 5. What is Inheritance?
# Inheritance is a mechanism where one class (child) can inherit properties and methods from another class (parent).
# This promotes code reuse and establishes a hierarchy.

# Example of Inheritance:
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

my_dog = Dog()
print(my_dog.speak())


# 6. What is Concatenation?
# Concatenation is the operation of joining two or more strings together to form a single string.

# Example of Concatenation:
str1 = "Hello, "
str2 = "world!"
result = str1 + str2
print(result)


# 7. What is the self keyword in a Class?
# The `self` keyword in a class refers to the instance of the class itself. It is used to access instance variables and methods.

# Example of the self keyword:
class Sample:
    def __init__(self, value):
        self.value = value

    def show(self):
        return self.value

obj = Sample(42)
print(obj.show())


# 8. What is File Handling?
# File handling refers to the operations performed on files, such as reading from, writing to, or modifying files in a program.

# Example of File Handling:
# Writing to a file
with open('example.txt', 'w') as f:
    f.write("Hello, world!")

# Reading from a file
with open('example.txt', 'r') as f:
    content = f.read()
    print(content)


# 9. What is NumPy?
# NumPy is a popular Python library for numerical computing. It provides support for large, multi-dimensional arrays
# and matrices, along with mathematical functions to operate on these arrays.

# Example of NumPy:
import numpy as np

# Creating a NumPy array
array = np.array([1, 2, 3, 4])
print(array)

# Performing a mathematical operation
array_squared = array ** 2
print(array_squared)