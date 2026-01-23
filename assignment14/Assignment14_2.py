#lambda funnction to acept one number and return its cube


numCube = lambda a : a * a * a

def main():
    no = eval(input("Enter number : "))
    result = numCube(no)
    print("Cube of number is : ", result)


if __name__ == "__main__":
    main()