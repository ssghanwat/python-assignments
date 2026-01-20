# 4. Print even numbers till N

def print_even_numbers(n):
    lst = []
    for i in range(2, n + 1, 2):
        lst.append(i)
    return lst

def main():
    no  = int(input("Enter a number: "))
    if no > 0:
        result = print_even_numbers(no)
        print("Even numbers : ", end=" ")
        for value in result:
            print(value, end = " ")
        print()
    else:
        print("Please enter a positive integer.")

if __name__ == "__main__":
    main()