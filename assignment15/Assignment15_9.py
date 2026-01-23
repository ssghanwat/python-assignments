# Write a lambda function using reduce() which accepts a list of numbers and returns 
# product of all elements
from functools import reduce

prodNum = lambda a, b : a * b

def numProd(lst):
    result = 1
    for i in lst:
        result = i * result
    
    return result

def reduceX(task, elements):
    result = 1
    for no in elements:
        result = task(result, no)
        
    return result


def main():
    lstLength  = int(input("Enter number of elements to enter : ")) 
    numbers = []
    for i in range(lstLength):
        numbers.append(int(input()))
    
    result1 = numProd(numbers)
    print("product of all elements are : ", result1, "   (usign simple function)")

    result2 = reduceX(prodNum, numbers)
    print("product of all elements are : ", result2, "   (usign custom reduce function)")

    result3 = reduce(lambda a, b: a * b, numbers)
    print("product of all elements are : ",result3, "   using built-in reduce")

if __name__ == "__main__":
    main()