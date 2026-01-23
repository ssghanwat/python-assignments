#lambda funnction to acept two number and return its higher number


numHigher = lambda a, b : a if a > b else b

def main():
    no1 = eval(input("Enter first number : "))
    no2 = eval(input("Enter second number : "))
    result = numHigher(no1, no2)
    print("Higher of two numbers is : ", result)


if __name__ == "__main__":
    main()