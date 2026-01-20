#  5. Check Palindrome

def check_pallindrome(n):
    rev = 0
    iDigit = 0

    while n > 0:
        iDigit = n % 10
        rev = (rev * 10) + iDigit
        n = n // 10
    return rev

def main():
    no = int(input("Enter a number: "))
    if no > 0:
        result = check_pallindrome(no)
        if result == no:
            print(f"{no} is a palindrome.")
        else:
            print(f"{no} is not a palindrome.")
    else:
        print("Please enter a positive integer.")

if __name__ == "__main__":
    main()      