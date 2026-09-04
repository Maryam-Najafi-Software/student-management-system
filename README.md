# Student Management System

A simple command-line Student Management System built with Python.

This project was created to practice Object-Oriented Programming, functions, modules, exception handling, file handling, and JSON data persistence.

## Features

* Add a student
* Show all students
* Search for a student
* Delete a student
* Update student information
* Calculate average score
* Validate age and score input
* Save student data to a JSON file
* Load student data when the application starts

## Project Structure

```text
student-management-system/
│
├── main.py
├── student.py
├── operations.py
├── storage.py
├── students.json
├── README.md
└── .gitignore
```

### `student.py`

Contains the `Student` class and student attributes.

### `operations.py`

Contains the main operations for managing students.

### `storage.py`

Handles saving and loading student data using JSON.

### `main.py`

Contains the command-line menu and controls the application flow.

## Requirements

* Python 3.x

No external Python packages are required.

## How to Run

Clone the repository and run:

```bash
python main.py
```

## Data Persistence

Student information is stored in `students.json`.

When the application starts, existing student data is loaded from the JSON file.

When a student is added, deleted, or updated, the changes are saved back to the file.

## Example

```text
===== Student Management System =====
1. Add student
2. Show students
3. Search student
4. Delete student
5. Calculate average
6. Update student
7. Exit

Enter your choice:
```

## Concepts Practiced

* Object-Oriented Programming (OOP)
* Classes and Objects
* Functions
* Lists
* Dictionaries
* Loops
* Conditional Statements
* Exception Handling
* Modules and Imports
* File Handling
* JSON
* Basic Data Persistence

## Author

Maryam Najafi
