# Sort List Alphanumerically
# List objects have a sort() method that
# will sort the list alphanumerically, ascending, by default:
# Sort the list alphabetically:


this_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list.sort()
print(this_list)

# Sort the list numerically:
this_list_num = [100, 50, 65, 82, 23]
this_list_num.sort()
print(this_list_num)

"""Sort Descending"""
# To sort descending, use the keyword argument reverse = True:
# Sort the list descending:
this_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list.sort(reverse=True)
print(this_list)

# Sort the list descending:
this_list_num = [100, 50, 65, 82, 23]
this_list_num.sort(reverse=True)
print(this_list_num)

