# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
# Loop through the letters in the word "banana":
for x in "banana":
    print(x)

for y in "Mango":
    print(y)

for z in "biriyani":
    print(z)


# String Length
# To get the length of a string, use the len() function.
# The len() function returns the length of a string:
show = "Hello Python!"
# "H e l l o P y t h o n !"
#  0 1 2 3 4 5 6 7 8 9 10 11 # space also count
print(len(show))  # 13

# Check String
# To check if a certain phrase or character is present in a string,
# we can use the keyword in.
# Check if "free" is present in the following text:
text = "The best things in life are free!"
print("free" in text)
print("now" in text)

# Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes,'free is Present")


# Check if NOT
# To check if a certain phrase or character is NOT present in a string,
# we can use the keyword not in.
# Check if "expensive" is NOT present in the following text:
text_line = "The best things in life are free!"
print("expensive" not in text_line)

x = 'Welcome'
print(x[3])