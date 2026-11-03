# num1, num2 are parameters that  are passed from start() function to sum() function
def sum(num1,num2):
    # return function just reutrns the value of a variable to where the function (eg. sum()) is called 
    # return is a built-in function
    return num1+num2

def start():
    a = int(input("Enter first number "))
    b = int(input("Enter first number "))
    print(f" The sum is {sum(a,b)}") # a and b are the arguments that carry value while calling the function 

start()