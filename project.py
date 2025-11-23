students = []
marks = {}

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    students.append({"name": name, "roll": roll})
    print("Student added successfully!")

def add_marks():
    roll = input("Enter roll number: ")
    subject = input("Enter subject: ")
    score = int(input("Enter marks: "))

    if roll not in marks:
        marks[roll] = []

    marks[roll].append({"subject": subject, "score": score})
    print("Marks added successfully!")

def show_students():
    print("\n--- Student List ---")
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}")

def show_report():
    print("\n--- Student Report ---")
    for s in students:
        roll = s["roll"]
        print(f"\n{s['name']} ({roll})")

        if roll not in marks or len(marks[roll]) == 0:
            print("No marks available")
        else:
            total = 0
            for m in marks[roll]:
                print(f"{m['subject']}: {m['score']}")
                total += m['score']
            
            average = total / len(marks[roll])
            print(f"Average: {average:.2f}")

def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Add Marks")
        print("3. Show Students")
        print("4. Show Report")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_marks()
        elif choice == "3":
            show_students()
        elif choice == "4":
            show_report()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

menu()
