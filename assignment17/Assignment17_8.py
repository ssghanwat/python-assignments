# 1
# 1   2
# 1   2   3
# 1   2   3   4
# 1   2   3   4   5

def printPattern(no):
    for i in range(1, no+1, 1):
        for j in range(1, i+1):
            print(j, end = "   ")
        print()

def main():
    no = eval(input("Enter number: "))
    printPattern(no)

if __name__ == "__main__":
    main()  


