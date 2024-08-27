# The remove() method removes the specified item.
# Remove "banana":
fruit_items = ["apple", "banana", "cherry"]
fruit_items.remove("banana")
print(fruit_items)
# fruit_items.append("mango")
# fruit_items.insert(1, "mango")
# print(fruit_items)

# Remove Specified Index
# The pop() method removes the specified index.
fruit_items = ["apple", "banana", "cherry"]
fruit_items.pop(2)
print(fruit_items)

# If you do not specify the index,
# the pop() method removes the last item.
fruit_items = ["apple", "banana", "cherry"]
fruit_items.pop()
print(fruit_items)

# The del keyword also removes the specified index:
# Remove the first item:
# If the specified index.
fruit_items = ["apple", "banana", "cherry"]
del fruit_items[1]
print(fruit_items)

# The del keyword can also delete the list completely.
# If you do not specify the index
# Delete the entire list:
fruit_items = ["apple", "banana", "cherry"]
del fruit_items

# Clear the List
# The clear() method empties the list.
# The list still remains, but it has no content.
fruit_items = ["apple", "banana", "cherry"]
fruit_items.clear()
print(fruit_items)
