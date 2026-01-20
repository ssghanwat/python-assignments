#  4. Reverse of a number

def reverse_number(n):
    iDigit = 0
    rev = 0
    while n > 0:
        iDigit = n % 10
        rev = (rev * 10) + iDigit
        n = n // 10
    return rev

def main():
    no = int(input("Enter a number: "))
    if no > 0:
        result = reverse_number(no)
        print(f"Reverse of {no} is {result}")
    else:
        print("Please enter a positive integer.")

if __name__ == "__main__":
    main()      