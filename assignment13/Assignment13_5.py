#Display Grade

def display_grade(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "First Class"
    elif marks >= 50:
        return "Second Class"
    else:
        return "Fail"

def main():
    marks = eval(input("Enter marks: "))
    if marks > 0:
        grade = display_grade(marks)   
        print("Grade:", grade)         
    else:
        print("Please enter valid marks.")

if __name__ == "__main__":
    main()
