# In programming, data type is an important concept.
# Variables can store data of different types,and different types can do different things.
# Python has the following data types built-in by default, in these categories:
"""
ext Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memory view
None Type:	NoneType
"""

# Print the data type of the variable x:
# x = 5
# print(type(x))

# String:
text = "Hello World"
print(text)
# display the data type of x:
print(type(text))

# Integer:
number = 20
# Display Number:
print(number)
# Display the data type of number:
print(type(number))

# Float
point_num = 20.5
# Display Float Number
print(point_num)
# Display the data type of number:
print(type(point_num))

# Complex
complex_number = 1j
print(complex_number)
# Display the data type of Complex Number
print(type(complex_number))

# List
item = ["Apple", "Mango", "Chili"]
print(item)
# Display the data type of List
print(type(item))

# Tuple
list_item = ("Vivo", "Samsung", "RedMi")
print(list_item)
# Display the data type of Tuple
print(type(list_item))

# Dictionary
my_item = {"name": "Raja", "age": "33", "Job": "Python Developer"}
print(my_item)
# Display the data type of Dictionary
print(type(my_item))

# Range
target = range(5)
print(target)
# Display the data type of Range
print(type(target))

# set
bucket_list = {"Mango", "Cherry", "apple"}
print(bucket_list)
# Display the data type of Set
print(type(bucket_list))

# Bool / Boolean
x = True
print(x)
# Display the data type of bool / boolean
print(type(x))

# Frozenset
fruit_items = frozenset({"apple", "banana", "cherry"})
print(fruit_items)
# Display the data type of Frozenset
print(type(fruit_items))

# Bytes
txt = b"Hello"
print(txt)
# Display the data type of Bytes
print(type(txt))

# Byte array
byte_array = bytearray(4)
print(byte_array)
# Display the data type of byte array
print(type(byte_array))

# Memory view
view_memory = memoryview(bytes(5))
print(view_memory)
# Display the data type of Memory View
print(type(view_memory))

# None Type
which_type = None
print(which_type)
# Display the data type of Memory View
print(type(which_type))


# Nxt Python Numbers