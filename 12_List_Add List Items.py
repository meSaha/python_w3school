# Append Items
# To add an item to the end of the list, use the append()method:
fruit_items = ["apple", "banana", "cherry"]
fruit_items.append("orange")
print(fruit_items)

# Insert Items
# To insert a list item at a specified index, use the insert() method.
fruit_items = ["apple", "banana", "cherry"]
fruit_items.insert(1, "orange")
print(fruit_items)

# Extend List
# To append elements from another list to the current list, use the extend() method.
# The elements will be added to the end of the list.
fruit_items = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
fruit_items.extend(tropical)
print(fruit_items)


mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')
print(mylist[1])