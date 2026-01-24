# Write a program which displays first 10 even numbers on screen.

def printNum(no):
    for i in range(no+1):
        if i % 2 == 0:
            print(i, end=" ")   
    print()

def main():
    number = int(input("Enter a number: "))
    printNum(number)

if __name__ == "__main__":
    main()