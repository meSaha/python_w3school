# List comprehension offers a shorter syntax when you want to
# create a new list based on the values of an existing list.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for x in fruits:
    if "a" in x:
        new_list.append(x)

print(new_list)

# With list comprehension you can do all that with only one line of code:
fruits = ["Mango", "cherry", "Kiwi", "banna"]
newlists = [x for x in fruits if "a" in x]
print(newlists)