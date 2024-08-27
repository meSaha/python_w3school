# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python
# used to store collections of data, the other 3 are Tuple, Set, and Dictionary
# all with different qualities and usage.
# Lists are created using square brackets:
"""create a List"""
this_list = [" Mango", "Apple", "Cherry"]
print(this_list)

# List Items
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

"""Ordered"""
# When we say that lists are ordered, it means that the items have a defined order,
# and that order will not change.

# If you add new items to a list,
# the new items will be placed at the end of the list.

"""Changeable"""
# The list is changeable,
# meaning that we can change, add, and remove
# items in a list after it has been created.

# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:
# Lists allow duplicate values:
items_list = ["apple", "banana", "cherry", "apple", "cherry"]
print(items_list)

# List Length
# To determine how many items a list has, use the len() function:
items_list = ["apple", "banana", "cherry", "apple", "cherry"]
print(len(items_list))

# List Items - Data Types
# List items can be of any data type:
# Example : String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# A list can contain different data types:
# A list with strings, integers and boolean values:
list_1 = ["abc", 34, True, 40, "male"]
print(list_1)

# type()
# From Python's perspective, lists are defined as objects with the data type 'list':
# <class 'list'>
# What is the data-type of a list?
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.
# Using the list() constructor to make a List:
this_list = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(this_list)

mylist = ['apple', 'banana', 'banana', 'cherry']
print(mylist[2])

# List items are indexed-and you can access them by referring to the index number:
this_list_1 = ["apples", "banana", "cherry"]
print(this_list_1[1])


# Negative-Indexing
# Negative indexing means start from the end
# -1 refers to the last item
# -2 refers to the second last item etc.
this_list_1 = ["apples", "banana", "cherry"]
print(this_list_1[-1])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
this_list_2 = ["apples", "Orange", "Kiwi", "melon", "Mango", "banana", "cherry"]
print(this_list_2[2:5])

# This example returns the items from the beginning to, but NOT including, "kiwi":
this_list_2 = ["apples", "Orange", "Kiwi", "melon", "Mango", "banana", "cherry"]
print(this_list_2[:4])
# This will return the items from index 0 to index 4.
# Remember that index 0 is the first item, and index 4 is the fifth item
# Remember that the item in index 4 is NOT included

# By leaving out the end value, the range will go on to the end of the list:
# This example returns the items from "cherry" to the end:
this_list_2 = ["apples", "Orange", "Kiwi", "melon", "Mango", "banana", "cherry"]
print(this_list_2[2:])

"""Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the list:"""
# This example returns the items from "Orange"(-4) to, but NOT including "mango"(-1):
this_list_2 = ["apples", "Orange", "Kiwi", "melon", "Mango", "banana", "cherry"]
print(this_list_2[-4:-1])

# Check if Item Exists
# To determine if a specified item is present in a list use the in Keyword:
# check if "apple" is present in the list :
this_list_2 = ["apples", "Orange", "Kiwi", "melon", "Mango", "banana", "cherry"]
if "apples" in this_list_2:
    print("Yes, 'apple', is in the fruits list")

mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
print(mylist[1:4])

"""Change Item value"""
# To change the value of a specific item, refer to the index number:
# change the second item
this_item = ["Delhi", "Mumbai", "Kolkata"]
this_item[1] = "Chennai"
print(this_item)

# Change a Range of Item Values
""" To change the value of items within a specific range,
 define a list with the new values, and refer to the range of index numbers where you want to insert the new values:"""
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
this_list_3 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
this_list_3[1:3] = ["blackcurrant", "watermelon"]
print(this_list_3)


# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:
# Insert "Watermelon" as the third item :

this_item_1 = ["Delhi", "Mumbai", "Kolkata"]
this_item_1.insert(2, "Siliguri")
print(this_item_1)

mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2])