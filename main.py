from operations import (
    add_student,
    show_students,
    search_student,
    delete_student,
    calculate_average,
    update_student
)

from storage import save_students, load_students



students = load_students()


while True:
    print("\n===== Student Management System =====")
    print("1. Add student")
    print("2. Show students")
    print("3. Search student")
    print("4. Delete student")
    print("5. Calculate average")
    print("6. Update student")
    print("7. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_student(students)
        save_students(students)

    elif choice == "2":
        show_students(students)

    elif choice == "3":
        search_name = input("Enter name to search: ").strip()
        search_student(students, search_name)

    elif choice == "4":
        delete_name = input("Enter name to delete: ").strip()
        delete_student(students, delete_name)
        save_students(students)

    elif choice == "5":
        calculate_average(students)

    elif choice == "6":
        update_name = input("Enter name to update: ").strip()
        update_student(students, update_name)
        save_students(students)

    elif choice == "7":
        save_students(students)
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
