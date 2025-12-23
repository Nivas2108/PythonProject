# Create a class Course with:
#•	class variable total_students
#•	instance variable student_name
#•	instance method enroll() → increments total_students
#•	class method show_total(cls) → prints total students
#•	static method is_eligible(age) → returns True if age ≥ 18
#Demonstrate enrolling multiple students and show total count.
class Course:
    total_students=0
    def __init__(self,name):
        self.name=name
    def enroll(self):
        self.total_students=self.total_students + 1
    @classmethod
    def show_students(cls):
        return cls.total_students
    @staticmethod
    def is_eligible(age):
        return age>18
c1=Course("C1")
c2=Course("C2")
c1.enroll()
c2.enroll()
print(Course.total_students)
print(c1.total_students)
print(c1.show_students())