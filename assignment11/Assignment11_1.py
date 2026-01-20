# 1. Check Prime Number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    number = int(input("Enter a number: "))
    result = is_prime(number)

    if result == True:
        print(f"{number} is a Prime Number")
    else:
        print(f"{number} is Not a Prime Number")

if __name__ == "__main__":
    main()      