import os

MIN_MARKS = 0
MAX_MARKS = 100
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")   # no hard-coded secret

students = []


def is_valid_marks(marks):
    return MIN_MARKS <= marks <= MAX_MARKS


def add_student(name, marks):
    student_id = len(students) + 1
    students.append({"id": student_id, "name": name, "marks": marks})


def average():
    if not students:
        return 0.0
    return sum(s["marks"] for s in students) / len(students)


def highest():
    if not students:
        return MIN_MARKS
    return max(s["marks"] for s in students)


def search(name):
    for student in students:
        if student["name"] == name:
            return student
    return None


def grade(marks):
    if not is_valid_marks(marks):
        return "Invalid"
    if marks >= 90:
        return "A"
    if marks >= 80:
        return "B"
    if marks >= 70:
        return "C"
    if marks >= 60:
        return "D"
    return "F"


def print_report():
    print("=== STUDENT REPORT ===")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | "
              f"Marks: {s['marks']} | Grade: {grade(s['marks'])}")
    print(f"Total students: {len(students)}")
    print(f"Average: {average()}")
    print(f"Highest: {highest()}")
    print("=== END REPORT ===")


def read_marks():
    try:
        marks = int(input("Marks: "))
    except ValueError:
        print("Marks must be a whole number.")
        return None
    if not is_valid_marks(marks):
        print(f"Marks must be between {MIN_MARKS} and {MAX_MARKS}.")
        return None
    return marks


def handle_add():
    name = input("Name: ")
    marks = read_marks()
    if marks is not None:
        add_student(name, marks)


def main():
    actions = {
        "1": handle_add,
        "2": lambda: print(average()),
        "3": lambda: print(highest()),
        "4": print_report,
        "5": lambda: print(search(input("Name: ")) or "Student not found."),
    }
    while True:
        choice = input("1.Add 2.Avg 3.Highest 4.Show 5.Search 6.Exit: ")
        if choice == "6":
            break
        action = actions.get(choice)
        if action:
            action()


if __name__ == "__main__":
    main()
