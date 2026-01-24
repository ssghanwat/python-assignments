# Write a program which accepts one number and displays the given pattern.
#               *    *    *    *    *    
#               *    *    *    *    *    
#               *    *    *    *    *    
#               *    *    *    *    *    
#               *    *    *    *    *    
#               *    *    *    *    *    
#               *    *    *    *    *    


def printPattern(no):
    for i in range(no +1):
        for j in range(no):
            print("*", end="    ")
        print()

def main():
    no = eval(input("Enter number: "))
    printPattern(no)

    

if __name__ == "__main__":
    main()  