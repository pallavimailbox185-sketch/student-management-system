from student_manager import StudentManager

def menu():
    manager = StudentManager()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sid = input("Enter ID: ")
            name = input("Enter Name: ")
            grade = input("Enter Grade: ")
            manager.add_student(sid, name, grade)

        elif choice == "2":
            manager.list_students()

        elif choice == "3":
            sid = input("Enter ID to update: ")
            name = input("Enter new name (leave blank to skip): ")
            grade = input("Enter new grade (leave blank to skip): ")
            manager.update_student(sid, name or None, grade or None)

        elif choice == "4":
            sid = input("Enter ID to delete: ")
            manager.delete_student(sid)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
    