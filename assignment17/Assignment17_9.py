#Accept number from user and return number of digits in that number

def cntDigits(no): 
    iCnt = 0
    iDigit = 0

    while no > 0:
        iDigit = no % 10  
        iCnt = iCnt + 1   
        no = no // 10     
    
    return iCnt


def main():
    no = eval(input("Enter number: "))
    result = cntDigits(no)
    print("Count of digits are : ", result)

if __name__ == "__main__":
    main()  

