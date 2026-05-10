import json

def load_students(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

def print_student_list(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : "
              f"ID = {student['Student_ID']} , "
              f"Email = {student['Email']}")

def main():
    filename = 'student.json'
    
    students = load_students(filename)
    
    print("-- This is the original Student list --")
    print_student_list(students)
    print()

    new_student = {
        "F_Name": "Anthony",
        "L_Name": "Garcia",
        "Student_ID": 12345,
        "Email": "AnthonyGarcia@yahoo.com"
    }
    students.append(new_student)

    print("-- This is the updated Student list --")
    print_student_list(students)
    print()

    with open(filename, 'w') as file:
        json.dump(students, file, indent=4)

    print("The student.json file was updated.")

if __name__ == "__main__":
    main()