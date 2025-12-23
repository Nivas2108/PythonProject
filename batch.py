class student:
    batch="P2"
    def __init__(self,name):
        self.name=name
    def change_batch(self,new_batch):
        self.batch=new_batch
s1=student("a")
s2=student("b")
s3=student("c")
s1.change_batch("P3")
print(s1.batch)
print(s2.batch)
print(s3.batch)