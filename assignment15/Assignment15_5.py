# Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.

from functools import reduce

MaxNum = lambda a,b : a if a > b else b

def maxNum(lst):
    temp = 0
    for i in lst:
        if i > temp:
            temp = i
    return temp

def ReduceX(task, Elements):
    Result = Elements[0]      
    for no in Elements[1:]:
        Result = task(Result, no)
    return Result


def main():
    total = 0   

    lstLength  = int(input("Enter number of elements to enter : ")) 
    numbers = []
    for i in range(lstLength):
        numbers.append(int(input()))

    result1 = ReduceX(MaxNum, numbers)
    print("Max number form list is : ", result1, "  (Using Custom reduce function)")

    result2 = maxNum(numbers)
    print("Max number form list is : ", result2, "   (using function)")

    result3 = reduce(lambda a,b : a if a > b else b, numbers)
    print("Maxnumber from list is : ",result3, "   (using built-in reduce)")

if __name__=="__main__":
    main()