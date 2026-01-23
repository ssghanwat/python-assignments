#lambda funnction to acept two number and return true if its even else return False 


numEven = lambda a : True if a % 2 == 0 else False

def main():
    no1 = eval(input("Enter number : "))
    result = numEven(no1)
    if result == True:
        print("Number is even ")
    else:
        print("number is not even")


if __name__ == "__main__":
    main()