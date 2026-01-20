# 2. Count digits in a number

def count_digits(n):
    count = 0
    while n > 0:
        count = count + 1
        n = n // 10
    return count

def main():
    no = int(input("Enter a number: "))
    if no > 0:
        result = count_digits(no)
        print(f"Number of digits in {no} is {result}")
    else:
        print("Please enter a positive integer.")

if __name__ == "__main__":
    main()      