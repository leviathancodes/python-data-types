# Python Data Types

# students_count = 1000 # Integer, underscores are the common spacing convention in Python
# rating = 4.99 # Float
# is_published = False # Booleans are always uppercased
# course_name = "Python" # Can use single, double, or triple quotes

# # Initializing in Python
# ## Multiple variables can be initialized on the same line

# x = 1
# y = 2
# x, y = 1, 2

# # You can also set multiple variables to the same value

# x = y = 1

# ---------------------------------------------------------------

# print(type(students_count)) # Prints the data type, which will be 'int' 

# age: int = 20
# # age = "Python" ## The mypy linter shows an error here when you degine the variable with a data type like in line 21
# print(age)

# ---------------------------------------------------------------

# Mutable and Immutable Types

## When we run our program, Python interpreter will allocate some memory to store the string 'foo'. 
## Our 'var' variable is purely a label for that location in memory.
# var = 'foo'

# print(id(var)) ## Prints the address of 'foo' memory location

# example_list = ["string", 1, True, [1,2,3,4]] ## This is an exaple of a list.  A lot like an array in JavaScript

# example_list.append("new item") ## The append method works similarly to JS's `push` method.  Adds value to the end of an array

# print(example_list)

# ------------------------------------------

## Strings

# course = "Python Programming"

# first_characther = course[0] ## You can use bracket notation to grab the index of a characther of a string
# negative_index = course[-1] ## This starts from the end of the string and goes backwards
# course_slice = course[7:] ## This is how you slice part of a string in Python
# course[2:7] ## Selectiong a range
# print(course_slice) 

## Escape Characters
# \" double quote
# \' single quote
# \\ display a slash
# \n new line

# message = "Travis Scott said \"It's lit!\""
# print(message)

## You can make multi line strings using triple quotes
# triple_quote_message = """
# A lightning flash:
# between the forest trees
# I have seen water.
# """
# print(triple_quote_message)

## Formatted Strings

# first = "Lance"
# last = "Huddleston II"
# full = f"{first} {last}"
# another_example = f"{8/4*2} {len(first)}"
# # print(full, another_example)

# ## Useful string methods
# example = "   The world is a crazy place  "
# print(example.upper()) # Returns a copy of the string converted to uppercase.
# print(example.lower()) # Returns a copy of the string converted to lowercase.
# print(example.title()) # Return a version of the string where each word is titlecased.
# print(example.strip()) # Return a copy of the string with leading and trailing whitespace remove.

# print(example.find("The")) # Find the beginning index of a substring in a string
# print(example.replace("crazy", ""))
# print("world" in example)
# print("world" not in example)


# decimal_string = "12345"
# print(decimal_string.isdecimal()) # Checks is a string is only comprised of decimals

# -------------------------------------------------

## Numbers and Number Methods

x = 10
print(bin(x)) # Return the binary representation of an integer.

x = 10 + 3 # 13
x = 10 - 3 # 7
x = 10 * 3  # 30
x = 10 / 3 # 3.3333333
x = 10 // 3 # Returns whole number etc 10 // 3 = 3
x = 10 % 3 # Returns remainder
x = 10 ** 3 # Returns number to the power of a number ex. 10 ** 3 = 1000

# The following two statements do the same thing

x = x + 1
x += 1