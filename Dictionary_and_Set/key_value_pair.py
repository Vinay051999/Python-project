# key value pair in dictionary
# Example: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# In this example, 'name', 'age', and 'city' are keys, while 'Alice', 30, and 'New York' are their corresponding values.
# Keys must be unique and immutable (e.g., strings, numbers, or tuples), while values can be of any data type and can be duplicated.
#====================================================

#nested dictionary
# A nested dictionary is a dictionary that contains another dictionary (or dictionaries) as its values.
# we can access the values of the nested dictionary using the keys of the outer dictionary and the keys of the inner dictionary.
# we can also add, remove, and modify the values of the nested dictionary using the keys of the outer dictionary and the keys of the inner dictionary.
# we can also store different data types as values in the nested dictionary.
# Example:
info={
    "key" : "value",
    "name" : "vinay",
    "age" : 25,
    "is_adult" : True,
    "Subjects" : ["Maths", "Science", "English"],
    "topics": ("Python", "Java", "C++"),
    }
print(info)
print(type(info))
print(list(info.keys())) # get all keys in the dictionary
print(list(info.values())) # get all values in the dictionary
print(info["name"]) # access value using key
print(info["Subjects"]) # access value using key
print(info.items()) # get all key-value pairs in the dictionary
