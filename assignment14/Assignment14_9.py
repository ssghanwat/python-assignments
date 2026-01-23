#lambda funnction to acept two number and return it Multiplication


numMult = lambda a, b : a * b

def main():
    no1 = eval(input("Enter first number : "))
    no2 = eval(input("Enter second number : "))

    result = numMult(no1, no2)
    print("Multiplication of 2 number is :", result)


if __name__ == "__main__":
    main()