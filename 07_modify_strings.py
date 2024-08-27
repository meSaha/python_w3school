# Upper Case
# The upper() method returns the string in upper case:
a = "hello python programming"
print(a.upper())

# Lower Case
# The lower() method returns the string in lower case:
b = "Hello Python Programming"
print(b.lower())

# Remove Whitespace
# Whitespace is the space before and/or after the actual text,
# and very often you want to remove this space.
# The strip() method removes any whitespace from the beginning or the end:
z = "Hello Programming"
print(z.strip())

# Replace String
# The replace() method replaces a string with another string:
w = "Hello Python!"
print(w.replace("Hello", "Practice"))

# Split String
# The split() method returns a list where the text between
# the specified separator becomes the list items.
city_name = "Denmark,France"
print(city_name.split(","))

# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.
# Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)

# To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# Escape Characters
# Single Quote
text = 'It\'s alright'
print(text)

# Backslash
text_2 = "This will insert one \\(Backslash)."
print(text_2)

# New Line
text_3 = "Hello\nPython Programming"
print(text_3)

# Tab
text_4 = "Hello\tPython Pragramming"
print(text_4)

# Backspace
# This example erases one character (backspace):
text_5 = "Hello \bProgramming"
print(text_5)