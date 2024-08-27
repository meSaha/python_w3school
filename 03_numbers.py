# There are three numeric types in Python:
# int
# float
# complex
# Variables of numeric types are created when you assign a value to them:

x = 1
y = 2.8
z = 1j
# use type()
print(type(x))
print(type(y))
print(type(z))

# You can convert from one type to another with the int(), float(), and complex() methods:
a = 12  # integer
b = 3.5  # float
c = 1j  # complex
d = "Display"  # string

# print(a)
# print(b)
# print(c)
# print(d)

# convert from int to float:
convert_int = float(a)
print(convert_int)
print(type(convert_int))

# convert from float to int:
convert_float = int(b)
print(convert_float)
print(type(convert_float))

# convert from int to complex:
convert_complex = complex(a)
print(convert_complex)
print(type(convert_complex))

# Random Number
# Python does not have a random() function to make a random number,
# but Python has a built-in module called random that can be used to make random numbers:
# Import the random module, and display a random number between 1 and 9:
import random

print(random.randrange(1, 10))
