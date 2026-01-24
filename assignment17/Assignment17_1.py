# Create one module named as Arithmetic which contains 4 functions as 
# Add() for addition, Sub() for subtraction, Mult() for multiplication, and Div() 
# for division. All functions accept two parameters as numbers and perform the operation.
# Write a Python program which calls all the functions from the Arithmetic module by 
# accepting the parameters from the user

import Arithmetic

def main():
    no1 = eval(input("Enter first number: "))
    no2 = eval(input("Enter second number: "))

    result_add = Arithmetic.add(no1, no2)
    result_sub = Arithmetic.sub(no1, no2)
    result_mult = Arithmetic.mult(no1, no2)
    try:
        result_div = Arithmetic.div(no1, no2)
    except ValueError as e:
        result_div = str(e) 

    print("Addition : ", result_add)
    print("Subtraction : ", result_sub)
    print("Multiplication : ", result_mult)
    print("Division : ", result_div)

if __name__ == "__main__":
    main()  