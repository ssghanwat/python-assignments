# 3. Arithmetic operations

def arithmetic_operations(a, b):
    div = 0.0
    if b!=0:
        div = a/b  
    return a+b, a-b, a*b, div
    
def main():
    no1 = eval(input("Enter first number : "))
    no2 = eval(input("Enter second number : "))

    Addition, substraction, multiplication, division = arithmetic_operations(no1, no2)
    print(f"Addition of a and b is {Addition}")
    print(f"substraction of a and b is {substraction}")
    print(f"multipplication of a and b is {multiplication}")
    print(f"division of a and b is {division}")
    


if __name__ == "__main__":
    main()