#######################################################################################

# Write a program which contains filter(), map() and reduce() in it.
# Python application which contains one list of numbers.
# List contains the numbers which are accepted from user. 
# Filter should filter out all prime numbers. 
# Map function will multiply each number by 2. 
# Reduce will return Maximum number from that numbers. 
# (You can also use normal functions instead of lambda functions).

# Input List = [2, 70, 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62

#######################################################################################

from functools import reduce

def filterPrime(no):
    if no < 2:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True

def mapMult(no):
    no = no * 2
    return no

def reduceMax(no1, no2):
    if no1 > no2:
        return no1
    else:
        return no2
    

def main():
    numbers = []
    no = int(input("enter number of elements : "))

    for i in range(no):
        elem = int(input())
        numbers.append(elem)

    filterX = list(filter(filterPrime, numbers))
    print("List after filter : ",filterX)

    mapX = list(map(mapMult, filterX))
    print("List after map    : ", mapX)

    reduceX = reduce(reduceMax, mapX)
    print("Output of reduce  : ",reduceX)

if __name__ == "__main__":
    main()