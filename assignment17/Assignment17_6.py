#    *   *   *   *   *
#    *   *   *   *
#    *   *   *
#    *   *
#    * 


def printPattern(no):
    for i in range(no, 0, -1):
        for j in range(i):
            print("*", end = "   ")
        print()

def main():
    no = eval(input("Enter number: "))
    printPattern(no)

if __name__ == "__main__":
    main()  




