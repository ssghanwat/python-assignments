# Write a program which contains one function that accepts one number from user and 
# returns true if number is divisible by 5, otherwise return false.

def chkDiv(num):
    if num % 5 == 0:
        return True
    else:
        return False  

def main():
    number = int(input("Enter a number: "))
    result = chkDiv(number)
    if result == True:
        print("number is dividible by 5")
    else:
        print("number is not dividible by 5")

if __name__ == "__main__":
    main()