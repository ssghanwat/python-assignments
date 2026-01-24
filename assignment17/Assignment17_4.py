#  Write a program which accepts one number from the user and returns the addition of its factors.

def sumFactors(no):
    iSum = 0
    for i in range(1, no):
        if no % i == 0:
            print(i, end=" ")
            iSum = iSum + i
    return iSum

def main():
    no = eval(input("Enter number: "))
    result = sumFactors(no)
    print("Sum of factors is : ", result)

if __name__ == "__main__":
    main()  

