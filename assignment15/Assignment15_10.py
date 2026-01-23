# Write a lambda function using reduce() which accepts a list of numbers and returns 
# count 0f even elements
from functools import reduce

evenCount = lambda a : 1 if a % 2 == 0 else 0

def countEven(lst):
    iCnt = 0
    for no in lst:
        if no % 2 == 0:
            iCnt = iCnt + 1

    return iCnt

def reduceX(task, Elements):
    result = 0
    for no in Elements:
        result = result + task(no)
    
    return result


def main():
    lstLength  = int(input("Enter number of elements to enter : ")) 
    numbers = []
    for i in range(lstLength):
        numbers.append(int(input()))
    
    result1 = countEven(numbers)
    print("Count of even numbers is : ", result1, "   (using simple function)")

    result2 = reduceX(evenCount, numbers)
    print("Count of even numbers is : ", result2, "   (using custom reduce function)")

    result3 = reduce(lambda a, b: a + 1 if b % 2 == 0 else a, numbers, 0)
    print("Count of even numbers is : ", result3, "   (using lambda with reduce)")

if __name__ == "__main__":
    main()