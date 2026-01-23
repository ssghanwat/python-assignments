# Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.

# Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.

# Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.

# Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.

# Write a lambda function using reduce() which accepts a list of numbers and returns the minimum element.

# Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

# Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

# Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.

# Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.



numEven = lambda n : n % 2 == 0


def filterX(task, Elements):
    Result = []

    for no in Elements:
        Ret = task(no)

        if Ret == True:
            Result.append(no)

    return Result


def main():

    lstLength  = int(input("Enter number of elements to enter : ")) 
    numbers = []
    for i in range(lstLength):
        numbers.append(int(input()))
    
    result = filterX(numEven, numbers)
    print("Even number are : ", end= " ")
    for i in result:
        print(i, end=" ")
    print()


    res = list(filter(lambda x : x % 2 == 0, numbers))
    print("Even number are :",*res, "   using built-in filter")
    print()

if __name__=="__main__":
    main()