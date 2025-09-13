# recurtion function to calculate factorial of a number
# factorial of n is n * factorial of (n-1)
# factorial of 0 is 1
# factorial of 1 is 1
# factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120
# factorial of 6 is 6 * 5 * 4 * 3 * 2 * 1 = 720

def show(n): # function definition
    if(n==0): # base case 
        return # return statement to exit the function 
    print(n) # print the value of n
     # recursive case is used to call the function itself with a modified argument 
    show(n-1) # function call with argument n-1 
show(5) # function call with argument 5 # output: 5 4 3 2 1