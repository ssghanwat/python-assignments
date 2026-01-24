# Write a program which accepts N numbers from the user and stores them into a list. 
# Return the minimum number from that list.

def minEle(lst):
    temp = lst[0]
    for i in lst:
        if i < temp:
            temp = i
    return temp

def main():
    numbers = []
    no = int(input("Enter the number of elements : "))
    
    for num in range(no):
        num = int(input())
        numbers.append(num)

    result = minEle(numbers)
    print("Min  of elements in list is : ", result)

if __name__=="__main__":
    main()
    
    