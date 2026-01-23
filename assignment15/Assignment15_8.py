# Write a lambda function using filter() which accepts a list of numbers and returns 
# list of numbers divisible by 3 and 5


numDivL = lambda a : a if a % 3 == 0 and a % 5 == 0 else None

def numDiv(lst):
    divLst = []
    for no in lst:
        if no % 3 == 0 and no % 5 == 0:
            divLst.append(no)
    return divLst

def filterX(task, Elements):
    result = []

    for no in Elements:
        if no % 3 == 0 and no % 5 == 0:
            ret = numDivL(no)
            result.append(no)
    return result
    

def main():
    lstLength  = int(input("Enter number of elements to enter : ")) 
    numbers = []
    for i in range(lstLength):
        numbers.append(int(input()))

    result1 = numDiv(numbers)
    print("Numbers Divisble by 3 and 5 are : ", end = " ")
    for no in result1:
        print(no, "    (using simpple function)")
    print(end=" ")

    result2 = filterX(numDivL, numbers)
    print("Numbers Divisble by 3 and 5 are : ", end = " ")
    for no in result2:
        print(no, "    (using custom filter function)")
    print(end=" ")
    
    result3 = list(filter(lambda a : (a % 3 == 0 and a % 5 == 0) , numbers))
    print("Numbers Divisble by 3 and 5 are : ", * result3)
    print(end=" ")

if __name__=="__main__":
    main()