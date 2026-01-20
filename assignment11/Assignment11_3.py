# 3. Sum of digits

def sum_of_digits(n):
    total = 0
    while n > 0:
        idigit = n % 10
        total = total + idigit
        n = n // 10
    return total

def main():
    no = int(input("Enter a number: "))
    if no > 0:
        result = sum_of_digits(no)
        print(f"Sum of digits in {no} is {result}")
    else:
        print("Please enter a positive integer.")

if __name__ == "__main__":
    main()      