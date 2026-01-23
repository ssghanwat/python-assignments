#lambda funnction to acept two number and return its minimum number


numMin = lambda a, b : a if a < b else b

def main():
    no1 = eval(input("Enter first number : "))
    no2 = eval(input("Enter second number : "))
    result = numMin(no1, no2)
    print("Minimum of two numbers is : ", result)


if __name__ == "__main__":
    main()