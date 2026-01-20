# 5. Print odd numbers till N


def print_odd_numbers(n):
    lst = []
    for i in range(1, n + 1, 2):
        lst.append(i)
    return lst

def main():
    no  = int(input("Enter a number: "))
    if no > 0:
        result = print_odd_numbers(no)
        print("odd numbers : ", end=" ")
        for value in result:
            print(value, end = " ")
        print()
    else:
        print("Please enter a positive integer.")

if __name__ == "__main__":
    main()