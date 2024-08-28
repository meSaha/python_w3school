"""Tuple"""
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# Create a Tuple:
mytuple = ("apple", "banana", "cherry")
print(mytuple)

"""Tuple Items"""
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0],
# the second item has index [1] etc.

"""Ordered"""
# When we say that tuples are ordered, it means that the items have a defined order,
# and that order will not change.

"""Unchangeable"""
# Tuples are unchangeable, meaning that we cannot change,
# add or remove items after the tuple has been created.

"""Allow Duplicates"""
# Since tuples are indexed, they can have items with the same value:
# Tuples allow duplicate values:
this_tuple = ("lemon Tea", "Masala Tea", "Ginger Tea", "Lemon Tea")
print(this_tuple)
print(type(this_tuple))

"""Tuple Length"""
# To determine how many items a tuple has, use the len() function:
# Print the number of items in the tuple:
this_tuple = ("lemon Tea", "Masala Tea", "Ginger Tea", "Lemon Tea")
print(len(this_tuple))