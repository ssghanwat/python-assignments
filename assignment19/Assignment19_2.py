# Write a program which contains one lambda function which accepts two parameters and returns its multiplication.

def MultNum(num1, num2):
    mult = lambda x, y : x * y
    return mult(num1, num2)

def main():
    no1 = int(input("enter first number : "))
    no2 = int(input("enter Second number : "))

    result = MultNum(no1, no2)
    print("Multiplication of number is : ", result)

if __name__ == "__main__":
    main()