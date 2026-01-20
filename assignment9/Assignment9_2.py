#Write a program which contains one function named as chkGreater()
#that accepts 2 parameters and prints greater number on console


def chkGreater(a,b):
    if a > b:
        return True
    else:
        return False
    
def main():
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))

    result = chkGreater(no1, no2)

    if result == True:
        print("First number is greater that is :", no1)
    else:
        print("Second number is greater that is :", no2)
        
if __name__ == "__main__":
    main()