#lambda funnction to acept two number and return true if its odd else return False 


numOdd = lambda a : True if a % 2 != 0 else False

def main():
    no1 = eval(input("Enter number : "))
    result = numOdd(no1)
    if result == True:
        print("Number is Odd ")
    else:
        print("number is not Odd")


if __name__ == "__main__":
    main()