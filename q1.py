class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
        return self.marks > 40
student1 = Student("NIVAS", 55)
student2 = Student("HARSHA", 38)
for student in [student1, student2]:
    status = "Passed" if student.is_passed() else "Failed"
    print(f"{student.name} has {status}")
