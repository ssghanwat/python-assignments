# Write a program which accepts N numbers from the user and stores them into a list.
#  Return the maximum number from that list.

def maxEle(lst):
    temp = lst[0]
    for i in lst:
        if i > temp:
            temp = i
    return temp

def main():
    numbers = []
    no = int(input("Enter the number of elements : "))
    
    for num in range(no):
        num = int(input())
        numbers.append(num)

    result = maxEle(numbers)
    print("Max  of elements in list is : ", result)

if __name__=="__main__":
    main()
    
    