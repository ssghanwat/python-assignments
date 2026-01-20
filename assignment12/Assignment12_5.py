# print reverse number

def print_reverse_numbers(n):
    numbers = []
    for i in range(n, 0, -1):
        numbers.append(i)
    return numbers
    
def main():
    no1 = int(input("Enter number : "))
    if no1 > 0:
        result = print_reverse_numbers(no1)
        print(f"reverse number till {no1} are : ", end = " ")
        for value in result:
            print(value, end = " ")
        print()
    else:
        print("enter number greater than 0")

if __name__ == "__main__":
    main()