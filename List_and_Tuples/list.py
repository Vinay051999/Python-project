# list is used to store multiple items in a single variable
# list is one of 4 built-in data types in Python used to store collections of data
# list is created using square brackets
# list is ordered, changeable, and allows duplicate values
marks = [90, 80, 70, 60, 50]
print(marks)
print(type(marks))
print(marks[0])  # access list item using index
print(marks[1]) # access list item using index
student =["vinay", 25, 5.8, True] # list can store different data types
print(student)


# list slicing
# accessing a range of items in a list
# slicing is done using the colon (:) operator
# syntax: list[start:end]
# start is the index to start from (inclusive)
# end is the index to end at (exclusive)
# if start is omitted, it defaults to 0
# if end is omitted, it defaults to the length of the list
# negative indexing is also allowed
# example:
marks = [90, 80, 70, 60, 50]
print(marks[1:4]) # access list items from index 1 to 3

print(marks[:3]) # access list items from start to index 2
print(marks[-3:]) # access list items from index -3 to end
print(marks[-4:-1]) # access list items from index -4 to -2