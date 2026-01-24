# Write a program which accepts N numbers from the user and stores them into a list. 
# Return the addition of all prime numbers from that list.
# The main Python file accepts N numbers from the user and 
# passes each number to the ChkPrime() function, which is part of a 
# user-defined module - MarvellousNum.
# Name of the function from main file should be ListPrime()

import MarvellousNum

def ListPrime(numbers):
    iSum = 0

    for value in numbers:
        iSum = iSum + MarvellousNum.ChkPrime(value)

    return iSum

    
def main():
    numbers = []
    numEle = int(input("Enter the number of elements : "))
    
    for num in range(numEle):
        num = int(input())
        numbers.append(num)
    
    result = ListPrime(numbers)
    print("Addition of prime numbers from list : ", result)

    

if __name__=="__main__":
    main()
    
    