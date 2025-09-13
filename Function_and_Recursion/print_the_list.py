cities = ["bangalore", "mumbai", "delhi", "kolkata"] #list of strings
movies = ["avatar", "inception", "interstellar", "gravity"] #list of strings

#print(movies[0]. end="")

def print_the_list(list): # function definition
    print(len(list)) # print the length of the list 

print_the_list(cities) # function call with argument 
print_the_list(movies)

def print_list(list):# function definition
    for item in list:# iterate through the list 
        print(item, end=", ") #print each item in the list 
    print_list(cities) # function call with argument # output: bangalore, mumbai, delhi, kolkata,
