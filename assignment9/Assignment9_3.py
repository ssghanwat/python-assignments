#Write a program which contains one function named as numSquare()
#that gives square of the number on console


def numSquare(a):
    return a * a

def main():

    no = int(input("Enter a number: "))
    
    if no >= 0:
        result = numSquare(no)
        print("Square of the number is:", result)
    else:
        print("Please enter a non-negative number.")
                
if __name__ == "__main__":
    main()