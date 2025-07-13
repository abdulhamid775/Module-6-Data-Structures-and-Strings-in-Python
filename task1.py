def get_student_marks():
    # Dictionary of students and their marks
    student_marks = {
        "Alice": 85,
        "Bob": 78,
        "Charlie": 92,
        "Diana": 88
    }

    # Ask user to input a student's name
    student_name = input("Enter the student's name: ")

    # Retrieve and display marks or appropriate message
    if student_name in student_marks:
        print(f"{student_name}'s marks: {student_marks[student_name]}")
    else:
        print("Student not found.")

if __name__ == "__main__":
    get_student_marks()
