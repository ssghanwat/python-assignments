#############################################################################################################

# 5: Design a Python application that creates two threads named Thread1 and Thread2.

# Thread1 should display numbers from 1 to 50.

# Thread2 should display numbers from 50 to 1 in reverse order.

# Ensure that:

# Thread2 starts execution only after Thread1 has completed.

# Use appropriate thread synchronization.

#############################################################################################################

import threading

def displayNum(no):
    for i in range(1, no+1, 1):
        print(i , end="   ")
    print()

def displayRev(num):
    for i in range(num, 0, -1):
        print(i , end="   ")
    print()

def main():
    num = int(input("Enter Number : "))

    Thread1 = threading.Thread(target=displayNum, args=(num,))
    Thread1.start()
    Thread1.join()

    Thread2 = threading.Thread(target=displayRev, args=(num,))
    Thread2.start()
    Thread2.join()
    
if __name__=="__main__":
    main()
