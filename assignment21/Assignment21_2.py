###################################################################################################

# Design a Python application that creates two threads.

# Thread 1 should calculate and display the maximum element from a list.

# Thread 2 should calculate and display the minimum element from the same list.

# The list should be accepted from the user.

###################################################################################################

import threading

def MinNum(numbers):
    temp = numbers[0]
    for no in numbers:
        if no < temp:
            temp = no
    print("Minimum number is : ", temp)

def MaxNum(numbers):
    temp = numbers[0]
    for no in numbers:
        if no > temp:
            temp = no
    print("Maximum number is : ", temp)


def main():
    lstLen = int(input("enter number of elements in list : "))
    numbers = []

    for i in range(lstLen):
        numbers.append(int(input()))

    minimum = threading.Thread(target=MinNum, args=(numbers,))
    maximum = threading.Thread(target=MaxNum, args=(numbers,))

    minimum.start()
    maximum.start()

    minimum.join()
    maximum.join()


if __name__=="__main__":
    main()