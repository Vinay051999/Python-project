# set is one of the 4 built-in data types in Python used to store collections of data
# set is created using curly brackets {}
# set is unordered, unchangeable*, and unindexed
# set does not allow duplicate values
# set is used to store multiple items in a single variable
# set is unordered, so we cannot access items using index
# set is unchangeable, so we cannot change items in a set, but we can add new items
# set does not allow duplicate values, so if we try to add a duplicate value, it
# will be ignored
# Example:
collections={1,2,3,2,1,"hello","world","world",4}
print(collections)
print(type(collections)) 
print(len(collections)) # get the number of items in the set

# empty set
# we cannot create an empty set using {}
empty_set = set()
empty_set.add(1) # add item to the set
empty_set.add(2) # add item to the set
empty_set.add(3) # add item to the set

print(empty_set)