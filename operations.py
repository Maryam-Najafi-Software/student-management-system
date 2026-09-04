from student import Student


def add_student(students):
    name = input("Enter name: ").strip()

    while True:
        try:
            age = int(input("Enter age: "))

            if age <= 0:
                print("Invalid age.")
                continue

            break

        except ValueError:
            print("Invalid age.")
            continue

    while True:
        try:
            score = int(input("Enter score: "))

            if score < 0 or score > 100:
                print("Invalid score.")
                continue

            break

        except ValueError:
            print("Invalid score.")
            continue

    new_student = Student(name, age, score)
    students.append(new_student)

    print("Student added successfully.")


def show_students(students):
    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print(student)


def search_student(students, search_name):
    for student in students:
        if student.name.lower() == search_name.lower():
            print(f"Found: {student}")
            return

    print("Student not found.")


def delete_student(students, delete_name):
    for student in students:
        if student.name.lower() == delete_name.lower():
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def calculate_average(students):
    if len(students) == 0:
        print("No students.")
        return

    total = 0

    for student in students:
        total += student.score

    average = total / len(students)

    print(f"Average score: {average:.2f}")


def update_student(students, update_name):
    for student in students:
        if student.name.lower() == update_name.lower():

            print(f"Current information: {student}")

            while True:
                try:
                    new_age = int(input("Enter new age: "))

                    if new_age <= 0:
                        print("Invalid age.")
                        continue

                    break

                except ValueError:
                    print("Invalid age.")
                    continue

            while True:
                try:
                    new_score = int(input("Enter new score: "))

                    if new_score < 0 or new_score > 100:
                        print("Invalid score.")
                        continue

                    break

                except ValueError:
                    print("Invalid score.")
                    continue

            student.age = new_age
            student.score = new_score

            print("Student updated successfully.")
            return

    print("Student not found.")