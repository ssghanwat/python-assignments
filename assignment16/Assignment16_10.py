
def chkLength(str):
    iCnt = 0
    for i in range(len(str)):
        iCnt = iCnt + 1
    return iCnt

def main():
    string = input("Enter a string: ")
    result = chkLength(string)
    print("Length of the string is:", result)

if __name__ == "__main__":
    main()