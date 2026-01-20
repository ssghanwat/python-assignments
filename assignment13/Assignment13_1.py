# 1. Area of rectangle
def area_rectangle(length, width):
    return length * width

def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    if length <= 0 or width <= 0:
        print("Length and width must be positive numbers.")
    else:
        area = area_rectangle(length, width)
        print(f"The area of the rectangle is: {area}")

if __name__ == "__main__":
    main()