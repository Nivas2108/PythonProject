class Student:
    total_students=0
    def __init__(self,name):
        self.name=name
        Student.total_students+=1
        print(f"new student has been created {self.name}.Total students={Student.total_students}")
s1=Student("Nivas")
s2=Student("nivas")