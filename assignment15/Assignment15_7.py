# Write a lambda function using filter() which accepts a list strings and return list of strings 
# having length greater than 5

lenCheck = lambda a : a if len(a) > 5 else None

def chkLength(lst):
    result = []
    for str in lst:
        if len(str) > 5:
            result.append(str)
    return result

def filterX(task, Elements):
    Result = []
    for str in Elements:
        ret = task(str)
        if ret is not None:
            Result.append(str)
    return Result


def main():
    lstLength  = int(input("Enter number of Strings to enter : "))
    strList = []
    for i in range(lstLength):
        strList.append(input())

    print(strList)

    result1 = chkLength(strList)
    print("Strings greater than length 5 are : ", result1, "    (using simple function)")

    result2 = filterX(lenCheck, strList)
    print("Strings greater than length 5 are : ", result2, "    (using custom filter function)")
    
    
    

if __name__ == "__main__":
    main()