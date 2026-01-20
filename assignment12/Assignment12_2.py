# 2. Print factors of a number

def print_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
            
    return factors
    
def main():
    no = int(input("Enter a number : "))
    if no > 0:
        result = print_factors(no)
        print(f"factors of {no} are : ", end = " ")
        for value in result:
            print(value, end = " ")
        print()
    else:
        print("enter number greater than 0")

if __name__ == "__main__":
    main()