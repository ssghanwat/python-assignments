#Write a program which contains one lambda function which accepts one parameter and returns power of two.


def power(num):
    square = lambda x : x ** 2
    return square(num)

def main():
    num = int(input("enter number : "))
    result = power(num)
    print("power of number is : ", result)

if __name__ == "__main__":
    main()