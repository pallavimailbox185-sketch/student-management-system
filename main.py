from student_manager import StudentManager

def main():
    mgr = StudentManager()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. List all students")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            sid   = input("Student ID: ").strip()
            name  = input("Name: ").strip()
            grade = input("Grade: ").strip()
            mgr.add_student(sid, name, grade)

        elif choice == "2":
            sid   = input("Student ID to update: ").strip()
            name  = input("New name (leave blank to keep): ").strip() or None
            grade = input("New grade (leave blank to keep): ").strip() or None
            mgr.update_student(sid, name, grade)

        elif choice == "3":
            sid = input("Student ID to delete: ").strip()
            mgr.delete_student(sid)

        elif choice == "4":
            mgr.list_students()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()