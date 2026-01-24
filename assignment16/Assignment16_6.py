# Write a program which accepts number from user and 
# checks whether that number is positive, negative, or zero.

def chknum(no):
    if no > 0:
        print("Positive Number")
    elif no < 0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    number = int(input("Enter a number: "))
    chknum(number)  

if __name__ == "__main__":
    main()  