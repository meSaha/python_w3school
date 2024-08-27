"""Use the copy() method"""
# You can use the built-in List method copy() to copy a list.
# Make a copy of a list with the copy() method:
this_list = ["apple", "cherry", "banana"]
my_list = this_list.copy()
print(my_list)

"""Use the list() method"""
# Another way to make a copy is to use the built-in method list().
# Make a copy of a list with the list() method:
this_list = ["apple", "banana", "cherry"]
my_list = list(this_list)
print(my_list)

"""Use the slice Operator"""
# You can also make a copy of a list by using the : (slice) operator.
# Make a copy of a list with the : operator:
this_list = ["apple", "banana", "cherry"]
my_list = this_list[:]
print(my_list)


"""Join Two Lists"""

# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.\
# Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)


# use the extend() method, where the purpose is to add elements from one list to another list:
# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)