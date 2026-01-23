# Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.

numSquares = lambda n: n**2  

def mapX(Task, Elements):
    Result = list()
    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)
    return Result

def main():
    numbers = [1, 2, 3, 4, 5]
    result = mapX(numSquares, numbers)
    print("Original numbers:", numbers)
    print("Squares of numbers: by user defined map", result)

    result_map = list(map(lambda n: n**2, numbers))  #user defined map
    print("Squares of numbers: by built-in map", result_map)

if __name__ == "__main__":
    main()
