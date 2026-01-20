# 3. Factorial of a number

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
    
def main():
    no  = int(input("Enter a number: "))
    if no > 0:
        result = factorial(no)
        print("Factorial of the number:", result)
    else:
        print("Please enter a positive integer.")

if __name__ == "__main__":
    main()