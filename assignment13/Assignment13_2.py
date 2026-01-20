# 1. Area of circle

def area_circle(r, PI = 3.14):
    return PI * r * r

def main():
    radius = float(input("Enter the radius of the circle: "))

    if radius <= 0:
        print("Radius must be a positive number.")
    else:
        area = area_circle(radius)
        print(f"The area of the circle is: {area}")

if __name__ == "__main__":
    main()