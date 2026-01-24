#Accept number from user and return addition of digits in that number

def sumDigits(no):
    iDigit = 0
    iSum = 0

    while no > 0:
        iDigit = no % 10 
        iSum = iSum + iDigit
        no = no // 10
    
    return iSum


def main():
    no = eval(input("Enter number: "))
    result = sumDigits(no)
    print("Sum of digits are : ", result)

if __name__ == "__main__":
    main()  

