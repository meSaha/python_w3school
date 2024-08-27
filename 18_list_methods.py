# Python has a set of built-in methods that you can use on lists.
my_number = [4, 3, 5]
my_number.sort()
print(my_number)

# Clear ():
item = [1, 2, 3]
item.clear()
print(item)

# append():
item_1 = [1, 2, 3]
item_1.append(4)
print(item_1)

# count()
points = [1, 1, 1, 2, 3]
x = points.count(1)
print(x)

# extend([4])
digits = [1, 2, 3, 4]
digits.extend([5])
print(digits)

# insert()
my_bucket = [1, 2, 3]
my_bucket.insert(3, 4)
print(my_bucket)

# index()
my_list = [1, 2, 3]
x = my_list.index(2)
print(x)

# remove()
my_list = [1, 2, 3]
my_list.remove(2)
print(my_list)

# pop()
my_list = [1, 2, 3]
my_list.pop()
print(my_list)

# reverse()
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)

# copy()
my_list = [1, 2, 3]
my_list.copy()
print(my_list)

# len()
my_list = [1, 2, 3]
y = len(my_list)
print(y)

# min()
my_list = min(1, 2, 3)
print(my_list)

# max()
my_list = max(1, 2, 3)
print(my_list)


