# Defining the Function , Syntax: def function_name():
def sum(): 
    # Always use indentation(space) to distinguish the code block that belongs to the function
    
    # The input funtion below is used to take integer or int as input from user and assign it 
    # to variables ie. a & b.

    #  Syntax: variable_name = data_type(input("sentence")) 
    a = int(input("Enter first number"))
    b = int(input("Enter second number"))

    # Displaying the result using print function, Syntax: print(f"sentence {variable_name or function_name}")
    # You can add or do arithmetic operations such as +,-,/,*,etc inside {} of a print statement
    # print is a built-in function 
    
    print(f"Sum is {a+b}")



# Calling the Function, Syntax: function_name()
sum()

