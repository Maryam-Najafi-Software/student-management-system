import json
from student import Student


def save_students(students):
    students_data = []

    for student in students:
        data = {
            "name": student.name,
            "age": student.age,
            "score": student.score
        }

        students_data.append(data)

    with open("students.json", "w") as file:
        json.dump(students_data, file, indent=4)


def load_students():
    try:
        with open("students.json", "r") as file:
            students_data = json.load(file)

    except FileNotFoundError:
        return []

    students = []

    for data in students_data:
        student = Student(
            data["name"],
            data["age"],
            data["score"]
        )

        students.append(student)

    return students