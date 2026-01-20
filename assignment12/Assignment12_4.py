# 4. Print numbers from 1 to N

def print_numbers(n):
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
    return numbers
    
def main():
    no1 = eval(input("Enter number : "))
    if no1 > 0:
        result = print_numbers(no1)
        print(f"number till {no1} are : ", end = " ")
        for value in result:
            print(value, end = " ")
        print()
    else:
        print("enter number greater than 0")

if __name__ == "__main__":
    main()