#multiplication table of a number

def multiplication_table(n):
    table = []
    for i in range(1, 11):
        table.append(n * i)   
    return table


def main():
    no = int(input("Enter a number: "))
    if no > 0:
        result = multiplication_table(no)

        print("Multiplication table:")
        for value in result:
            print(value, end=" ")
    else:
        print("Please enter a positive integer")


if __name__ == "__main__":
    main()
