# 2. Sum of first N natural numbers

def sum_natural_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total
    
def main():
    no  = int(input("Enter a number: "))
    if no > 0:
        result = sum_natural_numbers(no)
        print("Sum of first natural numbers:", result)
    else:
        print("Please enter a positive integer.")

if __name__ == "__main__":
    main()