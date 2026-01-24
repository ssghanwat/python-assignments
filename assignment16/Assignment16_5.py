# Write a program which displays 10 to 1 on screen.
def printRev(num):
    result = []
    for i in range(num, 0 ,-1):
        result.append(i)
    return result   

def main():
    number = int(input("Enter a number: "))
    revList = printRev(number)
    for no in revList:
        print(no, end = " ")
    print()

if __name__ == "__main__":
    main()