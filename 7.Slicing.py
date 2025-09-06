# Slicing in Python
# Slicing allows you to extract a portion of a string by specifying a start and end index.
# The syntax for slicing is string[start:end], where 'start' is the index to begin  the slice (inclusive) and 'end' is the index to end the slice (exclusive).
# You can also specify a step value using string[start:end:step], which determines the increment between each index in the slice.
# If 'start' is omitted, it defaults to the beginning of the string. If 'end' is omitted, it defaults to the end of the string. If 'step' is omitted, it defaults to 1.
# Example string    
String="I Am Vinay" 
slice1=String[0:5] # Slicing from index 0 to 4 (5 is exclusive)
print("Slice from index 0 to 4:", slice1) #printing the sliced string
slice2=String[5:] # Slicing from index 5 to the end of the string
print("Slice from index 5 to end:", slice2) #printing the sliced string 
#output of index 5 to end: Vinays
slice3=String[2:8] # Slicing from index 3 to 7 (8 is exclusive)
print( slice3) #printing the sliced string