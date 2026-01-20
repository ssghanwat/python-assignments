#Write a program which contains one function named as cubeNumber()
#that gives square of the number on console


def cubeNumber(a):  
    return a * a * a

def main():

    no = int(input("Enter a number: "))
    
    if no >= 0:
        result = cubeNumber(no)
        print("Cube of the number is:", result)
    else:
        print("Please enter a non-negative number.")
                
if __name__ == "__main__":
    main()