#############################################################################################################

# Design a Python application that creates three threads named Small, Capital, and Digits.

# All threads should accept a string as input.

# The Small thread should count and display the number of lowercase characters.

# The Capital thread should count and display the number of uppercase characters.

# The Digits thread should count and display the number of numeric digits.

# Each thread must also display:

# Thread ID

# Thread Name

#############################################################################################################

import threading
import os

def smallChar(str):
    smallCnt = 0
    for chr in str:
        if chr.islower():
            smallCnt = smallCnt + 1
    print("Thread id of thread - small   : ",threading.get_ident())
    print("Thread name of thread - small : ",threading.current_thread().name)
    print("Count of lower case Characters: ",smallCnt)
    print()  

def CapitalChar(str):
    capitalCnt = 0
    for chr in str:
        if chr.islower():
            capitalCnt = capitalCnt + 1
    print("Thread id of thread - Capital   : ",threading.get_ident())
    print("Thread name of thread - Capital : ",threading.current_thread().name)
    print("Count of Capital case Characters: ", capitalCnt)
    print()

def DigitCount(str):
    digitCnt = 0
    for chr in str:
        if chr.isdigit():
            digitCnt = digitCnt + 1
    print("Thread id of thread - Digit   : ",threading.get_ident())
    print("Thread name of thread - Digit : ",threading.current_thread().name)
    print("Count of Digits in String     : ", digitCnt)
    print()



def main():
    str = "sandeepGHANWAT0085"
    
    small = threading.Thread(target=smallChar, args= (str, ))
    Capital = threading.Thread(target=CapitalChar, args= (str, ))
    Digits = threading.Thread(target=DigitCount, args= (str, ))

    small.start()
    Capital.start()
    Digits.start()

    small.join()
    Capital.join()
    Digits.join()

if __name__=="__main__":
    main()
