#check perfect

def is_perfect_number(n):
    total = 0
    for i in range(1, n):          
        if n % i == 0:             
            total = total + i
    return total


def main():
    no = int(input("Enter number: "))
    if no > 0:
        result = is_perfect_number(no)
        if result == no:
            print(f"{no} is Perfect Number")
        else:
            print(f"{no} is Not Perfect Number")
    else:
        print("Enter number greater than 0")


if __name__ == "__main__":
    main()
