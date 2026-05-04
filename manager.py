import json
import os

from student import Student

FILE_PATH = "students.json"

class StudentManager:
    def __init__(self):
        self.students = []
        self.load()

    # ── Load from file ──────────────────────────────
    def load(self):
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, "r") as f:
                data = json.load(f)
                self.students = [Student.from_dict(d) for d in data]

    # ── Save to file ────────────────────────────────
    def save(self):
        with open(FILE_PATH, "w") as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)

    # ── Validation ──────────────────────────────────
    def id_exists(self, student_id):
        return any(s.student_id == student_id for s in self.students)

    # ── CRUD Operations ─────────────────────────────
    def add_student(self, student_id, name, grade):
        if self.id_exists(student_id):
            print(f"\n❌ Error: Student ID '{student_id}' already exists!")
            return False
        student = Student(student_id, name, grade)
        self.students.append(student)
        self.save()
        print(f"\n✅ Student '{name}' added successfully!")
        return True

    def update_student(self, student_id, name=None, grade=None):
        for s in self.students:
            if s.student_id == student_id:
                if name:
                    s.name = name
                if grade:
                    s.grade = grade
                self.save()
                print(f"\n✅ Student '{student_id}' updated successfully!")
                return True
        print(f"\n❌ Student ID '{student_id}' not found!")
        return False

    def delete_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                self.save()
                print(f"\n✅ Student '{student_id}' deleted successfully!")
                return True
        print(f"\n❌ Student ID '{student_id}' not found!")
        return False

    def list_students(self):
        if not self.students:
            print("\n📭 No students found.")
            return
        print("\n" + "=" * 48)
        print(f"| {'ID':<10} | {'Name':<20} | {'Grade':<10} |")
        print("=" * 48)
        for s in self.students:
            print(s)
        print("=" * 48)
        print(f"  Total students: {len(self.students)}")