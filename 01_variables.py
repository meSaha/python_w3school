# Variable is a Container and store the data.
x = 5  # x is int value
y = "Raja"  # y is string value
print(x)
print(y)

# Casting:
# If you want to specify the data-type of a variable, this can be done with casting.
a = str(3)
b = int(3)
c = float(3)
print(a)
print(b)
print(c)

# Get the Type:
# You can get the data-type of a variable with the type() function.

x = 5
y = "John"
print(type(x))
print(type(y))

# Some legal variable names :
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:
x, y, z = "orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:
a = b = c = "Orange"
print(a)
print(b)
print(c)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc.
# Python allows you to extract the values into variables.
# This is called unpacking / Unpack a list:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awsome"
print(x + y + z)

# Exercise
print('Hello', 'World')

# Global Variables
# Variables that are created outside of a function
# (as in all of the examples in the previous pages) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.
# Create a variable outside of a function, and use it inside the function:

# x = "Awesome"


# def myfunc():
#     print("Python is " + x)
#
#
# myfunc()

# Create a variable inside a function, with the same name as the global variable:

g = "awesome"


def myfunc():
    g = "fantastic"
    print("Python is " + g)

    myfunc()


print("Python is " + g)


# The global Keyword:
# To create a global variable inside a function, you can use the global keyword:
# If you use the global keyword, the variable belongs to the global scope:


def myfun():
    global x
    x = "fantastic"


myfun()

print("Python is " + x)
