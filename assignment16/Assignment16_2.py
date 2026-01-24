# Write a program which contains one function named ChkNum() 
# which accepts one parameter as number.If number is even then it 
# should display "Even number" otherwise display "Odd number" on console.


def ChkNum(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
def main():
    number = int(input("Enter a number: "))
    
    result = ChkNum(number) 
    if result == True:
        print("Even number")
    else:
        print("Odd number")

if __name__ == "__main__":
    main()