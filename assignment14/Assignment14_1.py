#lambda funnction to acept one number and return its square


numSquare = lambda a : a * a

def main():
    no = eval(input("Enter number : "))
    result = numSquare(no)
    print("Square of number is : ", result)


if __name__ == "__main__":
    main()