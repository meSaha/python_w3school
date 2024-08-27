# Loop Through a list
# You can through the list items by using a for loop:
# Print all items in the list , one by one:
fruit_items = ["apple", "banana", "cherry"]
for x in fruit_items:
    print(x)

# Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
fruit_items = ["apple", "banana", "cherry"]
for i in range(len(fruit_items)):
    print(fruit_items[i])  # The iterable created in the example above is [0, 1, 2]

# Using a While Loop
# You can loop through the list items by using a while loop.
# Use the len() function to determine the length of the list,
# then start at 0 and loop your way through the list items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.

fruit_items = ["apple", "mango", "cherry"]
i = 0
while i < len(fruit_items):
    print(fruit_items[i])
    i = i + 1
