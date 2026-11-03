# num1, num2 are parameters that  are passed from start() function to sum() function
def sum(num1,num2):
    print(f"Sum is {num1+num2}")

def start():
    a = int(input("Enter first number "))
    b = int(input("Enter first number "))
    sum(a,b) # a and b are the arguments that carry value while calling the function 

start()