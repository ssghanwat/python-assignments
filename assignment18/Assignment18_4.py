# Write a program which accepts N numbers from the user and stores them into a list.
# Accept one more number from the user and return the frequency of that number from the list.

def numFreq(lst, no):
    iCnt = 0
    for i in lst:
        if i == no:
            iCnt = iCnt + 1
    return iCnt
    
def main():
    numbers = []
    numEle = int(input("Enter the number of elements : "))
    
    for num in range(numEle):
        num = int(input())
        numbers.append(num)

    no = int(input("enter number to count frequency : "))

    result = numFreq(numbers, no)
    print("frequency of the number in elements in list is : ", result)

if __name__=="__main__":
    main()
    
    