# function  are used to encapsulate a piece of code that performs a specific task and can be reused multiple times throughout a program.
# function is defined using the def keyword followed by the function name and parentheses ().
# function can take parameters (also called arguments) which are values passed to the function when it is called.
# function can return a value using the return keyword. If no return statement is used, the function will return None by default. 
# Example:

# function definition 
def calculater_num(num1, num2):# function parameters
    sum = num1 + num2 # function body
    print(sum)
    return sum # function return value
calculater_num(10, 20) # function call with arguments
result = calculater_num(30, 40) # function call with arguments
print(result) # print the return value of the function

def print_hello():
    print("Hello, World!")
print_hello() # function call without arguments
print_hello() # function call without arguments
print_hello() # function call without arguments