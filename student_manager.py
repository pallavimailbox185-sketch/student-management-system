import json
import os
from student import Student

FILE = "data.json"

class StudentManager:
    def __init__(self):
        self.students = []
        self.load()

    def load(self):
        if os.path.exists(FILE):
            with open(FILE, "r") as f:
                data = json.load(f)
                self.students = [Student(**s) for s in data]

    def save(self):
        with open(FILE, "w") as f:
            json.dump([s.to_dict() for s in self.students], f, indent=2)

    def add_student(self, student_id, name, grade):
        if any(s.student_id == student_id for s in self.students):
            print("❌ Error: Student ID already exists.")
            return
        self.students.append(Student(student_id, name, grade))
        self.save()
        print("✅ Student added successfully.")

    def update_student(self, student_id, name=None, grade=None):
        for s in self.students:
            if s.student_id == student_id:
                if name:  s.name = name
                if grade: s.grade = grade
                self.save()
                print("✅ Student updated.")
                return
        print("❌ Student not found.")

    def delete_student(self, student_id):
        original = len(self.students)
        self.students = [s for s in self.students if s.student_id != student_id]
        if len(self.students) < original:
            self.save()
            print("✅ Student deleted.")
        else:
            print("❌ Student not found.")

    def list_students(self):
        if not self.students:
            print("No students found.")
        else:
            for s in self.students:
                print(s)