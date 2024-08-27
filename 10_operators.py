# Python divides the operators in the following groups:
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

"""Python Arithmetic Operators"""

# Addition
x = 5
y = 3
print(x+y)

# Subtraction
x = 10
y = 5
print(x-y)

# Multiplication
x = 10
y = 2
print(x*y)

# Division
x = 12
y = 2
print(x/y)

# Modulus
x = 5
y = 2
print(x % y)

# Exponentiation
x = 2
y = 6
print(x ** y)  # same as 2*2*2*2*2*2

# Floor division
x = 15
y = 2
print(x // y)  # the floor division // rounds the result down to the nearest whole number


""" Assignment Operators"""
# Equal =
x = 5
print(x)

# += is called the addition assignment operator
a = 5
a += 3
print(a)

# subtraction assignment ( -= ) operator
b = 6
b -= 3
print(b)

# The symbol *= is called the multiplication assignment operator
c = 8
c *= 8
print(c)

# The symbol /= is called the Divide and assignment operator
d = 5
d /= 3
print(d)

# The symbol %= is called the Modulus And
e = 5
e %= 3
print(e)

# The symbol //= is called Divide(floor) AND:
f = 5
f //= 3
print(f)

# The symbol **= is called Exponent AND
g = 5
g **= 3
print(g)

# The symbol &= is called Performs Bitwise AND on operands
h = 5
h &= 3
print(h)

# The symbol |= is called Bitwise OR on operands and assign value to left operand
i = 5
i |= 3
print(i)

# The symbol ^= is called Bitwise xOR on operands and assign value to left operand
j = 5
j ^= 3
print(j)

# The symbol >>= is called Bitwise right shift on operands and assign value to left operand
k = 5
k >>= 3
print(k)

# the symbol <<= is called Bitwise left shift on operands and assign value to left operand
l = 5
l <<= 3
print(l)

"""Comparison Operators"""
# Comparison operators are used to compare two values:
# Equal ==
x = 5
z = 3
print(x == z)  # returns False because 5 is not equal to 3

# Not equal !=
y = 5
x = 3
print(y != x)  # returns True because 5 is not equal to 3

# Greater than >
z = 5
y = 3
print(z > y)   # returns True because 5 is greater than 3

# Less than <
i = 5
k = 3
print(i < k)   # returns False because 5 is not less than 3

# Greater than or equal to >=
x = 5
p = 3
print(x >= p)  # returns True because five is greater, or equal, to 3

# Less than or equal to <=
y = 5
k = 3
print(y <= k) # returns False because 5 is neither less than or equal to 3

"""Logical Operators"""
# Logical operators are used to combine conditional statements:
"""and : Returns True if both statements are true	x < 5 and  x < 10"""

x = 4
print(x > 3 and x < 10)  # returns True because 5 is greater than 3 AND 5 is less than 10


"""or : Returns True if one of the statements is true x < 5 or x < 4"""
z = 5
print(z > 3 or z < 4) # returns True because one of the conditions are
# true (5 is greater than 3, but 5 is not less than 4)

"""not : Reverse the result, returns False if the result is true	not(x < 5 and x < 10)"""
x = 5
print(not(x > 3 and x < 10)) # returns False because not is used to reverse the result

# Identity Operators
"""Identity operators are used to compare the objects, not if they are equal,
but if they are actually the same object, with the same memory location:"""

# is : Returns True if both variables are the same object eg: x is y
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference between "is not" and "!=": this comparison returns False because x is equal to y

"""Membership Operators"""
# Membership operators are used to test if a sequence is presented in an object:
# in: Returns True if a sequence with the specified value is present in
# the object: x in y
items = ["apple", "banana"]
print("banana" in items)
# # returns True because a sequence with the value "banana" is in the list
print("pineapple" not in items)
# returns True because a sequence with the value "pineapple" is not in the list

x = 5
x += 3
print(x)
