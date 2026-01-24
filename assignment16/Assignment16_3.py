# Write a program which contains one function named Add() 
# which accepts two numbers from user and returns the addition of those two numbers.


def Add(num1, num2):
    return num1 + num2

def main():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    
    result = Add(number1, number2)
    print("Addition is:", result)

if __name__ == "__main__":
    main()