# Write a program which contains one function that accepts one number from user and 
# prints the pattern * * * * *.

def printPattern(num):
    for i in range(num):
        print("*", end=" ")  
    print()

def main():
    number = int(input("Enter a number: "))
    printPattern(number)

if __name__ == "__main__":
    main()