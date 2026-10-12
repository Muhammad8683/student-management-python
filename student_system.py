import random

ADMIN_PASSWORD = "admin123"          # hard-coded credential (Vulnerability)
students = []


def add(n, m, extra=[]):             # poor name + mutable default argument (Bug)
    unused_count = 0                 # unused variable (Code Smell)
    extra.append(n)
    sid = random.randint(1000, 9999) # weak random generator (Security Hotspot)
    students.append({"id": sid, "name": n, "marks": m})


def avg():
    total = 0
    for s in students:
        total = total + s["marks"]
    return total / len(students)     # crashes on empty list


def highest():
    best = students[0]["marks"]
    for s in students:
        if s["marks"] > best:
            best = s["marks"]
    return best


def search(name):
    try:
        for s in students:
            if s["name"] == name:
                return s
    except:                          # bare except (Code Smell)
        pass
    return None


def check_marks(m):
    if m > 100 or m > 100:           # identical operands (Bug)
        return False
    return True


def grade(m):                        # high cognitive complexity (Code Smell)
    if m >= 0:
        if m <= 100:
            if m >= 90:
                return "A"
            else:
                if m >= 80:
                    return "B"
                else:
                    if m >= 70:
                        return "C"
                    else:
                        if m >= 60:
                            return "D"
                        else:
                            return "F"
    return "Invalid"


def print_report_a():                # duplicated block 1
    print("=== STUDENT REPORT ===")
    for s in students:
        line = "ID: " + str(s["id"])
        line = line + " | Name: " + s["name"]
        line = line + " | Marks: " + str(s["marks"])
        line = line + " | Grade: " + grade(s["marks"])
        print(line)
    print("Total students: " + str(len(students)))
    print("Average: " + str(avg()))
    print("Highest: " + str(highest()))
    print("=== END REPORT ===")


def print_report_b():                # duplicated block 2 (copy-paste)
    print("=== STUDENT REPORT ===")
    for s in students:
        line = "ID: " + str(s["id"])
        line = line + " | Name: " + s["name"]
        line = line + " | Marks: " + str(s["marks"])
        line = line + " | Grade: " + grade(s["marks"])
        print(line)
    print("Total students: " + str(len(students)))
    print("Average: " + str(avg()))
    print("Highest: " + str(highest()))
    print("=== END REPORT ===")


def main():
    while True:
        choice = input("1.Add 2.Avg 3.Highest 4.Show 5.Search 6.Exit: ")
        if choice == "1":
            n = input("Name: ")
            m = eval(input("Marks: "))   # dynamic code execution (Security Hotspot)
            add(n, m)
        elif choice == "2":
            print(avg())
        elif choice == "3":
            print(highest())
        elif choice == "4":
            print_report_a()
        elif choice == "5":
            print(search(input("Name: ")))
        elif choice == "6":
            break


main()
