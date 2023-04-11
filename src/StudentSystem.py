"""
Hi There,

This code is a simple student management system that allows the user to add, list, find, and remove students. 

The program consists of two classes:
Student and StudentSystem. The Student class has four attributes: name, ID, grade, and address.

The StudentSystem class has four methods:
1 - add_student()
2 - list_students()
3 - find_student()
4 - remove_student()


The add_student() method prompts the user to enter the student's details, validates the input, and creates a new Student object.
The list_students() method prints the details of all the students that have been added.
The find_student() method prompts the user to enter the ID of the student they want to find, searches for the student with the given ID, and prints their details.
The remove_student() method prompts the user to enter the ID of the student they want to remove, searches for the student with the given ID, and removes them from the list of students.

 
 
The menu() function displays the menu options and prompts the user to enter their choice.
The main() function creates a new StudentSystem object, maps the menu options to the corresponding
methods of the StudentSystem object, and executes the corresponding method based on the user's choice.
The program runs until the user chooses to exit.


All The Best

"""

# Class Student


class Student:
    def __init__(self, name, ID, grade, address):
        self.name = name
        self.ID = ID
        self.grade = grade
        self.address = address


# Main Class
class StudentSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        # Prompt user to enter student details
        name = input("Enter name: ")
        while True:
            try:
                ID = int(input("Enter ID number: "))
                if ID <= 0:
                    raise ValueError
                if len(str(ID)) < 8:
                    raise ValueError("ID number must have at least 8 digits")
                break
            except ValueError as e:
                print(f"Invalid input. {e}")
        grade = input("Enter grade: ")

        # Prompt user to enter email address and validate it
        while True:
            address = input("Enter Email Address: ")
            if not address.endswith(("@gmail.com", "outlook.sa", "outlook.com", "hotmail.com")):
                print(
                    "Invalid email address. Must end with '@gmail.com', 'outlook.sa', 'outlook.com', or 'hotmail.com'.")
            else:
                break

        # Check if student with same ID already exists
        for student in self.students:
            if student.ID == ID:
                print("ID already exists. Student not added.")
                return

        # Create new student object and add it to the list of students
        student = Student(name, ID, grade, address)
        self.students.append(student)
        print(f"{student.name} added successfully")

    def list_students(self):
        # Check if any students have been added
        if not self.students:
            print("No students added yet")
            return

        # Print details of all students
        print("List of students:")
        for student_count, student in enumerate(self.students, start=1):
            print(f"""
Student Number : {student_count}
Name : {student.name}
ID : {student.ID}
Grade : {student.grade}
Email Address : {student.address}
---------------------------------------------
                    """
                  )

    def find_student(self):
        # Prompt user to enter ID of student to find
        try:
            ID = int(input("Enter ID number: "))
            if ID <= 0:
                raise ValueError
        except ValueError:
            print("Invalid input. ID number must be a positive integer.")
            return

        # Search for student with given ID and print their details
        student_count = 0
        for student in self.students:
            if student.ID == ID:
                student_count += 1
                print(f"""
Student Number : {student_count}
Name : {student.name}
ID : {student.ID}
Grade : {student.grade}
Email Address : {student.address}
--------------------------------------
                        """
                      )

        # If no student with given ID is found, print a message
        if student_count == 0:
            print("Student not found")

    def remove_student(self):
        # Prompt user to enter ID of student to remove
        try:
            ID = int(input("Enter ID number: "))
            if ID <= 0:
                raise ValueError
        except ValueError:
            print("Invalid input. ID number must be a positive integer.")
            return

        # Search for student with given ID and remove them from the list of students
        for student in self.students:
            if student.ID == ID:
                self.students.remove(student)
                print(f"{student.name} removed successfully")
                return

        # If no student with given ID is found, print a message
        print("Student not found")


def menu():
    # Display menu options and prompt user to enter their choice
    print("\nStudent System")
    print("1. Add Student")
    print("2. List Students")
    print("3. Find Student")
    print("4. Remove Student")
    print("5. Exit")
    return input("Enter your choice: ")


def main():
    # Create a new student system object
    student_system = StudentSystem()

    # Map menu options to corresponding methods of the student system object
    options = {
        "1": student_system.add_student,
        "2": student_system.list_students,
        "3": student_system.find_student,
        "4": student_system.remove_student,
        "5": exit,
    }

    # Display menu and execute corresponding method based on user's choice
    while True:
        choice = menu()
        func = options.get(choice, lambda: print("Invalid choice"))
        func()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
