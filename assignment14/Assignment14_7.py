#lambda funnction to acept two number and return true if its divisible by 5 


numDiv = lambda a : True if a % 5 == 0 else False

def main():
    no1 = eval(input("Enter number : "))
    result = numDiv(no1)
    if result == True:
        print("Number is Divisible by 5 ")
    else:
        print("number is not Divisible by 5")


if __name__ == "__main__":
    main()