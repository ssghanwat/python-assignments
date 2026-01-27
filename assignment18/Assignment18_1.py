#Write a program which accepts N numbers from the user and stores them into a list.
#  Return the addition of all elements from that list.

def lstSum(lst):
    iSum = 0
    for i in lst:
        iSum = iSum + i

    return iSum

def main():
    numbers = []
    no = int(input("Enter the number of elements : "))
    
    for num in range(no):
        num = int(input())
        numbers.append(num)

    result = lstSum(numbers)
    print("Sum of elements in list is : ", result)

if __name__=="__main__":
    main()
    
    