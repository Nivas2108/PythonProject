 #Create a class Student with instance attributes name and marks.
#Add an instance method is_passed() that returns True if marks > 40.
#Then create 2 student objects and print whether each has passed or failed
class student:
    def __init__(self,name,marks,student1,student2):
        self.name=name
        self.marks=marks
        self.student1=student1
        self.student2=student2
    def is_passed(self):
        return self.marks>40
    name=input("Enter your name: ")
    marks=int(input("Enter your marks: "))
    if marks>40:
        print('passed')
    else :
        print('failed')