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

""""Create Tuple With One Item"""
# To create a tuple with only one item, you have to add a comma after the item,
# otherwise Python will not recognize it as a tuple.
# One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

""""Tuple Items - Data Types"""
# Tuple items can be of any data type:
# String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)

# A tuple can contain different data types:
# A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

""""The tuple() Constructor"""
# It is also possible to use the tuple()
# constructor to make a tuple.
# Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thistuple)

""""Access Tuple Items"""
# You can access tuple items by referring to
# the index number, inside square brackets:
# Print the second item in the tuple:
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[1])

""""Negative Indexing"""
# Negative indexing means start from the end.
# -1 refers to the last item,
# -2 refers to the second last item etc.
# Print the last item of the tuple:
neg_tuple = ("apple", "banana", "cherry")
print(neg_tuple[-1])

""""Range of Indexes"""
# You can specify a range of indexes by specifying
# where to start and where to end the range.
# When specifying a range,
# the return value will be a new tuple with the specified items.
# Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[1:])
print(thistuple[2:])
print(thistuple[3:])

