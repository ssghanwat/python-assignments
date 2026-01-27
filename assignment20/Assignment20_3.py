#############################################################################################################

# 3: Design a Python application that creates two threads named EvenList and OddList.

# - Both threads should accept a list of integers as input.

# - The EvenList thread should:
#   Extract all even elements from the list.
#   Calculate and display their sum.

# - The OddList thread should:
#   Extract all odd elements from the list.
#   Calculate and display their sum.

# - Threads should run concurrently.

#############################################################################################################

import threading


def EvenAddition(lst):
    lstEven = []
    iSum = 0
    for no in lst:
        if no % 2 == 0:
            iSum = iSum + no
            lstEven.append(no)
    print("Even Elements from list are        : ", lstEven)
    print("Sum of Even Elements from list are : ", iSum)

def OddAddition(lst):
    lstOdd = []
    iSum = 0
    for no in lst:
        if no % 2 != 0:
            iSum = iSum + no
            lstOdd.append(no)
    print("Odd Elements from list are         : ", lstOdd )
    print("Sum of Odd Elements from list are  : ", iSum )



def main():
    no = int(input("enter number of elements in list : "))
    numbers = []

    for i in range(no):
        numbers.append(int(input()))

    EvenList = threading.Thread(target= EvenAddition, args = (numbers,))
    OddList = threading.Thread(target= OddAddition, args = (numbers,)) 

    EvenList.start()
    OddList.start()

    EvenList.join()
    OddList.join()

if __name__=="__main__":
    main()
