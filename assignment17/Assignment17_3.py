# Write a program which accepts one number from the user and returns its factorial.

def factorial(no):
    iFact = 1
    for i in range(1, no+1):
        iFact = iFact * i
    return iFact
        
def main():
    no = eval(input("Enter number: "))
    result = factorial(no)
    print("Factorial is : ", result)

    

if __name__ == "__main__":
    main()  


# 1*1 = 1
# 2*1 = 2
# 3*2 = 6
# 4*6 = 24
# 5*24 = 120