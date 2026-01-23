# Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.
from functools import reduce

numAdd = lambda a, b: a + b


def ReduceX(task, Elements):
    result = 0

    for no in Elements:
        result = task(result, no)

    return result

def main():

    lstLength  = int(input("Enter number of elements to enter : ")) 
    numbers = []
    for i in range(lstLength):
        numbers.append(int(input()))

    Result1 = ReduceX(numAdd, numbers)
    print("Addition of Numbers from list are : ",Result1, "   using user defined reduce")

    result2 = reduce(lambda a, b: a + b, numbers)
    print("Addition of Numbers from list are : ",result2, "   using built-in reduce")

    result3 = reduce(lambda a, b: a + b, numbers)
    print("Addition of Numbers from list are : ",result3, "   using built-in reduce")

if __name__=="__main__":
    main()


