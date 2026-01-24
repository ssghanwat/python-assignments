# 1   2   3   4   5
# 1   2   3   4   5   
# 1   2   3   4   5
# 1   2   3   4   5
# 1   2   3   4   5

def printPattern(num):
    for i in range(1,num+1):
        for j in range(1, num+1):
            print(j, end = "   ")
        print()


def main():
    no = eval(input("Enter number: "))
    printPattern(no)

if __name__=="__main__":
    main()





