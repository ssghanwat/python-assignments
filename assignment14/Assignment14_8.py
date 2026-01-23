#lambda funnction to acept two number and return it addition


numAdd = lambda a, b : a + b

def main():
    no1 = eval(input("Enter first number : "))
    no2 = eval(input("Enter second number : "))

    result = numAdd(no1, no2)
    print("Addition of 2 number is :", result)


if __name__ == "__main__":
    main()