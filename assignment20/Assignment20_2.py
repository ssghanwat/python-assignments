#############################################################################################################

# 2: Design a Python application that creates two threads named EvenFactor and OddFactor.

# -Both threads should accept one integer number as a parameter.

# - The EvenFactor thread should:
#   Identify all even factors of the given number.
#   Calculate and display the sum of even factors.

# - The OddFactor thread should:
#   Identify all odd factors of the given number.
#   Calculate and display the sum of odd factors.

# - After both threads complete execution, the main thread should display the message:
#   “Exit from main”

#############################################################################################################

import threading

def EvenFactor(num):
    iSum = 0
    print("Even Factors are       : ", end="  ")
    for i in range(1,num):
        if num % i == 0 and i % 2 == 0:
            print(i, end= "  ")
            iSum = iSum + i
        else:
            None
    print()
    print("Sum of Even Factors is : ",iSum)
    print()

def OddFactor(num):
    iSum = 0
    print("Odd Factors are       : ", end="  ")
    for i in range(1,num):
        if num % i == 0 and i % 2 != 0:
            print(i, end= "  ")
            iSum = iSum + i
        else:
            None
    print()
    print("Sum of Odd Factors is : ",iSum)
    print()

def main():
    no = int(input("Enter number : "))
    print()

    EvenFactorThread = threading.Thread(target = EvenFactor, args = (no,))
    OddFactorThread = threading.Thread(target =  OddFactor, args = (no,))

    EvenFactorThread.start()
    OddFactorThread.start()
    
    EvenFactorThread.join()
    OddFactorThread.join()

    print("Exit from main...")

if __name__=="__main__":
    main()