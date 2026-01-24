#Check prime number 

def chkPrime(no):
    if no <= 1:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True


def main():
    no = eval(input("Enter number: "))
    result = chkPrime(no)
    if result == True:
        print("Prime NUmber")
    else:
        print("Not prime number")
if __name__=="__main__":
    main()

