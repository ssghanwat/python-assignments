###################################################################################################

# Design a Python application that creates two threads named Prime and NonPrime.

# Both threads should accept a list of integers.

# The Prime thread should display all prime numbers from the list.

# The NonPrime thread should display all non-prime numbers from the list.

###################################################################################################

import threading

def primeNum(numbers):
    print("Prime Numbers:", end=" ")
    for number in numbers:
        if number > 1:
            for value in range(2, number):
                if number % value == 0:
                    break
            else:
                print(number, end=" ")
    print()
    

def NonPrimeNum(numbers):
    print("\nNon-Prime Numbers:", end=" ")
    for number in numbers:
        if number <= 1:
            print(number, end=" ")
        else:
            for value in range(2, number):
                if number % value == 0:
                    print(number, end=" ")
                    break
    print()

def main():
    lstLen = int(input("enter number of elements in list : "))
    numbers = []

    for i in range(lstLen):
        numbers.append(int(input()))

    Prime = threading.Thread(target=primeNum, args=(numbers,))
    NonPrime = threading.Thread(target=NonPrimeNum, args=(numbers,))

    Prime.start()
    NonPrime.start()

    Prime.join()
    NonPrime.join()


if __name__=="__main__":
    main()