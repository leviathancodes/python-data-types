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
var = 'foo'

print(id(var)) ## Prints the address of 'foo' memory location

example_list = ["string", 1, True, [1,2,3,4]] ## This is an exaple of a list.  A lot like an array in JavaScript

example_list.append("new item") ## The append method works similarly to JS's `push` method.  Adds value to the end of an array

print(example_list)

# ------------------------------------------

## Strings

course = "Python Programming"

first_characther = course[0] ## You can use bracket notation to grab the index of a characther of a string
negative_index = course[-1] # This starts from the end of the string and goes backwards
course_slice = course[7:] ## This is how you slice part of a string in Python
course[2:7] # Selectiong a range
print(course_slice) 

## Escape Character

message = "Travis Scott said \"It's lit!\""
print(message)