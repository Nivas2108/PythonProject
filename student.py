class student:
    passing_marks=0
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>self.passing_marks:
            print("PASS")
            return
        print("FAIL")
    @classmethod
    def update_passing_marks(cls,new_passing_marks):
        cls.passing_marks=new_passing_marks
    @staticmethod
    def grade(marks):
        if marks>90:
            print("A")
