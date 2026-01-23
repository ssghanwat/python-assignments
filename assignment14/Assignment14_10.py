#lambda funnction to acept three numbers and return largest number 


numMult = lambda a, b, c : a if a > b and a > c else b if b > a and b > c else c

def main():
    no1 = eval(input("Enter first number : "))
    no2 = eval(input("Enter second number : "))
    no3 = eval(input("Enter Third number : "))

    result = numMult(no1, no2, no3)
    print("Largest number is :", result)


if __name__ == "__main__":
    main()