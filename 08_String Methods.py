# String capitalize() Method
# The capitalize() method returns a string where the first character is upper case,
# and the rest is lower case.
your_text = "hello python programming"
show = your_text.capitalize()
print(show)


# String center() Method
# Print the word "banana", taking up the space of 30 characters,
# with "banana" in the middle:
# The center() method will center align the string,
# using a specified character (space is default) as the fill character.
fruit = "banana"
basket_1 = fruit.center(30)
basket_2 = fruit.center(40, "O")
print(basket_1)
print(basket_2)

# String count() Method
# The count() method returns the number of times
# a specified value appears in the string.
text = "I love apples, apple are my favorite fruit"
show_display = text.count("favorite")
print(show_display)

# String endswith() Method
txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)

# endswith More Example
# Check if position 5 to 11 ends with the phrase "my world.":
txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)

# String find() Method
# The find() method finds the first occurrence of the specified value.
find_txt = "Hello, Welcome to my Python Program"
find_result = find_txt.find("Welcome")
print(find_result)

# String startswith() Method
# The startswith() method returns True if the string
# starts with the specified value, otherwise False.
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

