#############################################################################################################

# 1: Design a Python application that creates two separate threads named Even and Odd.

# • The Even thread should display the first 10 even numbers.

# • The Odd thread should display the first 10 odd numbers.

# • Both threads should execute independently using the threading module.

# • Ensure proper thread creation and execution.

#############################################################################################################

import threading

def numEven(no):
    print("Even numbers are  : ", end = " ")
    for i in range(0, no + 1):
        if i % 2 == 0:
            print(i, end = "  ")
        else:
            None
    print()

def numOdd(no):
    print("Odd numbers are   : ", end = " ")
    for i in range(0, no + 1):
        if i % 2 != 0:
            print(i, end = "  ")
        else:
            None
    print()

def main():
    num = int(input("Enter number to print even numbers till number : "))

    evenThread = threading.Thread(target = numEven, args = (num,))
    oddThread = threading.Thread(target = numOdd, args=(num,))

    evenThread.start()
    oddThread.start()

    evenThread.join()
    oddThread.join()

if __name__=="__main__":
    main()