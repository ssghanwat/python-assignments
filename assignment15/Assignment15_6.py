# Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element.

from functools import reduce

minNum = lambda a,b : a if a < b else b

def minNum(lst):
    temp = lst[0]
    for i in lst:
        if i < temp:
            temp = i
    return temp

def ReduceX(task, Elements):
    Result = Elements[0]      
    for no in Elements:
        Result = task(Result, no)
    return Result

def main(): 

    lstLength  = int(input("Enter number of elements to enter : ")) 
    numbers = []
    for i in range(lstLength):
        numbers.append(int(input()))

    result1 = ReduceX(minNum, numbers)
    print("Minimum number form list is : ", result1, "  (Using Custom reduce function)")

    result2 = minNum(numbers)
    print("Minimum number form list is : ", result2, "   (using function)")

    result3 = reduce(lambda a,b : a if a < b else b, numbers)
    print("Minimum number form list is : ",result3, "   (using built-in reduce)")

if __name__=="__main__":
    main()