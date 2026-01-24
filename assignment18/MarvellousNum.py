# Function to check prime and return number if prime
def ChkPrime(no):
    if no <= 1:
        return 0

    for i in range(2, no):
        if no % i == 0:
            return 0

    return no   # return number if prime
