#Write a program which contains one function named as numDivisible()
#that that checks is it divisible by 3 and 5


def numDivisible(a):
    if a % 3 ==0 and a % 5 ==0:
        return True

def main():

    no = int(input("Enter a number: "))
    
    if no >= 0:
        result = numDivisible(no)
        if result == True:
            print("number is divisible by 3 and 5 :")
        else:
            print("number is not divisible by 3 and 5 :")
    else:
        print("Please enter a non-negative number.")
                
if __name__ == "__main__":
    main()