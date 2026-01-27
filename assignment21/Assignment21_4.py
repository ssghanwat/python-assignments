###################################################################################################

# Design a Python application that creates two threads.

# Thread 1 should compute the sum of elements from a list.

# Thread 2 should compute the product of elements from the same list.

# Return the results to the main thread and display them.

##################################################################################################
import threading

def sumList(numbers, result):
    iSum = 0
    for no in numbers:
        iSum = iSum + no
    result["Sum"] = iSum

def prodList(numbers, result):
    iProd= 1
    for no in numbers:
        iProd = iProd * no
    result["Product"] = iProd


def main():
    lstLen = int(input("enter number of elements in list : "))
    numbers = []
    result = {}

    for i in range(lstLen):
        numbers.append(int(input()))

    sum = threading.Thread(target= sumList, args=(numbers, result))
    Product = threading.Thread(target= prodList, args = (numbers, result))

    sum.start()
    Product.start()

    sum.join()
    Product.join()

    # print(result)
    
    print("Sum of elements      : ", result["Sum"])
    print("Product of elements  : ", result["Product"])

if __name__=="__main__":
    main()

    