import math


print("Hello World!!!")

if 5 > 2:
    print("Five is greater than two")

x = 5

y = "Hello World!!!"

# We use # as comment symbol in Python!!!
# Can I use it for muitiple lines??
"""
  Well, can be written like this
"""

print(x)  # type int

print(y)  # type str (String)

x = str(3)  # re-assignment

y = int(4)

z = float(5)

print(x)

print(y)

print(z)

print(int(math.pow(2, 2)))  # Casing

print(type(x))  # <class 'str'>

print(type(y))  # <class 'int'>

print(type(z))  # <class 'float'>

print(type(math.pow(2, 2)))  # <class 'float'> No double in Python lol

s = "John", "John"  # Single and Double Quotes have no difference in Python

a = 4

A = "Sally"  # Case sensitive, will not overwrite

print(a)  # 4

print(A)  # Sally

var = "John"  # Same as Java, naming rule is alphabet chars, numbers and underscore

Var = "john"

VAR = "jOHN"

print(var + Var + VAR, x)  # but + can only concat String to String
# To print different types together, use ,

x, y, z = "x", "y", "z"  # Multiple assignments

x, y, z = "x", 20, "z"  # Works with different types as well

x = y = z = "All as One"  # One value to Multiple Variables

print(bool(x == y == z))  # Can determine multiple statements in one

fruits = ["apple", "orange", "banana"]  # Collection(Array)

x, y, z = fruits  # Unpack a Collection

print(x, y, z)  # apple orange banana
