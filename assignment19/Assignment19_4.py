#####################################################################################
# 4. Write a program which contains filter(), map() and reduce() in it.
#  Python application which contains one list of numbers.
#  List contains the numbers which are accepted from user.
#  Filter should filter out all such numbers which are even.
#  Map function will calculate its square.
#  Reduce will return addition of all that numbers.

# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204

#######################################################################################

from functools import reduce

def filterLst(lstElement):
    if lstElement % 2 == 0:
        return True
    else:
        return False
    
def mapList(lstElement):
    return lstElement ** 2

def reduceList(lstElement1, lstElement2):
    return lstElement1 + lstElement2

def main():
    numbers = []
    no = int(input("enter number of elements : "))

    for i in range(no):
        elem = int(input())
        numbers.append(elem)
    
    fltr1 = list(filter(lambda x : x if x %2 == 0 else None, numbers))
    filterX = list(filter(filterLst, numbers))
    print("List after filter : ",filterX)

    map1 = list(map(lambda x : x ** 2, filterX))
    mapX = list(map(mapList, filterX))
    print("List after map    : ",mapX)

    redc1 = reduce(lambda x, y : x * y, mapX)
    reduceX = reduce(reduceList, mapX)
    print("Output of reduce  : ",reduceX)

    
 
if __name__ == "__main__":
    main()